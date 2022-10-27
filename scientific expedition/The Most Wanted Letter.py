# https://py.checkio.org/en/mission/most-wanted-letter/

def checkio(text):
    letters = ''.join(list(filter(str.isalpha, text))).lower()
    counter = {x : 0 for x in sorted(set(letters))}
    for i in letters:
        counter[i] += 1
    return max(counter, key=counter.get)
