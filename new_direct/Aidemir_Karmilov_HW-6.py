def bubble_sort(lis):
    n = len(lis)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]


lis = [90, 48, 4, 1, 10, 91]
bubble_sort(lis)
print("Отсортированный список:")
print(lis)


def binary_search(val, a):
    result_ok = False
    first = 0
    last = len(a) - 1
    pos = 0

    while first < last and not result_ok:
        mid = (first + last) // 2
        if val == a[mid]:
            first = mid
            last = first
            result_ok = True
            pos = mid
        elif val > a[mid]:
            first = mid + 1
        else:
            last = mid - 1

    if result_ok:
        print(f'Элемент найден.{pos}')
    else:
        print(f'Элемент не найден.')


a = [1, 3, 5, 7, 9, 11, 13]
target = 7
binary_search(target, a)
