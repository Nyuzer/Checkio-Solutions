# https://py.checkio.org/en/mission/ascending-list/

def is_ascending(items):
    return True if items == sorted(items) and len(set(items)) == len(items) else False
