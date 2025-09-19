
Project3_RideAtThePark.py

# Rollercoaster Ride Eligibility Checker

This Python program checks if a user is allowed to ride a rollercoaster based on their height and age, and calculates the ride price accordingly.

## How It Works

- The program welcomes the user to the rollercoaster.
- It asks for the user's height in centimeters and age.
- If the height is less than 120 cm **or** age is less than 12, the user is not allowed to ride.
- Otherwise, the user is allowed to ride and the program outputs the ticket price based on age:
  - Age 12 or younger: Ride costs R5
  - Age between 13 and 18: Ride costs R7
  - Age 19 or older: Ride costs R12

## Code Breakdown

- The main function is `age_and_height()`.
- It uses a `while` loop controlled by the `ageheight` flag (currently set to `True`).
- Takes height and age as inputs from the user.
- Applies conditional checks for eligibility and pricing.
- Prints the appropriate messages and price.

## How to Run

Run the script in your Python environment. It will prompt you for inputs and display the results based on the rules above.
