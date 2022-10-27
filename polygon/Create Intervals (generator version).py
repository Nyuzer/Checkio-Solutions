# https://py.checkio.org/en/mission/create-intervals-generator-version/

def create_intervals(data):
    data = list(sorted(data))
    data.append(100000000)
    result = []
    cnt = 0
    start = data[0]
    for i in data[1:]:
        if start + cnt == i - 1:
            cnt += 1
        else:
            yield (start, start+cnt)
            start = i
            cnt = 0
