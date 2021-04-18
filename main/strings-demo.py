website = "http://www.sadikturan.com"
course = "Python Kursu Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course) # 1.cevap

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10] # 2.cevap

# 3- 'website' içinden com karakterlerini alın.
result = website[-3:] # 3.cevap

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[:15]
result = course[-15:] # 4.cevap

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1] # 5.cevap

print(result)

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis'

# 6- Yukarıda verilen değişkenlerle ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.'
print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}.") # 6.cevap

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
ex = 'Hello world'
ex = ex[0:6] + 'W' + ex[-4:]
print(ex)

# 8- 'abc' ifadesini yan yana üç defa yazdırın.
s = 'abc' * 3 
print(s) # 8.cevap