# https://py.checkio.org/en/mission/brackets/


def checkio(expression):
    s = ''.join(c for c in expression if c in '([{}])')
    while s:
        s0, s = s, s.replace('()', '').replace('[]', '').replace('{}', '')
        if s == s0:
            return False
    return True
