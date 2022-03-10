import os
from art import logo


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def find_winning_bid(bidding_list):
    winning_bid = ["", 0]
    for name in bidding_list:
        bid_amount = bidding_list[name]
        if bid_amount > winning_bid[1]:
            winning_bid[1] = bid_amount
            winning_bid[0] = name
    print(f"The winner of the auction is {winning_bid[0]} with a bid of ${winning_bid[1]}")


clearConsole()
print(logo)
print('Welcome to the secret auction program.')
bidding = True
all_bids = {}

while bidding:
    users_name = input("What is your name?: ")
    current_bid = int(input("What is your bid?: $"))
    all_bids[users_name] = current_bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if continue_bidding == 'no':
        bidding = False
    clearConsole()

find_winning_bid(all_bids)
