def slices(numbers, digit):
    if digit <= 0:
        raise ValueError
    if len(numbers) < digit:
        raise ValueError

    ret = []
    numbers_list = list(numbers)
    numbers_list = [int(x) for x in numbers_list]
    for i in range(len(numbers_list) - digit + 1):
        ret.append(numbers_list[i:i+digit])
    return ret
