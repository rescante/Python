# def sayHello(fname,lname):
#     print('Merhaba' + " " + fname + " " + lname)

# sayHello('Mehmet','Derin')

def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageMehmet = yasHesapla(2002)
ageEylul = yasHesapla(2004)
ageYagiz = yasHesapla(2016)

print(ageMehmet, ageEylul, ageYagiz)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emekli oldunuz.')

EmekliligeKacYilKaldi(2002, 'Mehmet')
print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

# print(help(list.append))


