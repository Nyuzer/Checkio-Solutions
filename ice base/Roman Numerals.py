# https://py.checkio.org/en/mission/roman-numerals/

elements = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
}


def checkio(data):
    roman = ''

    for n in sorted(elements.keys(), reverse=True):
        while data >= n:
            roman += elements[n]
            data -= n

    return roman
