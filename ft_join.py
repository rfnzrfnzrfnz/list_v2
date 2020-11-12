def ft_len(st):
    l = 0
    for i in st:
        l += 1
    return l


def ft_join(lst, se=" "):
    s = ''
    for i in range(ft_len(lst)):
        if i == ft_len(lst) - 1:
            s += lst[i]
        else:
            s += lst[i] + se
    return s
