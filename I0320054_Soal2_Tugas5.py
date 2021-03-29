#Mulai
print("Soal 2")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Ditanya :")
print("Buatlah sebuah program yang dapat merubah/mengkonversi nilai input berupa angka")
print("menjadi huruf yang akan digunakan untuk grading, selain itu program harus dapat memunculkan nama pengguna.")
print("")
print("===========================")
print("")
print("Jawab :")
print("")
print("Selamat datang di tempat konversi nilai")
print("Siapakah nama anda?")
x = input(str("Nama saya adalah :"))
print("Baik saudara", x ,",","Silahkan masukkan nilai anda. ")
y = int(input("Nilai saya adalah :"))
if y < 60 :
    print("Halo",x,"! ,Nilai anda adalah E")
    print("Tuh kan nilai kamu E, ibu sita hp kamu!")
elif 60 <= y <= 64 :
    print("Halo",x,"! ,Nilai anda adalah C")
elif 65 <= y <= 69 :
    print("Halo",x,"! ,Nilai anda adalah C+")
elif 70 <= y <= 74 :
    print("Halo",x,"! ,Nilai anda adalah B")
elif 75 <= y <= 79 :
    print("Halo",x,"! ,Nilai anda adalah B+")
elif 80 <= y <= 84 :
    print("Halo",x,"! ,Nilai anda adalah A-")
#Kenapa A-? kenapa ga A biasa saja?
elif 85 <= y <= 100 :
    print("Halo",x,"! ,Nilai anda adalah A")
    print("Orang tuamu pasti bangga sekali nak")
else :
    pass

print("Selesai")
input("Klik enter untuk selesai")





