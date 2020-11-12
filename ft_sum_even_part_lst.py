def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_sum_even_part_lst(str):
    s = 0
    for i in str:
        if i % 2 == 0:
            s += i
    return s
