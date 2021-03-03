# this file specifies file paths to the .XML that contain the defs.

def getDataPath():
    return "C:/Program Files (x86)/Steam/steamapps/common/RimWorld/Data"
    # Set this to point at the 'Data' folder in your Rimworld installation, or a copy of it.
    # This is required even when parsing small amounts of data because inheritance can run between files.


def getToParsePath():
    return "./toParse"
    # put the .XML files you wish to parse into this folder, or any sub-folder
