print("USD = 38,49")
print("EUR = 42.22")
USD = input("USD --> UAH: ")
UAHd = input("UAH --> USD: ")
EUR = input("EUR --> UAH: ")
UAHe = input("UAH --> EUR: ")


if USD.isdigit():
    print(f"{USD} USD = {float(USD) * 38.49} UAH")
if UAHd.isdigit():
    print(f"{UAHd} UAH = {float(UAHd) / 38.49} USD")
if EUR.isdigit():
    print(f"{EUR} EUR = {float(EUR) * 42.22} UAH")
if UAHe.isdigit():
    print(f"{UAHe} UAH = {float(UAHe) / 42.22} EUR")
