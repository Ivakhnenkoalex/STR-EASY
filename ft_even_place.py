def ft_len(str):
    l = 0
    for i in str:
        l = l + 1
    return l


def ft_even_place(str):
    r = ""
    p = ft_len(str)
    for i in range(p):
        if i % 2 == 0:
            r = r + str[i]
    return (r)
