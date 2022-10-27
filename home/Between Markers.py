# https://py.checkio.org/en/mission/between-markers/

def between_markers(text, begin, end):
    x, y = 0, -1
    if begin in text:
        x = text.index(begin) + len(begin)
    if end in text:
        y = text.index(end)
    return text[x:y] if y > 0 else text[x:]
