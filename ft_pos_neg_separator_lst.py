def ft_pos_neg_separator_lst(lst):
    c = []
    e = []
    s = []
    for elem in lst:
        if elem > 0:
            c += [elem]
        elif elem < 0:
            e += [elem]
        else:
            s += [elem]

    return [e, s, c]
