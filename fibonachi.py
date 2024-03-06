def fibonachi(n):
    if (n <= 1):
        return n
    else:
        return (fibonachi(n-1) + fibonachi(n-2))


n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print(fibonachi(i))