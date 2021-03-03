import xml.etree.ElementTree as ET
from pathlib import Path
import ElementDict
import PathConfig

dataPath = PathConfig.getDataPath()
toParsePath = PathConfig.getToParsePath()
elementDict = ElementDict.getElemDict()

named_defs = {}  # used for inheritance, all defs that could possibly be referenced as parents get parsed into here
named_defs_processing = {}  # named classes that are also children (empty after inheritance processing)
named_defs_processed = []  # Names of defs in named_defs_processing that can be removed (this is stupid/messy code)


def GetParent(parentName):  # small function to simplify pulling data from named_defs and converting it
    return ET.fromstring(named_defs.get(parentName))


def InheritAttribs(childDef, parentDef):  # recursive inheritance function
    for defParentElem in parentDef:
        if childDef.find(defParentElem.tag) is None:  # if the element isn't overwritten
            childDef.append(defParentElem)  # add it to the child
        else:
            if defParentElem.find("./") is not None:  # if the element has children
                InheritAttribs(childDef.find(defParentElem.tag), defParentElem)  # recursively call this function
    return childDef


def ProcessInheritance(path):  # runs before actual data parsing.  Sorts out all possible parents and nested parents.
    for file in Path(path).rglob('*.xml'):  # load all XML files found at 'path'
        tree = ET.parse(file)
        root = tree.getroot()
        for defItem in root:
            if defItem.attrib.get("Name") is not None:  # if the def is named
                if defItem.attrib.get("ParentName") is not None:  # if the def has a parent
                    named_defs_processing.setdefault(defItem.attrib.get("Name"), ET.tostring(defItem))  # save the def
                else:
                    named_defs.setdefault(defItem.attrib.get("Name"), ET.tostring(defItem))  # save the def

    while named_defs_processing:  # while there are named defs that need processing
        for defItemName in named_defs_processing:  # get the names of defs
            defItem = ET.fromstring(named_defs_processing[defItemName])  # get the actual defs
            if named_defs.get(defItem.attrib.get("ParentName")) is not None:  # if the parent is already processed...
                defParent = GetParent(defItem.attrib.get("ParentName"))  # load parent data
                InheritAttribs(defItem, defParent)  # process this element
                named_defs.setdefault(defItemName, ET.tostring(defItem))  # add this def to the completed list
                named_defs_processed.append(defItemName)  # add this def to be removed from processing

        for defToRemove in named_defs_processed:  # for each element to be removed
            named_defs_processing.pop(defToRemove)  # remove it
        named_defs_processed.clear()
    print("Inheritance processing complete!")


def printTabs(tabNum):  # prints the number of tabs specified.  Code here could be better
    for i in range(0, tabNum):
        print("\t", end='')


def ProcessFile(root):
    for defItem in root:
        if defItem.find("defName") is not None:  # is an actual def
            print('\t["' + defItem.find("defName").text + '"] = {')
            if defItem.attrib.get("ParentName") is not None:  # if the def has a parent
                defItem = InheritAttribs(defItem, GetParent(defItem.attrib.get("ParentName")))

            for element in defItem:
                processElement(element, elementDict, 2)
            print("\t},")


def processElement(elem, processDict, tabbing):

    process = processDict.get(elem.tag)

    if process is None:
        printTabs(tabbing)
        print("-- ERROR: no process for tag", elem.tag)

    elif process is False:
        True  # do nothing!  false means ignore this tag

    elif process == "str":
        printTabs(tabbing)
        print('["' + elem.tag + '"] = "' + elem.text + '",')

    elif process == "dta":
        printTabs(tabbing)
        print('["' + elem.tag + '"] = ' + elem.text + ',')

    elif isinstance(process, dict):
        printTabs(tabbing)
        print('["' + elem.tag + '"] = {')
        for subElem in elem:
            processElement(subElem, process, tabbing + 1)

    else:
        print("-- ERROR:", elem.tag, "is set to nonexistent process", process)


if __name__ == '__main__':
    ProcessInheritance(dataPath)
    print("return {")
    for XMLFile in Path(toParsePath).rglob('*.xml'):
        myTree = ET.parse(XMLFile)
        myRoot = myTree.getroot()
        ProcessFile(myRoot)
    print("}")
