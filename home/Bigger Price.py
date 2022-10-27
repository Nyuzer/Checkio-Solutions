# https://py.checkio.org/en/mission/bigger-price/

def bigger_price(limit, data):
    result = []
    x = sorted(data, key=lambda x: x['price'])
    for i in range(1, limit + 1):
        result.append(x[-i])
    return result
