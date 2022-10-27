# https://py.checkio.org/en/mission/sum-numbers/

def sum_numbers(text: str) -> int:
    result = [int(i) for i in text.split() if i.isdigit()]
    return sum(result)
