# Josh Lim
# Comp Sci 30 P4
# 10/29/2019
# Simple action menu for Game


def menuSample(menuName):
    global choice
    choices = list(menuName)
    for key in menuName:
        print("\tPath " + key)
    choice = input("What path shall thoust choose?\n")
    for key in menuName:
        if choice == key:
            print(f"You have chose Path {key}")
        while str(choice) not in choices:
            print(f"I got, {str(choices)[1:-1]} watchu want?")
            choice = input("")
            for key in menuName:
                if choice == key:
                    print(f"You have chose Path {key}")
startPath = {
    "1": "A level 1 mob appears",
    "2": """You find yourself in a room, you have a choice to go left or
    right""",
    "3": "You are in a forest."
}
print("Welcome to Mazy Boi")
menuSample(startPath)
