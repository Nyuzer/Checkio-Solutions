# https://py.checkio.org/en/mission/second-index/

def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) >= 2:
        x = text.index(symbol)
        text = text[:x] + '_' + text[x+1:]
        return text.index(symbol)
    return None
