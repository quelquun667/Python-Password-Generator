import random
import string
import os
clear = lambda: os.system('cls')
import time
term_size = os.get_terminal_size()
from colorama import Fore, Back, Style

def main():
    
    clear()
    print(Style.RESET_ALL)

    name = """
    ____                                     _    ____                           _             
    |  _ \ __ _ ___ _____      _____  _ __ __| |  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
    (for exit press ctrl + c TWICE)
    """

    print("="*term_size.columns)
    print(name.center(term_size.columns))
    print("="*term_size.columns)
    try:
        lenght = int(input("Password length : "))
    except:
        print("You must enter an integer number")
        time.sleep(1)
        print("Program Restarting.")
        time.sleep(0.5)
        print("Program Restarting..")
        time.sleep(0.5)
        clear()
        main()
    if lenght > 64:
        print("too long")
        anwser = input("Do you want restart program ? [y/n] ")
        if anwser == "y":
            print("Program Restarting.")
            time.sleep(1)
            print("Program Restarting..")
            time.sleep(1)
            clear()
            main()
        elif anwser == "n":
            print("Program Closing..")
            exit(0)
        else:
            print("Wrong anwser")
            print("Program Closing..")
            exit(0)

    str_char = string.ascii_letters + string.digits + "!@#$^&*"

    result = ''

    for _ in range(lenght):
        char = random.choice(str_char)
        if char.isalpha():
            result += Style.RESET_ALL + char
        elif char.isnumeric():
            result += Fore.BLUE + char
        else:
            result += Fore.RED + char

    print(result)
    print(Style.RESET_ALL + "Lenght = ", lenght)
main()