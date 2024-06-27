import random
from AccountManager import *
import os
import shutil

columns = shutil.get_terminal_size().columns

selected = 1

# The Card class definition
class Card:
    def __init__(self, suit, value, card_value):
        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing Value of the Card like A for Ace, K for King
        self.value = value

        # Score Value for the Card like 10 for King
        self.card_value = card_value


# Function to print the cards
def print_cards(cards, hidden):
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()

# Clear the terminal
def clear():
    print("\n" * 30)
    os.system("cls")


clear()

# Function for a single game of blackjack
def blackjack_game(deck):
    global split
    global first_Card
    game = True
    while game:

        # Cards for both dealer and player
        player_cards = []
        dealer_cards = []

        # Scores for both dealer and player
        player_score = 0
        dealer_score = 0
        cards_played = 0

        clear()
        # Initial dealing for player and dealer
        while len(player_cards) < 2:

            cards_played += 1

            # Randomly dealing a card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)



            # Updating the player score
            player_score += player_card.card_value

            # In case both the cards are Ace, make the first ace value as 1
            if len(player_cards) == 2:
                if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                    player_cards[0].card_value = 1
                    player_score -= 10

            # Print player cards and score
            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)

            input()

            # Randomly dealing a card
            dealer_card = random.choice(deck)
            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            # Updating the dealer score
            dealer_score += dealer_card.card_value


            # Print dealer cards and score, keeping in mind to hide the second card and score
            print("DEALER CARDS: ")
            if len(dealer_cards) == 1:
                print_cards(dealer_cards, False)
                print("DEALER SCORE = ", dealer_score)
            else:
                print_cards(dealer_cards[:-1], True)
                print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

            # In case both the cards are Ace, make the second ace value as 1
            if len(dealer_cards) == 2:
                if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                    dealer_cards[1].card_value = 1
                    dealer_score -= 10

            input()

        # Player gets a blackjack
        if player_score == 21:
            print("PLAYER HAS A BLACKJACK!!!!")
            print("PLAYER WINS!!!!")
            win()
            update()
            break

        clear()

        # Print dealer and player cards
        print("DEALER CARDS: ")
        print_cards(dealer_cards[:-1], True)
        print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

        print()

        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        # Managing the player moves
        while player_score < 21:

            choice = input("Enter H to Hit or S to Stand or D for Double: ")

            # Sanity checks for player's choice
            if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
                clear()
                print("Wrong choice!! Try Again")

            # If player decides to HIT
            if choice.upper() == 'H':

                # Dealing a new card to Player
                player_card = random.choice(deck)
                player_cards.append(player_card)
                deck.remove(player_card)

                # Updating player score
                player_score += player_card.card_value

                # Updating player score in case player's card have ace in them
                c = 0
                while player_score > 21 and c < len(player_cards):
                    if player_cards[c].card_value == 11:
                        player_cards[c].card_value = 1
                        player_score -= 10
                        c += 1
                    else:
                        c += 1

                clear()

                # Print player and dealer cards
                print("DEALER CARDS: ")
                print_cards(dealer_cards[:-1], True)
                print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

                print()

                print("PLAYER CARDS: ")
                print_cards(player_cards, False)
                print("PLAYER SCORE = ", player_score)

            # If Player decides to Double
            if choice.upper() == 'D':
                double()

                # Dealing a new card to Player
                player_card = random.choice(deck)
                player_cards.append(player_card)
                deck.remove(player_card)

                # Updating player score
                player_score += player_card.card_value

                # Updating player score in case player's card have ace in them
                c = 0
                while player_score > 21 and c < len(player_cards):
                    if player_cards[c].card_value == 11:
                        player_cards[c].card_value = 1
                        player_score -= 10
                        c += 1
                    else:
                        c += 1

                clear()

                # Print player and dealer cards
                print("DEALER CARDS: ")
                print_cards(dealer_cards[:-1], True)
                print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

                print()

                print("PLAYER CARDS: ")
                print_cards(player_cards, False)
                print("PLAYER SCORE = ", player_score)

                print()

                break

            # If player decides to Stand
            if choice.upper() == 'S':
                break

        clear()

        # Print player and dealer cards
        print("DEALER CARDS: ")
        print_cards(dealer_cards[:-1], True)
        print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

        print()

        clear()

        # Print player and dealer cards
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        print()
        print("DEALER IS REVEALING THE CARDS....")

        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)

        # Check if player has a Blackjack
        if player_score == 21:
            print("PLAYER HAS A BLACKJACK")
            win()
            update()
            break

        # Check if player busts
        if player_score > 21:
            print("PLAYER BUSTED!!! GAME OVER!!!")
            break

        input()

        # Managing the dealer moves
        while dealer_score < 17:
            clear()

            print("DEALER DECIDES TO HIT.....")

            # Dealing card for dealer
            dealer_card = random.choice(deck)

            dealer_cards.append(dealer_card)
            deck.remove(dealer_card)

            # Updating the dealer's score
            dealer_score += dealer_card.card_value

            # Updating dealer score in case dealer's card have ace in them
            c = 0
            while dealer_score > 21 and c < len(dealer_cards):
                if dealer_cards[c].card_value == 11:
                    dealer_cards[c].card_value = 1
                    dealer_score -= 10
                    c += 1
                else:
                    c += 1

            # print player and dealer cards
            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)

            print()

            print("DEALER CARDS: ")
            print_cards(dealer_cards, False)
            print("DEALER SCORE = ", dealer_score)

            input()

            print()

            # Check if player has a Blackjack
            if player_score == 21:
                print("PLAYER HAS A BLACKJACK")
                win()
                update()
                break

            # Check if player busts
            if player_score > 21:
                print("PLAYER BUSTED!!! GAME OVER!!!")
                break

        # Dealer busts
        if dealer_score > 21:
            print("DEALER BUSTED!!! YOU WIN!!!")
            win()
            update()
            break

            # Dealer gets a blackjack
        if dealer_score == 21:
            print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
            update()
            break

        # TIE Game
        if dealer_score == player_score:
            print("TIE GAME!!!!")
            tie()
            update()
            break

        # Player Wins
        elif player_score > dealer_score:
            print("PLAYER WINS!!!")
            win()
            update()
            break

            # Dealer Wins
        else:
            print("DEALER WINS!!!")
            update()
            break
    playAgain()


if __name__ == '__main__':

    # Type of the card
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # Value of the suit
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

    # Type of the cards
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                    "K": 10}

    # The deck of cards
    deck = []

    for i in range(6):
    # Loop for every type of suit
        for suit in suits:

            # Loop for every type of card in a suit
            for card in cards:
                # Adding card to the deck
                deck.append(Card(suits_values[suit], card, cards_values[card]))


getChips = False

# Makes the Scroll animation for example in the starting scene
def scroll():
    for i in range(12):
        global columns
        columns = shutil.get_terminal_size().columns
        print("\n")
        time.sleep(0.4)

# Makes the Scroll animation for example in the starting scene just fast
def scrollfast():
    for i in range(25):
        global columns
        columns = shutil.get_terminal_size().columns
        print("\n")
        time.sleep(0.1)

import keyboard
import time

scrollfast()

# Prints the Intro
print("██████╗ ██████╗  ██████╗    ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗".center(columns))
print("██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝".center(columns))
print("██████╔╝██████╔╝██║         ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ ".center(columns))
print("██╔══██╗██╔══██╗██║         ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ ".center(columns))
print("██████╔╝██████╔╝╚██████╗    ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗".center(columns))
print("╚═════╝ ╚═════╝  ╚═════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝".center(columns))

for i in range(22):
    time.sleep(0.4)
    print("\n")

columns = shutil.get_terminal_size().columns


selected = 1
# Shows the menu where you can choose what to do
def show_menu():
    global selected
    clear()
    print("\n\n\n\n\n\n\n\n")
    print("-----Choose an option:------ (f1 for help)".center(columns))
    for i in range(1):
        i += 1
        print("{1} {0}. Login and Play {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Help {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Credits {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Get Chips {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Quit {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
    return selected

def show_menu2():
    global selected
    clear()
    print("\n\n\n\n\n\n\n\n")
    print("-----Choose an option:------ (f1 for help)".center(columns))
    for i in range(1):
        i += 1
        print("{1} {0}. 100 {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. 500 {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. 1000 {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. 2000 {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. 1 {0} {2}".center(columns).format(i, ">" if selected == i else " ", "<" if selected == i else " "))
    return selected
# Makes the select go up
def up():
    global columns
    global selected
    columns = shutil.get_terminal_size().columns
    if selected == 1:
        return
    selected -= 1
    if getChips == False:
        show_menu()
    else:
        show_menu2()
    return selected

# Makes the select go down
def down():
    global columns
    global selected
    columns = shutil.get_terminal_size().columns
    if selected == 5:
        return
    selected += 1
    if getChips == False:
        show_menu()
    else:
        show_menu2()
    return selected

# Makes you go back to the menu
def escape():
    global getChips
    getChips = False
    show_menu()
    return getChips
# Shows the help menu
def helpMenu():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. In The Menu you can move up and down with arrows. If you want to Enter a Menu you have to press the right arrow and if you want to exit again just press the escape key. \n2. In the Game you have to press Enter to continue and get the next Card. \n3. If you have no chips left, go to the get chips option. This is cheating so use it only if you have no Chips left.")

# Goes into the selected menu part
def enter():
    global getChips
    # Makes the login and starts the Blackjack game
    if selected == 1:
        if getChips == False:
            from AccountManager import login
            login()
            from AccountManager import bet
            bet()
            time.sleep(1)
            blackjack_game(deck)
        else:
            from AccountManager import chipMenu
            chipMenu(100)
    # Prints the helplist
    elif selected == 2:
        if getChips == False:
            print("\n\n\n1. In The Menu you can move up and down with arrows. If you want to Enter a Menu you have to press the right arrow and if you want to exit again just press the escape key. \n2. In the Game you have to press Enter to continue and get the next Card. \n3. If you have no Chips left you can go to the get Chips option and get Chips there. please only use it if you are out of Chips cause its Cheating.".center(columns))
        else:
            from AccountManager import chipMenu
            chipMenu(500)
    # Shows the credits
    elif selected == 3:
        if getChips == False:
            scrollfast()
            print(" ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗   ".center(columns))
            print("██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝██╗".center(columns))
            print("██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗╚═╝".center(columns))
            print("██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║██╗".center(columns))
            print("╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║╚═╝".center(columns))
            print(" ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝   ".center(columns))
            scroll()
            print("GAME DEVELOPMENT: LOUIS".center(columns))
            scroll()
            print("MENTAL SUPPORT: JÖREM".center(columns))
            scroll()
            print("SUPPORT AT DEVELOPING: ANDY & JUSTIN & LEON & MITJA & NOAH & JÖREM".center(columns))
            scroll()
            print("MOST MENTAL DAMAGES: JÖREM & BASTIAN".center(columns))
            scroll()
            print("IDEAS: FROM THE INTERNET AND MY BRAIN".center(columns))
            scroll()
            print("BEST FOOTBALLER: BASTI".center(columns))
            scroll()
            print("Thank you all for the support for my beautiful Project!!!<3.".center(columns))
            print("(press esc to Menu)".center(columns))
        else:
            from AccountManager import chipMenu
            chipMenu(1000)
    # Stops the Programm
    elif selected == 4:
        if getChips == False:
            getChips = True
            from AccountManager import login
            login()
            show_menu2()
            return getChips
        else:
            from AccountManager import chipMenu
            chipMenu(2000)
    elif selected == 5:
        if getChips == False:
            os.system("taskkill /PID Blackjack.exe /F")
        else:
            from AccountManager import chipMenu
            chipMenu(1)

# Function to play again or to go back to the Menu
def playAgain():
    while True:
        gameSet = input("Play again (A) or stop playing (S): ")
        if len(gameSet) != 1 or (gameSet.upper() != 'A' and gameSet.upper() != 'S'):
            clear()
            print("Wrong choice!! Try Again")
        if gameSet.upper() == "A":
            bet()
            blackjack_game(deck)
        elif gameSet.upper() == "S":
            decision = input("Are you sure you want to go back to the menu?(Yes or No): ")
            if decision.upper() == "YES":
                show_menu()
                break
            elif decision.upper() == "NO":
                pass
            else:
                input("This is not a valid Answer")

# For the Keybinds in the Menu
show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', enter)
keyboard.add_hotkey('esc', escape)
keyboard.add_hotkey('f1', helpMenu)
keyboard.wait()


