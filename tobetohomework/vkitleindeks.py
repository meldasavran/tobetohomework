#Kullanıcıdan ağırlık bilgisini alır (doğru format kontrolü yapar)
while True:
    try:
        ağırlık = float(input("Ağırlığınızı kilogram cinsinden girin: ").replace(',', '.'))
        break  # Doğru giriş yapıldığında döngüden çık
    except ValueError:
        print("Geçersiz giriş! Lütfen ağırlığı sayı olarak girin.")

#Kullanıcıdan boy bilgisini alır (doğru format kontrolü yapar)
while True:
    try:
        boy = float(input("Boyunuzu metre cinsinden girin: ").replace(',', '.'))
        break  # Doğru giriş yapıldığında döngüden çık
    except ValueError:
        print("Geçersiz giriş! Lütfen boyu sayı olarak girin.")
#Vücut Kitle İndeksini hesaplar
vki=(ağırlık/(boy*boy))
#VKİ değerini yorumlar
if vki < 18.5:
    print("VKİ yorumu: Zayıf")
    ideal_kilo = 18.5 * (boy ** 2)  # Zayıf için ideal kilo hesaplaması
    print("İdeal kilonuz:", ideal_kilo, "kilogram")
elif 18.5 <= vki < 24.9:
    print("VKİ yorumu: Normal")
    ideal_kilo = 22.5 * (boy ** 2)  # Normal için ideal kilo hesaplaması
    print("İdeal kilonuz:", ideal_kilo, "kilogram")
elif 24.9 <= vki < 29.9:
    print("VKİ yorumu: Fazla Kilolu")
    ideal_kilo = 24.9 * (boy ** 2)  # Fazla Kilolu için ideal kilo hesaplaması
    print("İdeal kilonuz:", ideal_kilo, "kilogram")
else:
    print("VKİ yorumu: Obez")
    ideal_kilo = 29.9 * (boy ** 2)  # Obez için ideal kilo hesaplaması
    print("İdeal kilonuz:", ideal_kilo, "kilogram")
