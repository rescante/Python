# error handling => hata yönetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('Yanlış bilgi girdiniz.')
#     print(e)
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('Yanlış bilgi girdiniz.', ex)
    else:
        break
    finally:
        print('try except sonlandı.')