# https://py.checkio.org/en/mission/majority/

def is_majority(items):
    plus = 0
    minus = 0
    for i in items:
        if i:
            plus += 1
        else:
            minus += 1
    return True if plus > minus and len(items) >= 1 else False
