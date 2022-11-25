def is_pan(n: int) -> int:
    return set(str(n)).issuperset('123456789')


def con_prod(n: int, number_list) -> int:
    """
    concatenated product of n and num_list
    """
    product = ''
    for num in number_list:
        product += str(n * num)
    return int(product)


if __name__ == '__main__':
    print(is_pan(1234))
    print(is_pan(987654321))
    print(is_pan(con_prod(9, [1, 2, 3, 4, 5])))
    print(is_pan(con_prod(192, [1, 2, 3])))

    pan_digital_nums = []
    num_list = [1]
    for j in range(2, 10):
        num_list.append(j)
        for i in range(1, 10000):
            k = con_prod(i, num_list)
            if len(str(k)) > 9:
                break
            if is_pan(k):
                pan_digital_nums.append(k)

    print(pan_digital_nums)
    print(max(pan_digital_nums))

