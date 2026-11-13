# EP. «Procedural Paradigms»
# Bilet nr.19
# Grupa: IT21Z
# N.P: Clițman Vladislav
# Задача 1: Разделение по знаку: Имея массив чисел, разделить его на два списка: первый — с положительными числами, второй — с отрицательными.
# Задача 2: Палиндромный массив: Проверить, читается ли заданный массив чисел одинаково как слева направо, так и справа налево



# Задача 1: Разделение по знаку

def split_by_sign(arr):
    positive = []
    negative = []

    for x in arr:
        if x > 0:
            positive.append(x)
        elif x < 0:
            negative.append(x)

    return positive, negative


numbers = [6, -2, 0, 9, -1, 5, -7, 0, 3, -4, 8, -6, 0]
pos, neg = split_by_sign(numbers)
print("Положительные:", pos)
print("Отрицательные:", neg)




# Задача 2: Палиндромный массив

def is_palindrome(arr):
    i = 0                      # левый указатель
    j = len(arr) - 1           # правый указатель

    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1

    return True

tests = [[1, 2, 3, 2, 1], [1, 2, 2, 1], [1, 2, 3], [5], []]
for t in tests:
    print(t, "->", is_palindrome(t))

