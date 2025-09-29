# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
names_list = []
prices_list = []
bidders = {}


 #3) If I want to add a new bid
def add_a_new_bidder():

    while True:
             
        add_new_bid = input("Do you want to add a new bid? Type 'yes' or 'no'""\n").lower()

        if add_new_bid == "yes":
            save_input_to_dictionary()

        elif add_new_bid == "no":
            winner()
            break

        else:
            print("You typed the incorrect option, type 'yes' or 'no'\n")
            continue



# 4) determine the winner
def winner():
    highest_price = max(prices_list)

    for price in prices_list:
        if price == highest_price:
            print(f"The winner is : {price}")


#1 and #2

def save_input_to_dictionary():
    name = input("What is your name?\n")
    names_list.append(name)
            #1.1) Add a user input
            #I wanted it to loop at the wrong option until you exit how can I achieve that?
    price = float(input("How much are you bidding?\n"))

    prices_list.append(price)

    # Match price and name 
    for index in range(len(names_list)): #create an index of the names list (researched this option)
        bidders[names_list[index]] = prices_list[index] # Match the names list to the price list and save in dictionary

            # Update the bidders dictionary
    bidders[name] = price
    print(bidders)







def main():
    print(logo)
    print("Hello, let the highest bidder win")
    save_input_to_dictionary()
    add_a_new_bidder()
    
    

main()
