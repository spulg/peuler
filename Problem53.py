if __name__ == '__main__':
    solution = 0
    with open("pascal_100.txt") as file:
        lines = file.readlines()
        for line in lines:
            line.strip()
            nums = line.split(' ')
            for num in nums:
                if int(num) > 1_000_000:
                    solution += 1
    print(solution)