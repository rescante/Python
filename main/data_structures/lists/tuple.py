list = [1, 2, 3]

tuple = (1, 'iki', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))

list = ['Ayşe','Veli']
tuple = ('Damla','Ayşe')
names = ('Gamze','Atalay','Mehmet') + tuple

list[0] = 'Mehmet'
# tuple[0] = 'Mehmet' ---> Tupleda eleman değiştirilemez.

print(names)

print(list)
print(tuple)