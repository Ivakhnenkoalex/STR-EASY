def ft_percent_lower_uppercase(str):
    m = 0
    s = 0
    for i in str:
        if i == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or 'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'Y' or 'T' or 'R' or ' Q' or 'W' or 'P' or 'Z' or 'X' or 'C' or 'V' or 'U' or 'А' or 'Б' or 'В' or 'Г' or 'Д' or 'Е' or 'Ё' or 'Ж' or 'З' or 'И' or 'Й' or 'К' or 'Л' or 'М' or 'Н' or 'О' or 'П' or 'Р' or 'С' or 'Т' or 'Ф' or 'Х' or 'Ц' or 'Ш' or 'Щ' or 'Ъ' or 'Ь' or 'Э' or 'Ю' or 'Я':
            m = m + 1
        else:
            s = s + 1
    return m / s * 100
