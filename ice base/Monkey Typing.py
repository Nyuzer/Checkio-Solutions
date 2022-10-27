# https://py.checkio.org/en/mission/monkey-typing/

def count_words(text, words):
    return sum([1 for word in words if word in text.lower()])

