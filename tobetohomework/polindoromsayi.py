sayi = input("Bir sayı girin: ")
ters = sayi[::-1]
if sayi == ters:
    print(sayi, " palindrom sayıdır.")
else:
    print(sayi, " palindrom sayı değildir.")