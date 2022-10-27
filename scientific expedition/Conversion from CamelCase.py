# https://py.checkio.org/en/mission/conversion-from-camelcase/

def from_camel_case(name):
    result = []
    x = -1
    for i in range(len(name)):
        if name[i] == name[i].upper():
            word = f'{name[i].lower()}'
            for j in name[i + 1:]:
                if j == j.upper():
                    break
                word += j.lower()
            result.append(word)
    return '_'.join(result)
