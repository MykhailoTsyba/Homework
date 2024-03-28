first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

first_1 = set(first)
second_1 = set(second)
uniq = first_1.difference(second_1)
print(uniq)