def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4, islemAdi):
    if islemAdi == "toplama":
        print(f1(2,3))
    elif islemAdi == "cikarma":
        print(f2(5,3))
    elif islemAdi == "carpma":
        print(f3(3,4))
    elif islemAdi == "bolme":
        print(f4(10,2))
    else:
        print("Geçersiz işlem...")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "ustalma")