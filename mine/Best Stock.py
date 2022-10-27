# https://py.checkio.org/en/mission/best-stock/

def best_stock(data):
    return sorted(data, key=lambda x: data[x])[-1]
