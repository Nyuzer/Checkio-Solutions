# https://py.checkio.org/en/mission/backward-each-word/

def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))
