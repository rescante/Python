'''
         ogrenciler = {
             '120': {
                 'ad': 'Ali',
                 'soyad': 'Yılmaz',
                 'telefon': '532 000 00 61'
             },
             '125': {
                 'ad': 'Can',
                 'soyad': 'Korkmaz',
                 'telefon': '532 000 00 21'
             },
             '128': {
                 'ad': 'Volkan',
                 'soyad': 'Yükselen',
                 'telefon': '532 000 00 38'
             },
         }
         
         1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
         dictionary içinde saklayınız.

         2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

# ogrenciler = {
#     input('öğrenci no: '): {
#         input('ad: '),
#         input('soyad: '),
#         input('telefon: ')
#     },
#     input('öğrenci no: '): {
#         input('ad: '),
#         input('soyad: '),
#         input('telefon: ')
#     },
#     input('öğrenci no: '): {
#         input('ad: '),
#         input('soyad: '),
#         input('telefon: ')
#     }
# }

# print(ogrenciler) ---> Benim yazdığım kod.

ogrenciler = {}

number = input('öğrenci no:')
name = input('öğrenci ad:')
surname = input('öğrenci soyad:')
phone = input('öğrenci telefon:')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input('öğrenci no:')
name = input('öğrenci ad:')
surname = input('öğrenci soyad:')
phone = input('öğrenci telefon:')

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input('öğrenci no:')
name = input('öğrenci ad:')
surname = input('öğrenci soyad:')
phone = input('öğrenci telefon:')

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})


print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefon numarası: {ogrenci['telefon']}")