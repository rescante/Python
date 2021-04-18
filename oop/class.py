# # class

# class Person:

#     # class attributes
#     address = 'no information'

#     # constructor (yapıcı method)
#     def __init__(self, name, year):

#         # object attributes
#         self.name = name
#         self.year = year
        

#     # instance methods
#     def intro(self):
#         print('Hello there!, I am ' + self.name)

#     def calculateAge(self):
#         return 2020 - self.year



# # object (instance)

# person1 = Person('Mehmet', 2002)
# person2 = Person('Hatice', 1979)

# person1.intro()
# person2.intro()

# # updating
# person1.name = 'Özkan'
# person2.address = 'Zonguldak'

# # accessing object attributes
# print(f'name: {person1.name} ve yaşım: {person1.calculateAge()}, address: {person1.address}')
# print(f'name: {person2.name} ve yaşım: {person2.calculateAge()}, address: {person2.address}')


class Circle:
    # class object attribute
    pi = 3.14

    def __init__(self, yaricap= 1):
        self.yaricap = yaricap

    # methods
    def cevre_Hesapla(self):
        return 2*self.pi + self.yaricap

    def alan_Hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() # yarıçap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_Hesapla()} çevre = {c1.cevre_Hesapla()}")
print(f"c2 : alan = {c2.alan_Hesapla()} çevre = {c2.cevre_Hesapla()}")
