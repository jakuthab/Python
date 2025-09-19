#Rock,Paper, Scissors Game
rock = ''' rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choose = [rock,paper,scissors]
#User selection based on choice
user_selection = int(input("Choose 0,1 or 2\n"))


# What to do based on user selection
if user_selection == 0:
    print(f"You chose:{choose[0]}")

elif user_selection == 1:
    print(f"You chose:{choose[1]}")

elif user_selection == 2:
    print(f"You chose:{choose[2]}")

#Computer automated choice based on randomization

computer_choice = int(random.randint(0, 2))

# Assign random computer_choice to choose variable I can compare the
if user_selection<0 or user_selection>2:
    print("You've selected an invalid number - try again and pick 0,1 or 2")

elif computer_choice==0:
    print(f"AI choose:{choose[0]}")

elif computer_choice==1:
    print(f"AI choose:{choose[1]}")

elif computer_choice==2:
    print(f"AI choose:{choose[2]}")


#Rules - Check for Winner#
#1. User:RockVsCom:scissors
#2. User:scissorsVsCom:paper
#3.User:PaperVsCom:Rock
if user_selection<0 or user_selection>2:
    print("You've selected an invalid number - try again and pick 0,1 or 2")

elif user_selection==0 and computer_choice==2:
    print("You win!")

elif user_selection>computer_choice:
    print("You win!")

elif user_selection < computer_choice:
    print("You Loose to AI!")

elif user_selection == computer_choice:
    print("Its a draw no ones wins! Play again! ")



# Here's what I learned from creating the Rock, Paper, Scissors game:

# What I Learned:

# ASCII Art Implementation:
# I learned how to use multi-line strings (''') to create visual game elements
# I understood how to store and display ASCII art in variables
# List Operations:
# I practiced using lists to store game choices (rock, paper, scissors)
# I learned to access list elements using index positions
# Random Module:
# I implemented random.randint() to generate computer choices
# I understood how to create randomized game decisions
# Conditional Logic:
# I developed complex if-elif statements for game rules
# I implemented game logic for winning, losing, and draw conditions
# I learned to handle invalid user inputs
# User Input Handling:
# I practiced getting and validating user input
# I converted string inputs to integers using int()
# F-strings:
# I used f-strings for formatted output of game choices
# I learned to combine variables with strings for clear user feedback
# This project helped me understand how to create an interactive game while implementing fundamental Python concepts like conditionals, user input, and randomization. I also learned the importance of input validation and clear user feedback in creating a user-friendly game experience.


