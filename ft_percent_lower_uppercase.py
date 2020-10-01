def ft_percent_lower_uppercase(str):
    m = 0
    s = 0
    for i in str:
        if i == i.upper():
            m += 1
        else:
            s += 1
    return m / s * 100
