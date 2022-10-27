# https://py.checkio.org/en/mission/common-words/

def checkio(line1, line2):
    line1 = line1.split(',')
    line2 = line2.split(',')
    result = list(filter(lambda elem: elem in line2, line1))
    return ','.join(sorted(result))
