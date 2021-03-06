"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Ladislav Bure3
email: ladislavb01@gmail.com
discord: Láďa#7333
"""

import random


separator = '-'
print(f"Hi there!."
      f"\n{separator * 47}"
      f"\nI've generated a random 4 digit number for you."
      f"\nLet's play a bulls and cows game."
      f"\nYou can end the game by pressing the q key.")


def secret_number():
    """Selects a random four-digit number where 0 is not at the beginning and the digits are not repeated"""

    number_s = list(str(random.randrange(1, 10, 1)))
    number_s_2 = []

    while len(number_s_2) < 3:

        step = random.randrange(0, 10, 1)
        if str(step) not in number_s_2 and str(step) not in number_s:
            number_s_2.append(str(step))
        else:
            continue

    number_s.extend(number_s_2)

    return number_s


def good_choice():
    """Check the correct entry"""

    print(separator * 30)

    while True:
        number = input('Enter the number: ')
        print(separator * 30)
        sorted_number = (sorted(number))

        if number == 'q':
            print(f'The number was: {"".join(secret)} \nTerminating the program...')

            exit()

        elif not number.isnumeric():
            print('No! The entry must be numbers.')

        elif '0' in number[0]:
            print('The number cannot begin with zero!')

        elif len(str(number)) != 4 and number.isnumeric():
            print('No! The number must be 4 characters long.')

        elif sorted_number[0] == sorted_number[1] or sorted_number[1] == sorted_number[2] or \
                sorted_number[2] == sorted_number[3]:
            print('No number twice!')

        else:
            return list(number)



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


secret = secret_number()
play()
