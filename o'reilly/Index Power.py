# https://py.checkio.org/en/mission/index-power/

def index_power(array, n):
    if len(array) - 1 >= n:
        return array[n] ** n
    return -1
