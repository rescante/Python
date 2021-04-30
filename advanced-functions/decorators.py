# def myDecorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @myDecorator
# def sayHello(name):
#     print("Hello", name)

# sayHello("Mehmet")

import math
import time

def calculateTime(func):
    def inner(*args, **kwargs):

        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " +str(finish-start) + " saniye sürdü.")

    return inner

@calculateTime
def usAlma(a,b):
    print(math.pow(a, b))

@calculateTime
def faktoriyel(num):
    print(math.factorial(num))

@calculateTime
def toplama(a,b):
    print(a+b)
    
usAlma(2,3)
faktoriyel(4)
toplama(10,20)