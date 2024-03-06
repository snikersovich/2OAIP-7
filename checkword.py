def check_word(n, div=None):
    if div is None:
        div = n - 1
    while div >= 2:
        if n % div == 0:
            print("Число не является простым")
            return False
        else:
            return check_word(n, div-1)
    else:
        print("Число является простым")
        return True


n = int(input("Введите число: "))
check_word(n)