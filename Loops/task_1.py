my_list = [27, 30, 556, 698, 2, 65742, 585, 15, 3, 56, 36554, 213, 458, 512, 654, 9587, 23654, 2536 ,2358, 5632, 53654, 4825]
denominator = int(input("Enter denominator: "))
val_numbers = [number for number in my_list if number % denominator == 0]
print(val_numbers)