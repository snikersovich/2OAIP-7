def maxlist(a,n):
    x = a[-n]
    if n == 1:
        return x
    return max(x, maxlist(a, n-1))


list = [1, 2, 3, 4, 5]
max_number = max(list)
print('Максимальное число: ', max_number)
