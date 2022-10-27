# https://py.checkio.org/en/mission/reverse-every-ascending/

def reverse_ascending(items):
    result = []
    temp = 0
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            result += sorted(items[temp: i+1], reverse=True)
            temp = i + 1
    result += sorted(items[temp:], reverse=True)
    return result
