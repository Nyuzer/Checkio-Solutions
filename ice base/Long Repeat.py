# https://py.checkio.org/en/mission/long-repeat/

def long_repeat(line):
    if len(line) > 0:
        res = []
        n_c = 0
        symbol = line[0]
        for i in line:
            if i == symbol:
                n_c += 1
            else:
                symbol = i
                res.append(n_c)
                n_c = 1
            if sum(res) + n_c == len(line):
                res.append(n_c)
        return max(res)
    else:
        return 0
