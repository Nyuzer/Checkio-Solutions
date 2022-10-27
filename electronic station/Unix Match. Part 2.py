# https://py.checkio.org/en/mission/unix-match-part-2/

from re import search


def unix_match(filename, pattern):
    if filename == pattern:
        return True
    if ('[' and ']') in pattern:
        if pattern.index('[') + 1 == pattern.index(']'):
            pattern = pattern.replace('[', '\[').replace(']', '\]')
    return (
            search(
                pattern.replace('!', '^').replace('*', '.*').replace('.', r'\.').replace('?', '.'), filename
            )
            is not None
        )
