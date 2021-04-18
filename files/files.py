# Doşya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu.
#       ** Dosyayı konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file = open("C:/users/Win10/Desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf8')
# file.write("Mehmet Alper")
# file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
#                       Varolan içeriğe ekleme yapar.

# file = open("newfile.txt","a",encoding='utf8')
# file.write("\nMehmet Alper")
# file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt","x",encoding='utf8')

# "r": (Read) okuma. varsayılan. Dosya konumda yoksa hata verir.