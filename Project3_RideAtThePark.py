ageheight = True

def age_and_height(): #practicing functions
    while  ageheight == True:
        print("Welcome to the rollercoaster!")
        height = int(input("What is your height in cm? "))
        age = int(input("How old are you: "))

        if height <120 or age <12:
            print("You cannot ride")

        else:
            print("You are allowed ride")

            if age <= 12:
                print("Your ride is R5")

            if age > 12:
                if age <= 18:
                    print("Your ride is R7")
                else:
                    if age >= 18:
                        print("Your ride is R12")

    
age_and_height()
