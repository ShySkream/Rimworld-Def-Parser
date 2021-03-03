# Rimworld-Def-Parser
This script pulls game data from Rimworld's Defs files and parses it for the Rimworld wiki.  The output format is a LUA dictionary, which is then manually uploaded to *Module:DefInfo/Data*.  

**If you wish to contribute**, the easiest way most people can help is filling in the ElementDict, which is what filters out useful parts of the Defs to go on the wiki.  We ignore a fair amount of the data since we don't want to put more load on the server than needed, but if there is a variable that would be useful, feel free to add it.  

The code currently has these defs fully parsed:

- all foods
- animal products
- raw plants (harvested)

These are the defs that are being parsed now:
- animals

Finally, these are the sections we plan to parse in the near future:
- materials
- clothing/apparel
- weapons
- furniture
- drugs

To get the code working, make sure to set the paths to the XML files in **PathConfig.py**.

