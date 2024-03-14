print("USD = 38,49")
print("EUR = 42.22")
UAHd_exchange = 38.49
USD_exchange = 0.0259
UAHe_exchange = 42.22
EUR_exchange = 0.0236
USD = input("USD --> UAH: ")
UAHd = input("UAH --> USD: ")
EUR = input("EUR --> UAH: ")
UAHe = input("UAH --> EUR: ")


if USD.isdigit():
    result_1 = float(USD) * UAHd_exchange
if UAHd.isdigit():
    result_2 = float(UAHd) * USD_exchange
if EUR.isdigit():
    result_3 = float(EUR) * UAHe_exchange
if UAHe.isdigit():
    result_4 = float(UAHe) * EUR_exchange

if USD.isdigit():
    print(f"{USD} USD = {result_1} UAH")
if UAHd.isdigit():
    print(f"{UAHd} UAH = {result_2} USD")
if EUR.isdigit():
    print(f"{EUR} EUR = {result_3} UAH")
if UAHe.isdigit():
    print(f"{UAHe} UAH = {result_4} EUR")
else:
    print("Eror: please, enter digit")