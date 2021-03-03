# how the code handles tags. "false" ignores the tag, "str" adds quotes and "dta" is for numbers and bools.
# Nested dicts are supported.

def getElemDict():
    return {
    "defName": False,
    "label": "str",
    "description": "str",
    "graphicData": False,
    "statBases": {
        "DeteriorationRate": "dta",
        "MarketValue": "dta",
        "Mass": "dta",
        "Nutrition": "dta",
        "Beauty": "dta",
    },
    "stackLimit": "dta",
    "socialPropernessMatters": False,
    }
