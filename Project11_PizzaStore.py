print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
valid_order = True

# Size validation and pricing
if size.lower() in ["s", "m", "l"]:
    if size.lower() == "s":
        bill += 15
    elif size.lower() == "m":
        bill += 20
    else:  # size.lower() == "l"
        bill += 25
else:
    valid_order = False
    print("Invalid pizza size! Please choose S, M, or L.")

# Pepperoni validation and pricing
if pepperoni.lower() in ["y", "n"]:
    if pepperoni.lower() == "y":
        if size.lower() == "s":
            bill += 2
        else:
            bill += 3
else:
    valid_order = False
    print("Invalid pepperoni option! Please choose Y or N.")

# Extra cheese validation and pricing
if extra_cheese.lower() in ["y", "n"]:
    if extra_cheese.lower() == "y":
        bill += 1
else:
    valid_order = False
    print("Invalid extra cheese option! Please choose Y or N.")

# Final bill output
if valid_order:
    print(f"Your final bill is: ${bill}.")
else:
    print("Please try again with valid options.")


# Here's what I learned from this Pizza Order code:

# Input Handling:

# Using input() function to get user responses
# Converting inputs to be case-insensitive using .lower()
# Conditional Statements:

# Using if, elif, and else for decision making
# Nested if statements for more complex conditions
# Using logical operators for input validation
# Variables:

# Creating and updating variables (bill = 0)
# Using a flag variable (valid_order) to track program state
# String Formatting:

# Using f-strings to display the final bill (f"Your final bill is: ${bill}.")
# Basic Math:

# Using += operator for adding to the bill amount
# User Experience:

# Implementing error messages for invalid inputs
# Creating a clear pricing structure
# This code helped me understand how to build a simple order system and handle user inputs effectively in Python.


