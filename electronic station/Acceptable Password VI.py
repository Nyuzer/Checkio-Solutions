# https://py.checkio.org/en/mission/acceptable-password-vi/

def is_acceptable_password(password):
    collect = set(password)
    if len(list(filter(lambda x: x.isdigit(), collect))) >= 3 or \
            len(list(filter(lambda x: x.isalpha(), collect))) >= 3 or (\
            len(list(filter(lambda x: x.isdigit(), collect))) +\
            len(list(filter(lambda x: x.isalpha(), collect))) >= 3):
        if len(password) >= 9 and 'password' not in password.lower():
            return True
        elif 'password' not in password.lower():
            return len(password) > 6 and 0 < len(list(filter(lambda x: x.isdigit(), password))) < len(password)
    return False
