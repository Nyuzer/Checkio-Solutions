# https://py.checkio.org/en/mission/sort-array-by-element-frequency/

def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
