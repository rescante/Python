# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f"a: {a} sayısı b: {b} sayısından büyüktür: {result}")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# exam1 = float(input('1.vize: '))
# exam2 = float(input('2.vize: '))
# final = float(input('final: '))

# average = ((((exam1 + exam2) / 2) * 0.6) + (final* 0.4))
# print(f"Not ortalamanız: {average} ve dersten geçme durumunuz: {average>50} ")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# score = int(input('Sayı: '))

# oddeven = (score % 2 == 0)

# print(f"Girilen sayı çiftdir: {oddeven} ")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

# score = int(input('Sayı: '))

# positive = (score > 0)

# print(f"Girilen sayı pozitiftir: {positive}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

email = 'email@alperderin.com'
password = 'abc123'

enterMail = input('Email: ')
enterPassword = input('Şifre: ')

isMail = (email == enterMail.lower().strip())
isPassword = (password == enterPassword.lower())

print(f"Email bilgisi doğru mu: {isMail} ve Parola bilgisi doğru mu: {isPassword}")


