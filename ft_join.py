def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_join(lst, sep=" "):
    s = ''
    for i in range(ft_len(lst)):
        if i == ft_len(lst) - 1:
            s += lst[i]
        else:
            s += lst[i] + sep
    return s
