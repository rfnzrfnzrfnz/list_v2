def ft_join(lst, sep=" "):
    res_str = ''
    for item in lst[:-1]:
        res_str += f"{item}" + sep
    res_str += f"{lst[-1]}"
    return res_str
