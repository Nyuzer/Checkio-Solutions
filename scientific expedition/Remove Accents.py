# https://py.checkio.org/en/mission/remove-accents/

import unicodedata

def checkio(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')
