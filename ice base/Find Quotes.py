# https://py.checkio.org/en/mission/find-quotes/

def find_quotes(string):
    result = []
    length = 0
    cnt = 0
    word = ''
    for i in string:
        if i == '"':
            cnt += 1
            length += 1
            if cnt % 2 == 0:
                length = 0
                result.append(word)
                word = ''
            continue
        if length > 0 and cnt % 2 == 1:
            word += i
    return result
