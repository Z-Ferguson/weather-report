from collections import OrderedDict
import os


class Menu:

    def __init__(self, welcome_msg=0):
        self.welcome_msg = welcome_msg
        self.menu_option = OrderedDict()

    def register(self, title, function):
        self.menu_option[title] = function

    def display(self):
        clear()
        if self.welcome_msg:
            print("\n" + self.welcome_msg)
        while True:
            for index, option in enumerate(self.menu_option):
                print("{} {} ".format(index+1, option))
            ui = input(
            "\nWhat do you want to do? Enter a number next to the option:\n>")
            for index, option in enumerate(self.menu_option):
                if str(index+1) == ui:
                    clear()
                    self.menu_option[option]()


def test():
    # New feature testing area
    pass


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == "__main__":
    test()
