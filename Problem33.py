import math


def cancel(a: int, b: int) -> (int, int):
    num, dem = str(a), str(b)
    c, d = num, dem
    if sorted(num) == sorted(dem):
        return 1, 1

    for i in range(len(num)):
        for j in range(len(dem)):
            if num[i] == dem[j]:
                c = c.replace(num[i], '')
                d = d.replace(num[i], '')
    if c == '' or d == '' or "0" in c or "0" in d:
        return 1, 1

    return int(c), int(d)


if __name__ == '__main__':
    result = []
    for num in range(11, 100):
        for dem in range(11, 100):
            a, b = cancel(num, dem)
            if a != num and b != dem and num / dem == a / b and a / b < 1 and num % 10 != 0 and dem % 10 != 0:
                print(num, dem, a, b)
                result.append(a / b)
    print(math.prod(result).__round__(10))
