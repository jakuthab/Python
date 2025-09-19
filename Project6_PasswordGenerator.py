import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# Add letters
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add symbols
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(password_list)

# Convert the list to a string
password = ''.join(password_list)
print(f"Your password is: {password}")


# Project Description: I created a Python Password Generator that creates secure, randomized passwords based on user specifications. The program asks users how many letters, symbols, and numbers they want in their password and generates a random combination of these characters.

# What I Learned:

# List Manipulation:
# I learned how to work with multiple lists (letters, numbers, and symbols)
# I gained experience in appending elements to lists using password_list.append()
# I understood how to convert a list to a string using the join() method
# Random Module:
# I learned to use random.choice() to select random elements from lists
# I discovered random.shuffle() to randomize the order of elements in a list
# I understood the importance of randomization in creating secure passwords
# For Loops:
# I implemented for loops with range() to control the number of characters added
# I learned how to iterate through specific ranges to add the desired number of each character type
# User Input:
# I practiced getting user input using input()
# I learned to convert string inputs to integers using int()
# I implemented f-strings for clearer user prompts
# String Manipulation:
# I learned about string concatenation using join()
# I understood how to combine different character types into a single password string
# Type Annotations:
# I was introduced to the typing module and how to use type hints
# I learned about the @final decorator (though not directly used in the main code)
# This project helped me understand how to combine various Python concepts to create a practical application. It also taught me about the importance of randomization in security-related applications and how to create user-friendly interfaces through proper input handling and output formatting.

# The concepts I incorporated demonstrate a good foundation in Python programming, from basic data structures to more advanced concepts like random number generation and type hinting.


