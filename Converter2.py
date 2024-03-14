print("1 USD is 38,49 UAH")
UAH_exchange = 38.49
USD_exchange = 0.0259
USD = float(input("Please, enter amount (USD): "))
UAH = float(input("Please, enter amount (UAH): "))

if USD is float:
    result_1 = USD * UAH_exchange
elif UAH is float:
    result_2 = UAH * USD_exchange
else:
    result = "eror"

print(f"{result_1} UAH")
print(f"{result_2} USD")