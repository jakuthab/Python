treasure_not_found = True

while treasure_not_found:
    print(r'''
    *******************************************************************************
     ,adPPYb,d8 88       88  ,adPPYba,  ,adPPYba, 8b,dPPYba,   
    a8"    `Y88 88       88 a8P_____88 a8P_____88 88P'   `"8a  
    8b       88 88       88 8PP""""""" 8PP""""""" 88       88  
    "8a    ,d88 "8a,   ,a88 "8b,   ,aa "8b,   ,aa 88       88  
     `"YbbdP'88  `"YbbdP'Y8  `"Ybbd8"'  `"Ybbd8"' 88       88  
             88                                                
             88                                                
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    direction = input("Do you want to go left or right? Type left or right\n")
    if direction == "right" or direction!="left":
        print("Fall into a whole Game over")

    elif direction == "left":
        print("You've come to the lake. There is an island in the middle of the lake")
        swim = input("Do you want to swim or wait? Type swim or wait\n")
        if swim == "swim" or swim != "wait":
            print("Attached by trout.Game Over")

        elif swim =="wait":
            print("You've arrived at the island unharmed. There is a house with 3 doors")
            door = input("Which door do you want to enter? Type red, blue or yellow\n")
            if door == "red":
                print("You got burnt by fire. Game Over :(")
            elif door == "blue":
                print("You got eaten by beasts.Game over :(")
            elif door == "yellow":
                print("I always knew you'd win! you found the treasure! You win!")
            else:
                print("Game over")
                break


# Here's what I learned from creating the Treasure Island game:

# What I Learned:

# While Loop Implementation:
# I used a while loop with a boolean flag (treasure_not_found) to control game flow
# I learned how to create continuous game play until specific conditions are met
# ASCII Art:
# I implemented multi-line string art using r''' (raw string)
# I learned to create visually appealing game interfaces
# Nested Conditional Statements:
# I created complex game logic using nested if-elif-else statements
# I implemented multiple decision paths based on user choices
# User Input Handling:
# I practiced getting and validating text-based user inputs
# I learned to handle different case scenarios for user responses
# Game Flow Control:
# I used the break statement to exit the game loop
# I implemented multiple decision points with different outcomes
# String Comparison:
# I learned to compare user input strings for decision making
# I implemented OR conditions for handling invalid inputs
# This project helped me understand how to create an interactive text-based adventure game while practicing fundamental Python concepts like loops, conditionals, and user input handling. I also learned about creating engaging user experiences through story-based programming.



