# https://py.checkio.org/en/mission/split-list/

def split_list(items):
    result = [[], []]
    for i in range(len(items)//2, 0, -1):
        result[1].append(items[-i])
    for i in range(len(items) - len(items)//2):
        result[0].append(items[i])

    return result
