# https://py.checkio.org/en/mission/frequency-sorting/

def frequency_sorting(numbers):
    return sorted(sorted(numbers), key=lambda x: numbers.count(x), reverse=True)
