def digital_sum(n):
    _sum = 0
    for c in map(int, str(n)):
        _sum += c
    return _sum

if __name__ == '__main__':
    _max = 0
    for i in range(100):
        for j in range(100):
            if _max < digital_sum(i ** j):
                _max = digital_sum(i ** j)
    print(_max)