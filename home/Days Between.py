# https://py.checkio.org/en/mission/days-diff/

from datetime import datetime


def days_diff(a, b):
    return abs((datetime(*a) - datetime(*b)).days)
