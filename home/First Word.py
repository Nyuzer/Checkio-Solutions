# https://py.checkio.org/en/mission/first-word/

def first_word(text):
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    return text.split()[0]
