def sum_func(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_func(1, 3, 4, 5, 6, 3, 3, 3))
