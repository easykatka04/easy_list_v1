def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_rev_par_list(num):
    i = 1
    a = 0
    while a < ft_len(num) - 1:
        temp = num[-i]
        num[-i] = num[-(i + 1)]
        num[-(i + 1)] = temp
        a = a + 1
        i = i + 1
    return num
