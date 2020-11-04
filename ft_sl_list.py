def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_sl_list(a):
    b = list()
    i = 1
    l = 0
    for i in range(0, ft_len(a)):
        if a[i] > a[i-1]:
            l += 1
    return l
