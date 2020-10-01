def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)


def ft_cmp_str(str1, str2, num):
    result = ""
    num = num - 1
    for i in range(num):
        result = result + str1[i]
    result = result + str2

    for i in range(num, ft_len(str1)):
        result = result + str1[i]
    return result
