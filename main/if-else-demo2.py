# 1-
# sayi = float(input('sayı: '))

# if sayi>0 and sayi<=100:
#     print('Sayı 0 ile 100 arasındadır.')
# else:
#     print('Sayı 0 ile 100 arasında değildir.')

# 2-
# sayi1 = int(input('sayı: '))

# if sayi1>0:
#     if sayi1%2==0:
#         print('Sayı pozitif çift sayıdır.')
#     else:
#         print('Sayı pozifittir fakat çift değildir.')
# else:
#     print('Sayı pozitif değildir.')

# 3-
# email = 'alperderin@gmail.com'
# password = '12345'

# girilenEmail = input('Email: ')
# girilenParola = input('Parola: ')

# if girilenEmail == email:
#     if girilenParola == password:
#         print('Girişiniz onaylandı.')
#     else:
#         print('Girdiğiniz parola yanlış.')
# else:
#     print('Girdiğiniz email veya parola yanlış.')

# 4-
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# if (a>b) and (a>c):
#     print('a en büyük sayıdır.')
# elif (b>a) and (b>c):
#     print('b en büyük sayıdır.')
# elif (c>a) and (c>b):
#     print('c en büyük sayıdır.')

# 5-
# vize1 = float(input('1.vize: '))
# vize2 = float(input('2.vize: '))
# final = float(input('final: '))

# ortalama = ((vize1 + vize2)/2)*0.6 + (final*0.4)

# durum-1
# if (ortalama>=50):
#     if (final>=50):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
# else:
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

# durum-2
# if (ortalama>=50):
#     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
# else:
#     if (final>=70):
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldınız.')
#     else:
#         print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

# 6-
# name = input('isminiz: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))

# index = (kg) / (hg**2)

# if (index >= 0) and (index<=18.4):
#     print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf.')
# elif (index > 18.4) and (index<=24.9):
#     print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
# elif (index>24.9) and (index<=29.9):
#     print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
# elif (index>29.9) and (index<=34.9):
#     print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
# else:
#     print('girilen bilgiler yanlış.')
