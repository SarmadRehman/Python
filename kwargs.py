def sum_func(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


print(sum_func(coffee=2.7, tea=6.3, juice=7.3))
