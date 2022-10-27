# https://py.checkio.org/en/mission/acceptable-password-v/

def is_acceptable_password(password):
    if len(password) > 9 and 'password' not in password.lower():
        return True
    elif 'password' not in password.lower():
        return len(password) > 6 and 0 < len(list(filter(lambda x: x.isdigit(), password))) < len(password)
    else:
        return False
