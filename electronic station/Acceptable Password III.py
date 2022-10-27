# https://py.checkio.org/en/mission/acceptable-password-iii/

def is_acceptable_password(word):
    cnt = 0
    for i in word:
        if i.isdigit():
            cnt += 1
    if len(word) - cnt == 0:
        return False
    return len(word) > 6 and cnt > 0
