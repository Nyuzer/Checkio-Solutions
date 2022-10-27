# https://py.checkio.org/en/mission/count-digits/

def count_digits(text):
    cnt = 0
    for i in text:
        if i.isdigit():
            cnt += 1
    return cnt
