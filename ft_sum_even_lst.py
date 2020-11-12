def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_sum_even_lst(str):
    s = 0
    for i in range(0, ft_len(str), 2):
        s += str[i]
    return s
