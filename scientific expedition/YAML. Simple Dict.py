# https://py.checkio.org/en/mission/yaml-simple-dict/

def yaml(string):
    collect = string.split()
    result = {}
    for i in collect:
        if ':' in i:
            key = ''
            key = i.replace(':', '')
        else:
            if i.isdigit():
                result[key] = int(i) if result.get(key) == None else str(result[key]) + ' ' + i
            else:
                result[key] = i if result.get(key) == None else str(result[key]) + ' ' + i
                print(result)
    return result


