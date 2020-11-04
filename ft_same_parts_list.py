def ft_len(z):
    x = 0
    for i in z:
        x = x + 1
    return x


def ft_same_parts_list(a):
    b = list()
    i = 1
    l = 0
    for i in range(0, ft_len(a)):
        if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
            l = l + 1
        if a[i] == 0 and a[i-1] == 0:
            l = l + 1
    if l > 0:
        return True
    if l == 0:
        return False
