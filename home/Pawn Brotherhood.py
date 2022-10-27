# https://py.checkio.org/en/mission/pawn-brotherhood/


def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)


def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])
