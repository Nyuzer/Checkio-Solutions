# https://py.checkio.org/en/mission/sum-by-type/


def sum_by_types(items):
    string = ''
    summa = 0
    for i in items:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            string += i
    return [string, summa]
