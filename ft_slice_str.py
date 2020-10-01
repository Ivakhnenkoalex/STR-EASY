def ft_slice_str(str, start, end):
    x = ""
    for i in range(start, end+1):
        if i >= len(str):
            break
        x = x + str[i]
    return x
