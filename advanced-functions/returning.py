# def usAlma(number):
#     def inner(power):
#         return number ** power

#     return inner

# two = usAlma(2)
# three = usAlma(3)

# print(two(3))
# print(three(4))

# def yetkiSorgula(page):
#     def inner(role):
#         if role == 'admin':
#             return '{0} rolünün {1} sayfasına ulaşabilir.'.format(role,page)
#         else:
#             return '{0} rolünün {1} sayfasına ulaşamaz.'.format(role,page)

#     return inner

# user_1 = yetkiSorgula("Product Edit")
# print(user_1('admin'))

def islem(islemAdi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpma = 1
        for i in args:
            carpma *=i
        return carpma

    if islemAdi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
print(toplama(1,3,5,6,7))

carpma = islem("carpma")
print(carpma(1,3,5,7,8))