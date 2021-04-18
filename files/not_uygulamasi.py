def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    
    ogrenciAdi = liste[0]
    notlar = liste[1]

    not1 = notlar[0]
    not2 = notlar[1]
    not3 = notlar[2]

    ortalama = (not1+not2+not3)/3

    

def ortalamari_oku():
    with open('sinav_notlari.txt','r', encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyadı: ')
    not1 = input('Not 1: ')
    not2 = input('Not 2: ')
    not3 = input('Not 3: ')

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+' '+ soyad+ ':'+ not1+ ','+ not2 + ',' + not3+ '\n')

def notlari_kaydet():
    pass

while True:
    islem = input('1- Not Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem == '1':
        ortalamari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    else:
        break