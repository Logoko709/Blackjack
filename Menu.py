import keyboard
import time


print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n▌                ▌\n▌ BBC BLACKJACK  ▌\n▌                ▌\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

selected = 1

def show_menu():
    global selected
    print("\n" * 35)
    print("-----Choose an option:------ (f1 for help)")
    for i in range(1):
        i += 1
        print("{1} {0}. Login and Play {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Settings {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Help {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
        print("{1} {0}. Credits {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))
        i += 1
    return selected
def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()
    return selected

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    show_menu()
    return selected

def escape():
    show_menu()

def helpMenu():
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. In The Menu you can move up and down with arrows. If you want to Enter a Menu you have to press the right arrow and if you want to exit again just press the escape key. \n2. In the Game you have to press Enter to continue and get the next Card. \n3. If you have no money left and you already have much dept and cause that you want to restart and delete your Account then just go in to the User directory and delete the txt file with your username.")




show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('right', enter)
keyboard.add_hotkey('esc', escape)
keyboard.add_hotkey('f1', helpMenu)
keyboard.wait()
