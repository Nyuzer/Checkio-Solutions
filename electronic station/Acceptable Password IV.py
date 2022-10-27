# https://py.checkio.org/en/mission/acceptable-password-iv/

def is_acceptable_password(password):
    if len(password) > 9:
        return True
    else:
        return len(password) > 6 and 0 < len(list(filter(lambda x: x.isdigit(), password))) < len(password)
