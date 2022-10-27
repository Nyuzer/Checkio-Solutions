# https://py.checkio.org/en/mission/remove-all-after/

def remove_all_after(items, border):
    return items[:items.index(border) + 1] if border in items else items
