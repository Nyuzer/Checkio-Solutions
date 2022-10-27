# https://py.checkio.org/en/mission/yaml-more-types/

def kav(word):
    word = word[word.find('"') + 1: word.rfind('"')]
    return word.replace('\\', '')


def yaml(a):
    t = [i.strip() for i in a.split('\n') if i]
    d = {}
    for elem in t:
        if elem.count('"') % 2 == 0 and elem.count('"') > 2:
            val = kav(elem)
            key = elem.split(':')[0].replace('"', '').replace('\\', '')
            d[key] = val
            continue
        key, val = (i.strip().replace('\\', '') for i in elem.split(':'))
        if val.count('"') == 2:
            d[key] = val.replace('"', '')
            continue
        if val == '' or val == 'null':
            d[key] = None
            continue
        if val.upper() == "FALSE":
            d[key] = False
            continue
        if val.upper() == "TRUE":
            d[key] = True
            continue

        d[key] = int(val) if val.isdecimal() else val
    sorted_d = {}
    for key in sorted(d):
        sorted_d[key] = d[key]
    return sorted_d
