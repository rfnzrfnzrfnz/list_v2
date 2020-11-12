def ft_rmstrchar(str, less):
    s1 = ''
    for i in str:
        if i not in less:
            s1 += i
    return s1
