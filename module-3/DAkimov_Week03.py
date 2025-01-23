"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Notice: If you roll a 2 or a 7, you get a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('DA. mss: ')  # Change input prompt to your initials.
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You cannot bet more than what you have.')
        else:
            pot = int(pot)
            break

    # Roll the dice:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')
    bet = input('mss: ').upper()

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    roll_total = dice1 + dice2

    # Check for bonus:
    if roll_total == 2 or roll_total == 7:
        print(f'You rolled a {roll_total}! You get a 10 mon bonus!')
        purse += 10

    # Determine if it is even or odd:
    if roll_total % 2 == 0:
        correct_bet = 'CHO'
    else:
        correct_bet = 'HAN'

    # Did the player win?
    if bet == correct_bet:
        print('You won! You take', pot, 'mon.')
        purse += pot  # Add the pot from player's purse.
        # Subtract house's cut:
        purse -= int(pot * 0.12)
        print('The house takes 12 percent, so you now have', purse, 'mon.')
    else:
        print('You lost!')
        purse -= pot  # Subtract the pot from player's purse.

    # Check if the player is out of money:
    if purse == 0:
        print('You are out of money!')
        print('Thanks for playing!')
        sys.exit()