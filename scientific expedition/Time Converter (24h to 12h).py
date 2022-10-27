# https://py.checkio.org/en/mission/time-converter-24h-to-12h/

import datetime


def time_converter(time):
    time = time.split(':')
    if time[0] == '00' and time[1] == '00':
        return '12:00 a.m.'
    elif time[0] == '12' and time[1] == '00':
        return '12:00 p.m.'
    elif datetime.time(int(time[0]), int(time[1]), 0) < datetime.time(12, 0, 0):
        return f'{int(time[0])}:{time[1]} a.m.'
    return f'{int(time[0]) - 12}:{time[1]} p.m.' if int(time[0]) != 12 else f'{time[0]}:{time[1]} p.m.'
