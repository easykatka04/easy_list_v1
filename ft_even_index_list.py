def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_even_index_list(a):
    b = list()
    for i in range(0, ft_len(a), 2):
        b.append(a[i])
    return b
