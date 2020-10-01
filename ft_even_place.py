def ft_len(str):
    n = 0
    for i in str:
        n = n + 1
    return n


def ft_even_place(str):
    r = ""
    p = ft_len(str)
    for i in range(p):
        if i % 2 == 0:
            r = r + str[i]
    return (r)
