# https://py.checkio.org/en/mission/goes-after/

def goes_after(word, first, second):
    if first in word and second in word:
        return word.index(second) - word.index(first) == 1
    return False
