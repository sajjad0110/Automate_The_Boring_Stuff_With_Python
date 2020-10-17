import sys


def collatz(number):
    if number % 2 == 0:
        return (number // 2)
    elif number % 2 == 1:
        return (3 * number + 1)


try:
    digit = int(input('Enter the number: '))

    while digit >= 1:
        print(collatz(digit))
        digit = collatz(digit)
        if digit == 1:
            sys.exit()
except ValueError:
    print('Do not enter noninteger string.')
