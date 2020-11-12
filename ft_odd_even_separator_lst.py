def ft_odd_even_separator_lst(lst):
    c = []
    f = []
    for elem in lst:
        if elem % 2 == 0:
            c += [elem]
        else:
            f += [elem]
    return [c, f]
