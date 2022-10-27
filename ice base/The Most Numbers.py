# https://py.checkio.org/en/mission/most-numbers/

def checkio(*args):
    return abs(-max(args) + min(args)) if args else 0
