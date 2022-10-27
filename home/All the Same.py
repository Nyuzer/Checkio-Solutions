# https://py.checkio.org/en/mission/all-the-same/

from functools import reduce


def all_the_same(elements):
    return reduce(lambda x, y: x == y, elements) if len(elements) > 1 else all(elements)
