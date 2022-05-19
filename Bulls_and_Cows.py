"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ladislav Bure3
email: ladislavb01@gmail.com
discord: Láďa#7333
"""

# Program pozdraví užitele a vypíše úvodní text
# Program dále vytvoří tajné 4 místné číslo (číslice musí být unikátní a nesmí začínat 0)
# Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity,
# začínat nulou, příp. obsahovat nečíselné znaky
# Program vyhodnotí tip uživatele
# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
# příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). Vrácené ohodnocení musí brát ohled
# na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).

# Příklad hry s číslem 2017:
# Hi there!
# -----------------------------------------------
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# -----------------------------------------------
# Enter a number:
# -----------------------------------------------
# >>> 1234
# 0 bulls, 2 cows
# -----------------------------------------------
# >>> 6147
# 1 bull, 1 cow
# -----------------------------------------------
# >>> 2417
# 3 bulls, 0 cows
# -----------------------------------------------
# >>> 2017
# Correct, you've guessed the right number
# in 4 guesses!
# -----------------------------------------------
# That's {amazing, average, not so good, ...}
# Program toho může umět víc. Můžeš přidat například:
#
# počítání času, za jak dlouho uživatel uhádne tajné číslo
# uchovávat statistiky počtu odhadů jednotlivých her

import random

separator = '-'
print("Hi there!.\n", separator * len("I've generated a random 4 digit number for you."), ' \
                                       '"\nI've generated a random 4 digit number for you."
                                                                                          "\nLet's play a bulls and "
                                                                                          "cows game.")


def secret_number():
    """Selects a random four-digit number that does not contain 0 and does not repeat digits"""

    number_s = []

    while len(number_s) < 4:
        step = random.randrange(1, 10, 1)
        if str(step) not in number_s:
            number_s.append(str(step))
        else:
            continue
    return number_s


secret = secret_number()


def good_choice():

    """Check the correct entry"""

    print(separator * 30)

    while (number := input('Enter the number: ')) != 'q':

        print(separator * 30)
        sorted_number = (sorted(number))

        if '0' in number:
            print('No! No zeros!')

        elif len(str(number)) != 4 and number.isnumeric():
            print('No! The number must be 4 characters long.')

        elif sorted_number[0] == sorted_number[1] or sorted_number[1] == sorted_number[2] or \
                sorted_number[2] == sorted_number[3]:
            print('No number twice!')

        elif len(str(number)) == 4 and number.isnumeric():
            return list(number)

        else:
            print('No! The entry must be numbers.')

    else:
        print('Terminating the program...')
        exit()


def bulls_cows(secret, number):

    """Compares the entered number with the secret number"""

    bull = 0
    cow = 0

    while number != secret:

        for x in range(4):
            if number[x] == secret[x]:
                bull += 1
        for y in number:
            if y in secret:
                cow += 1
        if bull > 1 and cow > 1:
            print(f'bulls {bull} / cows {cow}')
        elif bull > 1 and cow <= 1:
            print(f'bulls {bull} / cow {cow}')
        elif bull <= 1 and cow > 1:
            print(f'bull {bull} / cows {cow}')
        else:
            print(f'bull {bull} / cow {cow}')
        return bull, cow
    else:
        bull += 4
        cow += 4
        print(f'bulls {bull} / cows {cow}')
        return bull, cow


def play():
    """Starts the game"""

    print(secret)
    guesses = 0
    while bulls_cows(secret, good_choice()) != (4, 4):
        guesses += 1
        continue
    else:
        guesses += 1
        print(separator * 54)
        print(''.join(secret))
        print(f"Correct, you've guessed the right number in {guesses} guesses!")
        print(separator * 54)
        print('Terminating the program...')
        exit()


play()
