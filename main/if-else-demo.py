# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.
name = input('İsminiz: ')
age = int(input('Yaşınız: '))
education = input('Eğitim durumunuz: ')

if age >= 18:
    if (education == 'lise' or education == 'üniversite'):
        print(f'{name} ehliyet alabilirsin.')
    else:
        print(f'{name} ehliyet alamazsın, eğitim durumun yetersiz.')
else:
    print(f'{name} ehliyet alamazsın, yaşın tutmuyor.')

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralağına karşılık gelen not bilgisini yazdırın.
#    0-24 => 0
#    25-44 => 1
#    45-54 => 2
#    55-69 => 3
#    70-84 => 4
#    85-100 => 5

# yazılı1 = int(input('1.yazılı: '))
# yazılı2 = int(input('2.yazılı: '))
# sozlu = int(input('sözlü: '))

# ortalama = (yazılı1 + yazılı2 + sozlu)/3

# if ortalama >= 0 and ortalama <= 24:
#     print(f"Notunuz 0 ve ortalamanız: {ortalama}")
# elif ortalama >= 25 and ortalama <= 44:
#     print(f"Notunuz 1 ve ortalamanız: {ortalama}")
# elif ortalama >= 45 and ortalama <= 54:
#     print(f"Notunuz 2 ve ortalamanız: {ortalama}")
# elif ortalama >= 55 and ortalama <= 69:
#     print(f"Notunuz 3 ve ortalamanız: {ortalama}")
# elif ortalama >= 70 and ortalama <= 84:
#     print(f"Notunuz 4 ve ortalamanız: {ortalama}")
# elif ortalama >= 85 and ortalama <= 100:
#     print(f"Notunuz 5 ve ortalamanız: {ortalama}")
# else:
#     print('Yanlış bilgi girdiniz.')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor.
#    (şimdi) - (2018/8/1) => gün
import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2018/8/9): ')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<=365:
    print('1.bakım aralığı')
elif days>365 and days<=365*2:
    print('2.bakım aralığı')
elif days>365*2 and days<=365*3:
    print('3.servis aralığı')
else:
    print('yanlış bilgi girdiniz.')



    