import sys
import random
import string

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
update_characters_left(lowercase_letters)
#
uppercase_letters = int(input("ile dużych liter ma miec hasło? "))
update_characters_left(uppercase_letters)

special_characters = int(input("ile znaków specjalnych ma miec hasło? "))
update_characters_left(special_characters)

digits = int(input("ile cyfr ma miec hasło? "))
update_characters_left(digits)
# This is a sample Python script.
if characters_left > 0:
    print('nie wzystkie znaki zostały wyświtlone')
    lowercase_letters += characters_left

print()
print('długośc hasła:', password_lenght)
print('małe litery:', lowercase_letters)
print("duże litery:", uppercase_letters)
print('znaki specjalne:', special_characters)
print('cyfry:', digits)

for i in range(password_lenght):
    if lowercase_letters > 0:
       password.append(random.choice(string.ascii_lowercase))
       lowercase_letters -= 1
    if uppercase_letters > 0:
       password.append(random.choice(string.ascii_uppercase))
       uppercase_letters -= 1
    if special_characters > 0:
       password.append(random.choice(string.punctuation))
       special_characters -= 1
    if digits > 0:
       password.append(random.choice(string.digits))
       digits -= 1

random.shuffle(password)
print('wygenerowane hasło:', ''.join(password))

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sett
