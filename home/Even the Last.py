# https://py.checkio.org/en/mission/even-last/

def checkio(array):
    summary = 0
    for i in range(0, len(array), 2):
        summary += array[i]
    return summary * array[-1] if len(array) > 0 else summary
