# 1- "Bmw, Mazda, Opel, Mercedes" elemanlarına sahip bir liste oluşturunuz.
my_list = ['Bmw', 'Mazda', 'Opel', 'Mercedes']
# 2- Liste kaç elemanlıdır ?
result2 = len(my_list)
print(result2)
# 3- Listenin ilk ve son elemanı nedir ?
result3 = my_list[0],my_list[-1]
print(result3)
# 4- Mazda değerini Toyota ile değiştirin.
my_list[1] = 'Toyota'
result4 = my_list
print(result4)
# 5- Mercedes listenin bir elemanı mıdır ?
result15 = 'Mercedes' in my_list
print(result15)
# 6- Listenin -2 indeksindeki değer nedir ?
result5 = my_list[-2]
print(result5)
# 7- Listenin ilk 3 elemanını alın.
result6 = my_list[0:3]
print(result6)
# 8- Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.
my_list[-2:] = ['Toyota','Renault']
result8 = my_list
print(result8)
# 9- Listenin üzerine 'Audi' ve 'Nissan' değerlerini ekleyin.
my_list.append('Audi')
my_list.append('Nissan')
result9 = my_list
print(result9)
# 10- Listenin son elemanını silin.
del my_list[-1]
result10 = my_list
print(result10)
# 11- Liste elemanlarını tersten yazdırın.
result11 = my_list[::-1]
print(result11)
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

          # studentA: Yiğit Bilgi 2010, (70,60,70)
          # studentB: Sena Turan 1999, (80,80,70)
          # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırın.

Student1 = studentA[0]
Student2 = studentB[1]
Student3 = studentC[3]

print(Student1)
print(Student2)
print(Student3)

resultStudent = f'{(studentA[0])} {(studentA[1])} {(2020-studentA[2])} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}'
print(resultStudent)