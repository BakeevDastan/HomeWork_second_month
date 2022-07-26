def bubble_sort(a):
    N = len(a)
    for i in range(N - 1):
        m = a[i]
        p = i

        for j in range(i + 1, N):
            if m > a[j]:
                m = a[j]
                p = j
        if p != i:
            t = a[i]
            a[i] = a[p]
            a[p] = t
    print(a)


a = [-3, 5, 6, 2, 7, -8]
bubble_sort(a)



def binary_search(arr, low, high, x):

    if high >= low:
        mid = (high + low) // 2
        if mid == x:
            return mid
        elif mid > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, low, high + 1, x)
    else: return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 123, 234, 456, 856, 123, 34, 576, 434364, 123, 34656]
x = 3
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print('Ваше число', result)
else:
    print('Такогго числа не существует')


