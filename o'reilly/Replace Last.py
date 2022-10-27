# https://py.checkio.org/en/mission/replace-last/

def replace_last(line):
    if line:
        x = [line.pop(-1)]
        return x + line
    return []
