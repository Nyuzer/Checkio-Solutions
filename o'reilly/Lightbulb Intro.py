# https://py.checkio.org/en/mission/lightbulb-intro/

def sum_light(dates):
    seconds = 0
    for i in range(0, len(dates), 2):
        seconds += (dates[i + 1] - dates[i]).total_seconds()
    return int(abs(seconds))
