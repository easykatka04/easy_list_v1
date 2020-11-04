def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_rev_list(num):
    for i in range(0, ft_len(num) // 2):
        temp = num[i]
        num[i] = num[-(i + 1)]
        num[-(i + 1)] = temp
    return num
