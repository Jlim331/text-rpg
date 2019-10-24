def nestedDictPrinter(dictName):
    """Prints out contents in a nested dictionary up to 2 layers,
    dictName is the dictionary name
    """
    for dictName, info in dictName.items():
        print(dictName.title())
        for items in info:
            print(f"\t{items}: {info[items]}")

weapons = {
    "stick": {
        "ATTACK": 3,
        "DURABILITY": 5,
        },
    "iron sword": {
        "ATTACK": 15,
        "DURABILITY": 20,
        "SHARPNESS": 10,
        }
    }
mobs = {
    "spider": {
        "ATTACK": 3,
        "HP": 10,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
    }
hero = {
    "inventory": ["map", "flashlight"],
    "stats": {
        "ATTACK": 10,
        "HP": 100,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
}
for character, info in hero.items():
    print(character.title())
    if character == "inventory":
        for items in info:
            print(f"\t{items}")
    if character == "stats":
        for items in info:
            print(f"\t{items}: {info[items]}")
nestedDictPrinter(weapons)
nestedDictPrinter(mobs)
