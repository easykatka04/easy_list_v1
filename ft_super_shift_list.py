def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_super_shift_list(num, n):
    a = 0
    if n > 0:
        i = 1
        while a < ft_len(num) - 1:
            temp = num[-i]
            num[-i] = num[-(i + n)]
            num[-(i + n)] = temp
            a = a + 1
            i = i + 1
        return num
    if n < 0:
        i = 0
        while a < ft_len(num) - 1:
            temp = num[i]
            num[i] = num[i + n]
            num[i + n] = temp
            a = a + 1
            i = i + 1
        return num
