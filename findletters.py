def recursia_find_letter(s):
    if len(s) == 0:
        return 0
    letter = s[0]
    if letter in 'аоуыэеёиюя':
        return 1 + recursia_find_letter(s[1:])
    return recursia_find_letter(s[1:])


print(recursia_find_letter('Рекурсия'))