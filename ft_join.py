def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_join(lst, sep=' '):
    c = ''
    for i in range(ft_len(lst)):
        if i == ft_len(lst) - 1:
            c += lst[i]
        else:
            c += lst[i] + sep
    return c
