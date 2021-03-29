#Mulai
print("Exercise 5.3")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
#Penggunaan if untuk 3 kasus dan selebihnya
#input bilangan
print("Masukkan koordinat! ")
print("")
x = int(input("Masukkan nilai x : "))
y = int(input("Masukkan nilai y : "))
info = "Koordinat (" + str(x) + "," + str(y) + ") berada pada kuadran "
#memeriksa nilai x dan y
if x > 0 :
    print(info + "I")
elif x < 0 and y > 0 :
    print(info + "II")
elif x < 0 and y < 0 :
    print(info + "III")
elif x > 0 and y < 0 :
    print(info + "IV")
elif x == "Saya tersesat" :
    print(" Segera berserah diri kepada Tuhan")
else :
    pass
print("")
print("Selesai")
print("")
input("Klik enter untuk kembali :")
