def nestedDictPrinter(dictName):
    """Prints out content in a nested dictionary up to 2 layers,
    takes dictName as the dictionary name.
    """
    for dictName, key in dictName.items():
        """loops through the keys in the nested dictionary, dictName, and then
        prints the nested dictionary names along with its values.
        """
        print(dictName.title()) # prints nested dictionary name
        for items in key:
            """loops through nested dictionary key values and and prints the
            key along with the value with a tab before.
            """
            print(f"\t{items}: {info[items]}")
# Nested dictinoary containing information for weapons
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
# Nested dictinoary containing information for mobs
mobs = {
    "spider": {
        "ATTACK": 3,
        "HP": 10,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
    }
# Nested dictinoary containing information for hero
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
    """loops through the nested dictionary, character and its keys and then
    prints out the nested dictionary name.
    """
    print(character.title())
    if character == "inventory":
        for items in key:
            """loops through nested dictionary key values and and prints the
            key along with the value with a tab before if the key is
            "inventory"
            """
            print(f"\t{items}")
    if character == "stats":
        for items in key:
            """loops through nested dictionary key values and and prints the
            key along with the value with a tab before if the key is
            "stats"
            """
            print(f"\t{items}: {info[items]}")
# Prints out the content of the weapons nested dictionary
nestedDictPrinter(weapons)
# Prints out the content of the mobs nested dictionary
nestedDictPrinter(mobs)
