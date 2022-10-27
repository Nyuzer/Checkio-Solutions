# https://py.checkio.org/en/mission/median/

def checkio(data):
    return sorted(data)[len(data) // 2] if len(data) % 2 == 1 else \
        (sorted(data)[len(data)//2] + sorted(data)[len(data)//2 - 1]) / 2
