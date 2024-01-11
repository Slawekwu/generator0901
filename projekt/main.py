1from math import sqrt
from random import randint

GAME_WIDTH = 10
GAME_HEIGH = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGH)
player_x = 0
player_y = 0
player_found_key = False
steps = 0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
print(key_x, key_y)

while not player_found_key:
    steps += 1
    print()
    print('możesz udać się w kierunkach określonych jako [W/A/S/D]: ')
    print(player_x, player_y)

    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    print(distance_after_move)

    move = input('dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGH:
                print('Auć! Uderzasz w ścianę!!!')
                player_y = GAME_HEIGH

        case 's':
            player_y -= 1
            if player_y < 0:
                print('Auć! Uderzasz w ścianę!!!')
                player_y = 0

        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Auć! Uderzasz w ścianę!!!')
                player_x = 0

        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print('Auć! Uderzasz w ścianę!!!')
                player_x = GAME_WIDTH

        case 'q':
            print('koniec gry!')
            quit()

        case default:
            print('nie wiem dokąd idziesz..')
            continue

    if distance_before_move < distance_after_move:
        print('zimniej')
    else:
        print('cieplej')
        distance_before_move = distance_after_move

        print(player_x, player_y)
    if player_x == key_x and player_y == key_y:
        print('klucz jest twój!')
        print(f'potrzebowałeś {steps} ruchów.')
        quit()
distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)