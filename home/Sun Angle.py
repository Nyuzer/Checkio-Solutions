# https://py.checkio.org/en/mission/sun-angle/

import datetime


def sun_angle(time):
    time = time.split(':')
    if datetime.time(6, 0, 0) <= datetime.time(int(time[0]), int(time[1]), 0) <= datetime.time(18, 0, 0):
        result = (int(time[0]) - 6) * 15 + int(time[1]) / 4
        return result
    else:
        return "I don't see the sun!"
