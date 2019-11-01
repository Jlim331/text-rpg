# Josh Lim
# Comp Sci 30 P4
# 10/29/2019
# Simple action menu for Game


def menuSample(menuName):
    """Function that will take a dictionary, menuName, and converts it to a
    text-based menu
    """
    # Used for determining the next path
    global choice
    # Creates a list of keys for error checking
    choices = list(menuName)
    # Prints keys
    for key in menuName:
        print("\tPath " + key)
    # Input for choosing the menu
    choice = input("What path shall thoust choose?\n")
    # Loop that checks if the user enter an invalid input
    for key in menuName:
        while str(choice) not in choices:
            print(f"I got, {str(choices)[1:-1]} watchu want?")
            choice = input("")
            # Repeats inpyt for choosing the menu
            for key in menuName:
                if choice == key:
                    # Prints out users choice
                    print(f"You have chose Path {key}")
# Dictionary containing the first start path
startPath = {
    "1": "A level 1 mob appears",
    "2": """You find yourself in a room, you have a choice to go left or
    right""",
    "3": "You are in a forest."
}
print("Welcome to Mazy Boi")
# Prints out startPath's text based menu system
menuSample(startPath)
