# https://py.checkio.org/en/mission/bird-language/


translate = lambda s: s and s[0]+translate(s[1 + (s[0] != ' ')+(s[0] in 'aeiouy'):])
