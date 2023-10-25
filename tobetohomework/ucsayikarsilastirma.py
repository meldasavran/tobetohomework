sayi1=float(input(("1.Sayıyı Giriniz:")))
sayi2=float (input(("2.Sayıyı Giriniz:")))
sayi3=float (input(("3.Sayıyı Giriniz:")))
if sayi1 > sayi2 and sayi1 > sayi3:
    enBbuyuk = sayi1
elif sayi2 > sayi1 and sayi2 > sayi3:
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

if sayi1 < sayi2 and sayi1 < sayi3:
    enKucuk = sayi1
elif sayi2 < sayi1 and sayi2 < sayi3:
    enKucuk = sayi2
else:
    enKucuk = sayi3


print("En büyük sayı:", enBuyuk)
print("En küçük sayı:", enKucuk)