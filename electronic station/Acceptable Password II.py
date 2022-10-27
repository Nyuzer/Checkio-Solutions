# https://py.checkio.org/en/mission/acceptable-password-ii/

def is_acceptable_password(word):
    cnt = 0
    for i in word:
        if i.isdigit():
            cnt += 1
            break
    return len(word) > 6 and cnt > 0
