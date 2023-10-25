maas = float(input("Mevcut maaşı girin: "))
zamOrani = float(input("Zam oranını yüzde olarak girin: "))
zamOrani = zamOrani / 100
zamliMaas = maas + (maas * zamOrani)
print("Zamlı maaş:", zamliMaas)