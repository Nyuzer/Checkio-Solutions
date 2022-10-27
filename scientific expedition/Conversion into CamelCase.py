# https://py.checkio.org/en/mission/conversion-into-camelcase/

def to_camel_case(name):
    name = name.replace('_', ' ').split()
    result = [word[0].upper() + word[1:] for word in name]
    return ''.join(result)
