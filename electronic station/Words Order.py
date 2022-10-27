# https://py.checkio.org/en/mission/words-order/

def words_order(text, words):
    for word in words:
        if word not in text.split():
            return False
    return [text.index(i) for i in words if words.count(i) == 1] == sorted([text.index(i) for i in words])
