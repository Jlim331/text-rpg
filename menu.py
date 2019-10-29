# Josh Lim
# Comp Sci 30 P4
# 10/29/2019
# Simple action menu for Game


def menuSample(menuName):
    global choice
    for key in menuName:
        print("\tPath " + key)
    choice = input("")
    for key in menuName:
        if choice == key or choice == "path " + key or choice == "Path " + key:
            print(f"You have chose Path {key}")
        while choice not in ["1", "2", "3",]:
            print("Invalid input, please try again.")
            choice = input("")
            for key in menuName:
                if choice == key or choice == "path " + key or choice == "Path " + key:
                    print(f"You have chose Path {key}")
menu = {
    "1": "A level 1 mob appears",
    "2": """You find yourself in a room, you have a choice to go left or
    right""",
    "3": "You are in a forest."
}
print("Welcome to Mazy Boi \nWhat path shall thoust choose?")
menuSample(menu)
