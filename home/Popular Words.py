# https://py.checkio.org/en/mission/popular-words/

def popular_words(text: str, words: list) -> dict:
    result = {}
    for i in words:
        x = text.lower().split().count(i)
        result[i] = x
    return result
