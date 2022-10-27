# https://py.checkio.org/en/mission/three-words/

def checkio(words):
    result = 0
    for word in words.split():
        if word.isalpha():
            result += 1
            if result == 3:
                break
        else:
            result = 0
    return result == 3
