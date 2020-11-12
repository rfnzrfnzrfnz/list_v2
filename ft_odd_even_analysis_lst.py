def ft_odd_even_separator_lst(lst):
    c = []
    f = []
    for elem in lst:
        if elem % 2 == 0:
            c += [elem]
        else:
            f += [elem]
    return [c, f]


def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_rmstrchar(str):
    s = 0
    for i in str:
        if i % 2 == 0:
            s += i
    return s


def ft_rtrchar(str):
    p = 0
    for i in str:
        if i % 2 == 1:
            p += i
    return p


def ft_odd_even_analysis_lst(lst):
    a = ft_odd_even_separator_lst(lst)
    kolchet = 0
    maxchet = a[0][0]
    minchet = a[0][0]
    kolnechet = 0
    maxnechet = a[1][0]
    minnechet = a[1][0]
    sumchet = ft_rmstrchar(lst)
    kolchet = ft_len(a[0])
    kolnechet = ft_len(a[1])
    sumnechet = ft_rtrchar(lst)
    for i in a[0]:
        if i > maxchet:
            maxchet = i
        if i < minchet:
            minchet = i
    for i in a[1]:
        if i > maxnechet:
            maxnechet = i
        if i < minnechet:
            minnechet = i
    print('Анализ списка:')
    print('Количество четных чисел: ', kolchet, ',\t\tКоличество нечетных чисел: ', kolnechet, ',', sep='')
    print('Максимальная четная цифра: ', maxchet, ',\t\tМаксимальная нечетная цифра: ', maxnechet, ',', sep='')
    print('Минимальная четная цифра: ', minchet, ',\t\tМинимальная нечетная цифра: ', minnechet, ',', sep='')
    print('Сумма четных чисел: ', sumchet, ',\t\tСумма нечетных чисел: ', sumnechet, ',', sep='')
    print('')
    return kolchet, maxchet, minchet, sumchet, kolnechet, maxnechet, minnechet, sumnechet
