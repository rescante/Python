# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
# x = int(input('Sayı: '))

# result = (x > 0) and (x <= 100)


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
# x = int(input('Sayı: '))

# result = (x > 0) and (x % 2 == 0)

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = 'gmail@alperderin.com'
# password = '12345'

# userEmail = input('Email: ')
# userPassword = input('Password:')

# if (email == userEmail) and (password == userPassword):
#     print('Your entry has been applied.') 

# if not(email == userEmail) and not(password == userPassword):
#     print('Your entry has been denied.')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
# x = int(input('1.score: '))
# y = int(input('2.score: '))
# z = int(input('3.score: '))

# if (x > y) and (x > z):
#     print('1.socre is the greatest.')

# if (y > x) and (y > z):
#     print('2.score is the greatest.')

# if (z > x) and (z > y):
#     print('3.score is the greatest.')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    b) Finalden 70 aldığında ortalamanın önemi olmasın.
# x = float(input('First exam: '))
# y = float(input('Second exam: '))
# z = float(input('Final exam: '))

# average = ((x + y)/2) * 0.6 + z * 0.4
# # result1 = (average >= 50) and (z >= 50)
# result2 = (average >= 50) or (z >= 70)

# print(f"Öğrencinin ortalaması: {average} ve sınıfı geçme durumu: {result2} ")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
name = input('Name: ')
weight = float(input('Weight: '))
height = float(input('Height: '))

index = (weight) / (height ** 2)

#    Aşağıdaki tabloya göre kişi hangi kiloya girmektedir ?
#    0-18.4 => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla kilolu
#    30.0-34.9 => Şişman(Obez)

thin = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
overweight = (index > 24.9) and (index <= 29.9)
obese = (index > 29.9) and (index <= 34.9)


print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayif: {thin}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {overweight}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obese}")

