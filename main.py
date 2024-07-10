def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata: Sıfıra bölme hatası!"
    return a / b

print("Yapılacak işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

secim = input("Seçiminizi yapın (1, 2, 3 veya 4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == "1":
    sonuc = toplama(sayi1, sayi2)
    print(f"{sayi1} + {sayi2} = {sonuc}")
elif secim == "2":
    sonuc = cikarma(sayi1, sayi2)
    print(f"{sayi1} - {sayi2} = {sonuc}")
elif secim == "3":
    sonuc = carpma(sayi1, sayi2)
    print(f"{sayi1} * {sayi2} = {sonuc}")
elif secim == "4":
    sonuc = bolme(sayi1, sayi2)
    if isinstance(sonuc, str):
        print(sonuc)
    else:
        print(f"{sayi1} / {sayi2} = {sonuc}")
else:
    print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 girin.")
