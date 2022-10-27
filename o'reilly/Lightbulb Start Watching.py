# https://py.checkio.org/en/mission/lightbulb-start-watching/

from datetime import datetime


def sum_light(els, start_watching=False):
    result = 0
    if start_watching:
        for i in range(0, len(els), 2):
            if els[i] == start_watching:
                result += (els[i + 1] - els[i]).total_seconds()
            elif els[i] > start_watching:
                result += (els[i + 1] - els[i]).total_seconds()
            elif els[i] < start_watching < els[i + 1]:
                result += (els[i + 1] - start_watching).total_seconds()
    else:
        for i in range(0, len(els), 2):
            result += (els[i + 1] - els[i]).total_seconds()
    return int(result)
