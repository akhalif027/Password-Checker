import string

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation
upper = string.ascii_uppercase

MINIMUM_PASSWORD_LENGTH = 6


def get_password():
    password = input('Please enter your password ')

    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print('Your Password must be at least 6 characters long. Enter a new password')
        password = input('Please enter your password ')

    return password


def password_strength_checker(password=None):
    if not password:
        password = get_password()

    elif len(password) < MINIMUM_PASSWORD_LENGTH:
        print('Your password is too short.')

    strength = 0

    if len(password) >= 9:
        strength += 1

    for i in password:
        if i in numbers:
            strength += 1
        if i in special:
            strength += 1
        if i in upper:
            strength += 1

    if strength <= 1:
        print('Your password is very weak. Try making your password longer')
    elif 2 <= strength <= 3:
        print('Your Password is weak. Try adding special characters or numbers.')
    elif 3 < strength <= 5:
        print('Your Password is okay')
    elif 5 < strength <= 7:
        print('Your Password is good')
    else:
        print('Your Password is strong')


password_strength_checker('Password')
