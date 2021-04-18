liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun
# sayı olduğundan emin olunuz aksi halde hata mesajı yazınız.

# while True:
#     sayi = input("Sayı: ")
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print('Girdiğiniz sayı: ',result)
#     except ValueError:
#         print('Geçersiz sayı')
#         continue

# 3: Girilen parola içinde Türkçe karakter hatası veriniz.

# def checkPassword(parola):
#     turkce_karakter = 'şçıİğüö'

#     for i in parola:
#         if i in turkce_karakter:
#             raise TypeError('Parola türkçe karakter içeremez.')
#         else:
#             pass
#     print('Geçerli parola')

# parola = input('Parola: ')

# try:
#     checkPassword(parola)
# except TypeError as error:
#     print(error)

# 4: Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1

    for i in range(1, x+1):
        result *= i

    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as error:
        print(error)
        continue

    print(y)