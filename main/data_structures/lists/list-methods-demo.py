names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1- 'Cenk' ismini listenin sonuna ekleyiniz.
names.append('Cenk')
result = names

# 2- 'Sena' değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
result = names

# 3- 'Deniz' ismini listeden siliniz.
# names.remove('Deniz')
# result = names

# 4- 'Deniz' isminin indeksi nedir ?
result = names.index('Deniz')

# 5- 'Ali' listenin bir elemanı mıdır ?
result = 'Ali' in names

# 6- Liste elemanlarını ters çevirin.
names.reverse()
years.reverse()

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9- str = 'Chevrolet,Dacia' karakter dizisini listeye çeviriniz.
str = 'Chevrolet,Dacia'
cars = str.split(',')
print(cars)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
result = max(years)
result = min(years)

# 11- years dizisinde kaç tane 1998 vardır ?
print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
brands = []

brand = input('Brand: ')
brands.append(brand)

brand = input('Brand: ')
brands.append(brand)

brand = input('Brand: ')
brands.append(brand)

print(brands)