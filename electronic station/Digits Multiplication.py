# https://py.checkio.org/en/mission/digits-multiplication/

def checkio(number):
    result = 1
    for i in str(number):
        if int(i) == 0:
            continue
        result *= int(i)
    return result
