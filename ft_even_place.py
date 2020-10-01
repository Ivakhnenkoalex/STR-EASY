def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return a


def ft_even_place(str):
    r = ""
    b = ft_len(str)
    for i in range(b):
        if i % 2 == 0:
            r = r + str[i]
    return(r)
