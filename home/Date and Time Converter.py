# https://py.checkio.org/en/mission/date-and-time-converter/

from datetime import datetime


def date_time(time):
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if dt.hour == 1 else 'hours'
    minute = 'minute' if dt.minute == 1 else 'minutes'
    return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')
