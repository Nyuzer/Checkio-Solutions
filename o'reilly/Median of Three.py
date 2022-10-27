# https://py.checkio.org/en/mission/median-of-three/

def median_three(items):
    result = []
    for i in range(0, len(items)):
        if len(result) >= 2:
            array = []
            for j in range(2, -1, -1):
                array.append(items[i - j])
            array.remove(min(array))
            array.remove(max(array))
            result.append(array[0])
        else:
            result.append(items[i])
    return result
