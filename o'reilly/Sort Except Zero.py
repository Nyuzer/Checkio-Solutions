# https://py.checkio.org/en/mission/sort-except-zero/

def except_zero(items):
    x = []
    y = 0
    for i in range(items.count(0)):
        x.append(items.index(0, y))
        y = items.index(0, y) + 1
    items = sorted([i for i in items if i != 0])
    for i in x:
        items.insert(i, 0)
    return items
