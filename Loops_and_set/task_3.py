new_list = []
count = int(input("Enter count of list numbers: "))
for i in range(count):
    new_element = int(input("Enter numbers: "))
    new_list.append(new_element)
uniq_elements = sorted(set(new_list))
print(uniq_elements)