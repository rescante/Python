# Bankamatik Uygulaması

MehmetHesap = {
    'ad': 'Mehmet Derin',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

EylulHesap = {
    'ad': 'Eylul Derin',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Hoşgeldin {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranız alabilirsiniz.')
        bakiyeSorgulama(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanılsın mı ? (evet/hayır)')

            if ekHesapKullanimi == 'evet':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0 
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranızı çekebilirsiniz.')
                bakiyeSorgulama(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} kalmıştır.")
        else:
            print('üzgünüz bakiyeniz yetersiz.')
            bakiyeSorgulama(hesap)

def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL'dir.")

paraCek(MehmetHesap, 4500)

