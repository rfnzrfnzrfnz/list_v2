def ft_len(str):
    l = 0
    for i in str:
        l += 1
    return (l)


def ft_pos_neg_analysis_lst(lst):
    kolpol = 0
    kolotr = 0
    nol = 0
    maxpol = -1
    maxotr = -1
    minpol = 0
    minotr = 0
    summapol = 0
    summaotr = 0

    for i in lst:
        if i > 0:
            kolpol += 1
            if i > maxpol:
                maxpol = i
            if i < minpol:
                minpol = i
            summapol = summapol + i

        elif i < 0:
            kolotr += 1
            if i > maxotr:
                maxotr = i
            if i < minotr:
                minotr = i
            summaotr = summaotr + i
        else:
            nol += 1
    print('Положительные:', "\t\tОтрицательные:")
    print('Количество чисел: ', kolpol, ',\t\tКоличество чисел: ', kolotr, ',', sep='')
    print('Максимальная цифра: ', maxpol, ',\t\tМаксимальная цифра: ', maxotr, ',', sep='')
    print('Минимальная цифра: ', minpol, ',\t\tМинимальная цифра: ', minotr, ',', sep='')
    print('Сумма чисел:', summapol, ',\t\tСумма чисел: ', summaotr, ',', sep='')
    print('Среднее значение: ', summapol / kolpol, '\t\tСреднее значение:', summaotr / kolotr, sep='')
    print()
    print('Количество нулей:', nol, sep='')
    return kolpol, kolotr, maxpol, maxotr, minpol, minotr, nol, summapol, summaotr
ft_pos_neg_analysis_lst([-1,-2,-3,-4,0,0,1,2,3,4,5,6])