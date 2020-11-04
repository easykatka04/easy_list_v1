def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_even_parts_list(a):
    b = list()
    for i in range(0, ft_len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
    return b
