# how the code handles tags. "false" ignores the tag, "str" adds quotes and "dta" is for numbers and bools.
# "li" is for non-text-carrying list elements.  Nested dicts are supported.

def getElemDict():
    return {

        # These tags can be ignored by the wiki (at least currently)
        "defName": False,  # parsed in the actual code
        "graphicData": False,
        "resourceReadoutPriority": False,
        "altitudeLayer": False,
        "socialPropernessMatters": False,  # if you can use this item inside a prisoner's room
        "drawGUIOverlay": False,  # research what this does
        "uiIconForStackCount": False,  # research what this does
        "rotatable": False,  # may become useful with future defs
        "soundInteract": False,
        "soundDrop": False,

        # mostly standard element tags
        "label": "str",
        "description": "str",
        "statBases": {
            "DeteriorationRate": "dta",
            "MarketValue": "dta",
            "Mass": "dta",
            "WorkToMake": "dta",
            "Nutrition": "dta",
            "MaxHitPoints": "dta",
            "Flammability": False,
            "Beauty": "dta",
            "FoodPoisonChanceFixedHuman": "dta",
        },
        "ingestible": {
            "preferability": "str",
            "optimalityOffsetHumanlikes": "dta",
            "optimalityOffsetFeedingAnimals": "dta",
            "ingestEffect": False,
            "ingestSound": False,
            "foodType": "str",
            "maxNumToIngestAtOnce": "dta",
            "tasteThought": "str",
            "canAutoSelectAsFoodForCaravan": "dta",  # fun fact: royal jelly is the only food with this as false
            "joy": "dta",
            "joyKind": "str",
        },
        "thingClass": "str",
        "category": "str",
        "useHitPoints": False,  # Could be useful?
        "healthAffectsPrice": "dta",
        "selectable": False,
        "stackLimit": "dta",
        "tickerType": "str",  # What the heck is this var for?
        "thingCategories": {
            "li": "li",
        },
        "alwaysHaulable": "dta",
        "comps": {
            "li": "li",
        },
        "pathCost": "???",  # Research what this does
        "tradeability": "str",



    }
