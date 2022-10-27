# https://py.checkio.org/en/mission/merge-intervals-iterator-version/

def merge_intervals(intervals):
    result = []
    for interval in intervals:
        for j in range(interval[0], interval[1] + 1):
            result.append(j)
    return create_intervals(list(set(result)))


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
            result.append((start, start+cnt))
            start = i
            cnt = 0
    return iter(result)
