string_1 = str(input('Enter the text: '))
string_2 = str(input('Confirm the text: '))
len_str_1 = len(string_1)
len_str_2 = len(string_2)


if string_1 == string_2:
    print('Data are confirmed')
else:
    print('Data aren\'t confirmed')