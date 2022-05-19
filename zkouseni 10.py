n = ['2', '9', '8', '5']
# moje = ['1', '2', '3', '4']

n_1 = ['1', '2', '3', '4']
# n_1.reverse()
print(n_1)


def good_choice():
    """Check the correct entry"""

    while (number := input('Enter the number. Be careful, the numbers do not repeat!: ')) != 'q':
        sorted_number = (sorted(number))
        print(sorted_number)
        if '0' in number:
            print('NO! No zeros!')

        elif sorted_number[0] == sorted_number[1] or sorted_number[1] == sorted_number[2] or \
                sorted_number[2] == sorted_number[3]:
            print('NO! Double number!')

        elif len(str(number)) == 4 and number.isnumeric():
            return list(number)

        elif len(str(number)) != 4 and number.isnumeric():
            print('NO! The number must be 4 characters long.')

        else:
            print('NO! The entry must be numbers.')

    else:
        print('Terminating the program...')
        exit()


print(good_choice())
