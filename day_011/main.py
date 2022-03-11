############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card():
    return random.randint(0, len(cards) - 1)


def print_cards(hand):
    hand_as_string = ""
    for index, card in enumerate(hand):
        if index == len(hand) - 1:
            hand_as_string += str(card)
        else:
            hand_as_string += str(card) + ", "
    return hand_as_string


def get_score(hand):
    score = 0
    for card in hand:
        score += card

    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score -= 10
    return score


def check_winner(user, computer):
    if user > 21:
        return "Bust, you lose.  Better luck another time!"
    if computer > 21:
        return "Dealer busts, you win!  Congratulations!"
    if user == computer:
        return "Draw."
    if user == 21:
        return "BLACKJACK!  Congrats!  You win!"
    if computer == 21:
        return "Dealer has BLACKJACK.  Sorry, you lose!  Maybe next time!"
    if user > computer:
        return "Congrats!  You win!"
    if user < computer:
        return "You lose.  Better luck next time!"


def blackjack():
    print(logo)
    users_cards = [cards[get_card()], cards[get_card()]]
    computers_cards = [cards[get_card()], cards[get_card()]]

    is_completed = False
    while not is_completed:
        users_score = get_score(users_cards)
        users_cards_string = print_cards(users_cards)

        print(f"Your cards: [{users_cards_string}], current score: {users_score}")
        print(f"Dealer's first card: {computers_cards[0]}")

        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'n':
            is_completed = True
        else:
            users_cards.append(cards[get_card()])
            if get_score(users_cards) > 21:
                is_completed = True

    users_final_score = get_score(users_cards)
    users_final_cards = print_cards(users_cards)

    computer_drawing = True
    # If the user busts, do not draw cards
    if users_final_score > 21:
        computer_drawing = False
    while computer_drawing:
        computers_score = get_score(computers_cards)
        if computers_score < random.randint(14, 17):
            computers_cards.append(cards[get_card()])
        else:
            computer_drawing = False
    computers_score = get_score(computers_cards)
    computers_cards_string = print_cards(computers_cards)

    print(f"Your final hand: [{users_final_cards}], final score: {users_final_score}")
    print(f"Dealer's final hand: [{computers_cards_string}], final score: {computers_score}")

    print(check_winner(users_final_score, computers_score))


playing = True
while playing:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        blackjack()
    else:
        playing = False
