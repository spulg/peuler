# as far as I can tell, you need to write out all of the special cases of how numbers are constructed, then you can
# write a sort of regular expression to generate them recursively


numbers = {
    "1": 'one' ,
    "2": 'two',
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
    "9": 'nine',
    "10": 'ten',
    "11": 'eleven',
    "12": 'twelve',
    "13": 'thirteen',
    "14": 'fourteen',
    "15": 'fifteen',
    "18": 'eighteen',

    "20": 'twenty',
    "30": 'thirty',
    "40": 'forty',
    "50": 'fifty',
    "80": 'eighty',
    "100": 'hundred',
    "1000": 'thousand'

}


def sum_of_num_of_letters(n):
    temp = 0
    for i in range(1, n+1):
        temp += num_of_letters(i)
    return temp


def num_of_letters(n):
    return len(construct_number(n))


def construct_number(n):
    length = len(str(n))
    if length == 4 and int(str(n)[1:]) == 000:
        return construct_number(int(str(n)[0])) + numbers["1000"]  # 1000 would call '000' which would call '00'..
    if length == 4:
        return construct_number(int(str(n)[0])) + numbers["1000"] + construct_number(int(str(n)[1:]))
    if length == 3 and int(str(n)[1:]) == 00:  # 300, 400 etc. are also edge cases
        return construct_number(int(str(n)[0])) + numbers["100"]
    if length == 3:
        return construct_number(int(str(n)[0])) + numbers["100"] + "and" + construct_number(int(str(n)[1:]))
    if length == 2:
        if str(n) in numbers:
            return numbers[str(n)]
        if str(n)[0] == '1':
            return construct_number(int(str(n)[1:])) + 'teen'
        if str(n)[0] == '2':
            return numbers["20"] + construct_number(int(str(n)[1:]))
        if str(n)[0] == '3':
            return numbers["30"] + construct_number(int(str(n)[1:]))
        if str(n)[0] == '4':
            return numbers["40"] + construct_number(int(str(n)[1:]))
        if str(n)[0] == '5':
            return numbers["50"] + construct_number(int(str(n)[1:]))
        if str(n)[0] == '8':
            return numbers["80"] + construct_number(int(str(n)[1:]))
        else:
            return construct_number(int(str(n)[0])) + "ty" + construct_number(int(str(n)[1:]))
    if length == 1:
        if n == 0:
            return ''
        return numbers[str(n)]
    

def solve_problem():
    print(sum_of_num_of_letters(1000))


if __name__ == "__main__":
    import time

    start_time = time.time()
    solve_problem()
    print("runtime: \x1b[1;31m%.1fs\x1b[0m" % (time.time() - start_time))

import profile
profile.run('solve_problem()')



