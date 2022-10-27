# https://py.checkio.org/en/mission/fizz-buzz/

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    return str(number)
