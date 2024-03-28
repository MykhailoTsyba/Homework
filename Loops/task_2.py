my_list = [1, 2, 3, 5, 4, 5, 6, 7, 8, 9, 10, 11]

for number in my_list:
    index = my_list.index(number)
    if index == number-1:
        continue
    else: print(f"Inconsistant number is {number} on index {index}")
    break







