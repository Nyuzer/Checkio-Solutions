# https://py.checkio.org/en/mission/unix-match-part-1/

# without re

def unix_match(filename, pattern):
    l1, l2 = len(filename), len(pattern)
    if filename == pattern:
        return True
    elif pattern.count('*') == l2 and l1 >= 1:
        return True
    # my.exe    *.exe   *.txt   file.txt  *z*
    elif pattern.count('?') >= 1 and pattern.count('*') >= 1 and l1 >= l2:
        for i in pattern:
            if i == '*' or i == '?':
                continue
            elif i in filename:
                continue
            return False
        check = ''
        trigger = 0
        for i in range(l2):
            if pattern[i] == '?':
                check += filename[i]
            elif pattern[i] == '*':
                if l2 - i != 1:
                    check += filename[trigger: filename.index(pattern[i + 1])]
                else:
                    check += filename[trigger + 1:]
            else:
                check += pattern[i]
            trigger = len(check) - 1
        return check == filename
    elif l1 >= l2 > 1 and '*' in pattern:
        for i in pattern:
            if i == '*':
                continue
            elif i in filename:
                continue
            return False
        check = ''
        trigger = 0
        for i in range(l2):
            if pattern[i] == '*':
                if len(pattern) - i != 1:
                    check += filename[trigger: filename.index(pattern[i+1])]
                else:
                    check += filename[trigger + 1:]
            else:
                check += pattern[i]
                trigger = len(check) - 1
        return check == filename
    elif '?' in pattern and l2 == l1:
        check = ''
        for i in range(l1):
            if pattern[i] == '?':
                check += filename[i]
            else:
                check += pattern[i]
        return check == filename
    return False

# with re

"""
from re import search


def unix_match(filename: str, pattern: str) -> bool:
    return (
        search(
            pattern.replace(".", r"\.").replace("*", ".*").replace("?", "."), filename
        )
        is not None
    ) 
"""
