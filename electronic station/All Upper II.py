# https://py.checkio.org/en/mission/all-upper-ii/

def is_all_upper(text):
    if len(text.replace(' ', '')) > 0 and sum(map(str.isalpha, text)) > 0:
        return text.upper() == text
    return False
