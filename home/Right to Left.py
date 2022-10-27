# https://py.checkio.org/en/mission/right-to-left/

def left_join(phrases):
    result = []
    for phrase in phrases:
        if 'right' in phrase:
            result.append(phrase.replace('right', 'left'))
            continue
        result.append(phrase)
    return ','.join(result)
