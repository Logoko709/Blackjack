########################################################################
#||        This File is for the Account Management like the Chips     ||
########################################################################

# Import needed Packages
import os
import shutil
import time
import re

# Makes the Variable to place Text in the middle of the Screen
columns = shutil.get_terminal_size().columns

# Clear the terminal
def clear():
    print("\n" * 30)
    os.system("cls")

def remove_special_characters(string):
    return re.sub(r"[^a-zA-Z0-9]+", "", string)

# Login System
def login():
    global username
    global file_path
    global win_value
    global loose_value

    makingNewAccount = True

    # Gets your username
    while makingNewAccount:
        username = input("\n\n\nenter your username (special letters will be removed): ")
        username = remove_special_characters(username)
        if len(username) < 3:
            print("The Username has to be more then the minimum of 3 letters")
        else:
            break
    file_path = ("User/" + username + "/" + "chips.txt")
    win_value = 0
    loose_value = 0
    # If it is a new username it makes a new Account with 1000 Chips but if it already exists it will log you in
    if not os.path.exists(file_path):
        newPasswort = True
        while newPasswort:
            # Asks for a new Password for the new Account
            passwort = input("\n\n\nMake a new password: ")
            passwortenter = input("\n\n\nConfirm your password: ")
            if len(passwort) < 1 or passwort != passwortenter:
                if len(passwort) < 1:
                    print("\nYour password has to have a minimum of 1 letter!")
                if  passwort != passwortenter:
                    print("Passwords don't match please try again!")
            else:
                newPasswort = False
        # Makes the new File
        os.mkdir("User/" + username)

        with open(file_path, "w") as file:
            file.write("1000")
        with open("User/" + username + "/" + "passwort.txt", "w") as file:
            file.write(passwort)
        print(f"The User {username} has been created.")
    else:
        running = True
        tries = 3
        while running:
            with open("User/" + username + "/" + "passwort.txt", "r") as file:
                correctPassword = file.read()
            confirmPasswort = input("\nPassword: ")
            if confirmPasswort == correctPassword:
                print(f"Logged {username} in!")
                running = False
            else:
                print("Wrong Password!", tries, "left!")
                tries -= 1
                if tries == -1:
                    print("Goodbay")
                    time.sleep(2)
                    os.system("taskkill /PID Blackjack.exe /F")






# Bet for the game
def bet():
    global bet_value
    global new_chip_value
    global chip_value
    # Reads how many Chips you got
    user = open("User/" + username + "/" + "chips.txt", "r")
    chip_value = int(user.read())
    print("You have now", chip_value, "Chips")
    betting = True

    while betting:
        try:
            # Asking you how much you would like to bet
            bet_value = int(input("How much do you want to bet (1-100000): "))
        except ValueError:
            print("This is not a number try again!")
            continue
        # Checks if you got enough chips for your bet and if it's in the minimum and maximum range
        if bet_value >= 1 and bet_value <= 1000000 and chip_value >= bet_value:
            print("Are you sure you want to bet", bet_value, "Yes or No?(Y or N)")
            try:
                finalbet = input(" ")
            except ValueError:
                print("This is not a option try again!")
                continue
            if finalbet.upper() == "Y" or "Yes":
                chip_value = chip_value - bet_value
                betting = False
            else:
                print("No? Okay bet again")
        elif bet_value > 1000000:
            print("Your bet is too high (MAX. 1000000")

        elif bet_value < 1:
            print("Your bet is too low (MIN. 1)")

        elif chip_value <= bet_value:
            print("You are broke, you dont got enough Money💀")

        else:
            print("Error")
    update()

# Handles winning logic.
def win():
    global win_value
    win_value = (2 * bet_value)
    print("You won", bet_value, "Chips")
    return win_value

# Handles Tie logic.
def tie():
    global win_value
    win_value = bet_value
    print("You get", bet_value, "Chips back")
    return win_value

# Updates user's chip count.
def update():
    new_chip_value = chip_value + win_value - loose_value
    user = open(file_path, "w")
    user.write(str(new_chip_value))
    print("You have", new_chip_value, "Chips")

# Updates the bet Chips if double
def double():
    global chip_value
    global bet_value
    chip_value = chip_value - bet_value
    bet_value = bet_value * 2
    update()
    return bet_value

# Placeholder function for debugging.
def end():
    breakpoint()


def chipMenu(value):
    new_chip_value = value
    user = open(file_path, "w")
    user.write(str(new_chip_value))
    print("You have", new_chip_value, "Chips")


