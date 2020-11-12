def ft_join(lst, sep=" "):
    res_str = ''
    for item in lst[:-1]:
        res_str += str(item) + sep
    res_str += str(lst[-1])
    return res_str
