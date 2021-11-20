# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from machine.Text import Text


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    machine = Text()
    machine.display_items()
    selected_item = input("Please pick an item: ")

    machine.select_item(int(selected_item))
    machine.display_message(message="")

    entered_coins = input("Please enter your coins: ")

    coins_list = entered_coins.split(',') # parse entered coins eg: 1,2,0,0
    entered_coins = [int(value) for value in coins_list]

    machine.enter_coins(entered_coins)
    machine.display_change_message("")

if __name__ == '__main__':
    print_hi('Freightos')
