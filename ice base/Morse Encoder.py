# https://py.checkio.org/en/mission/morse-encoder/

def morse_encoder(text):
    morse = {'a': '.-', 'b': '-...', 'c': '-.-.',
             'd': '-..', 'e': '.', 'f': '..-.',
             'g': '--.', 'h': '....', 'i': '..',
             'j': '.---', 'k': '-.-', 'l': '.-..',
             'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.',
             's': '...', 't': '-', 'u': '..-',
             'v': '...-', 'w': '.--', 'x': '-..-',
             'y': '-.--', 'z': '--..', '0': '-----',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.'}
    result = []
    super_res = ''
    for word in text.lower().split():
        for symbol in word:
            result.append(morse[symbol])
        super_res += ' '.join(result) + '   '
        print(super_res)
        result = []
    return super_res[:-3]
