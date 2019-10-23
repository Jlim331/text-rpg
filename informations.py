Weapons = {
    "Stick": {
        "ATTACK": 3,
        "DURABILITY": 5,
        },
    "Iron Sword": {
        "ATTACK": 15,
        "DURABILITY": 20,
        "SHARPNESS": 10,
        }
    }

for weapon, info in Weapons.items():
    print(weapon)
    if 'ATTACK' in info.keys():
        print(f"\tAttack: {info['ATTACK']}")
    if 'DURABILITY' in info.keys():
        print(f"\tDurability: {info['DURABILITY']}")
    if 'SHARPNESS' in info.keys():
        print(f"\tSharpness: {info['SHARPNESS']}")

Mobs = {
    "Spider": {
        "ATTACK": 3,
        "HP": 10,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
    }

for mob, info in Mobs.items():
    print(mob)
    if 'ATTACK' in info.keys():
        print(f"\tAttack: {info['ATTACK']}")
    if 'HP' in info.keys():
        print(f"\tHP: {info['HP']}")
    if 'VITALITY' in info.keys():
        print(f"\tVitality: {info['VITALITY']}")
    if 'DEFENSE' in info.keys():
        print(f"\tDefense: {info['DEFENSE']}")
    if 'LUCK' in info.keys():
        print(f"\tLuck: {info['LUCK']}")

hero = {
    "inventory":["map", "flashlight"],
    "stats": {
        "ATTACK": 10,
        "HP": 100,
        "VITALITY": 10,
        "DEFENSE": 10,
        "LUCK": 0,
        }
}

for character, info in hero.items():
    print(character)
