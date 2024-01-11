import sys

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print(' liczba znaków spoza przedziału 0,', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print('pozostało znaków:', characters_left)
password_lenght = int(input('jak długie ma być hasło? '))

if password_lenght < 5:
    print('hasło musi mieć minmum 5 znaków, spróbuj jeszcze raz')
    sys.exit(0)
else:
    characters_left = password_lenght
    # print('pozostało znaków:', characters_left)

lowercase_letters = int(input("ile małych liter ma miec hasło? "))
# if lowercase_letters > characters_left:
#     print('liczba znaków przekracza liczbę wolnych znakow')
#     sys.exit(0)
update_characters_left(lowercase_letters)

uppercase_letters = int(input("ile dużych liter ma miec hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("ile znaków specjalnych ma miec hasło? "))
update_characters_left(special_characters)

digits = int(input("ile cyfr ma miec hasło? "))
update_characters_left(digits)
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sett
