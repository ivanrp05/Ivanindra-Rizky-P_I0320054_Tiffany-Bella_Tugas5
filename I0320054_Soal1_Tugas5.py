#Mulai
print("Soal 1")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Ditanya :")
print(" Buatlah program sederhana yang dapat menyapa pengunjung hotel, dengan ketentuan :")
print("- Program harus dapat menerima input nama dan jenis kelamin pengguna program")
print("- Program menggunakan percabangan")
print("- Program wajib memberikan output kepada pengguna berupa kalimat 'Selamat Datang' ")
print("- Titik-titik di atas diisi dengan nama dan jenis kelamin pengguna program ")
print("")
print("===========================")
print("")
print("Jawab :")
print("")
#Untuk ini dikasih 2 pilihan nama :
#"Asep Gumilar","Edy Sujarwo","Lulut" untuk laki laki
#"Sulastri","Suyati" untuk perempuan
#"Saleh" untuk abang abang cucok wwkwkw
print("Selamat datang di Hotel Krusty Krab")
print("")
print("Dimana motto kami adalah :"
      "'Kami tidak akan pernah menolak permintaan pelanggan meskipun permintaannya aneh aneh'")
print("")
print("Apakah anda sudah memesan kamar sebelumnya?")
#Note, pada saat input nama jangan lupa tambahkan spasi
#atas nama : Asep Gumilar instead of atas nama :Asep Gumilar
x = str(input("Saya sudah melakukan reservasi atas nama :"))
if x == " Asep Gumilar" :
    print("Selamat datang Tuan", x , ",", "Berikut adalah kunci kamar anda, semoga anda dapat menikmati pelayanan kami")
elif x == " Edy Sujarwo" :
    print("Selamat datang Tuan", x , ",", "Berikut adalah kunci kamar anda, semoga anda dapat menikmati pelayanan kami")
elif x == " Lulut" :
    print("Selamat datang Tuan", x , ",", "Berikut adalah kunci kamar anda, semoga anda dapat menikmati pelayanan kami")
elif x == " Sulastri" :
    print("Selamat datang Nyonya", x , ",", "Berikut adalah kunci kamar anda, semoga anda dapat menikmati pelayanan kami")
elif x == " Suyati" :
    print("Selamat datang Nyonya", x , ",", "Berikut adalah kunci kamar anda, semoga anda dapat menikmati pelayanan kami")
#Bonus hehehe
elif x == " Saleh" :
    print("Halo abang saleh, cucok ah ")
    print("Canda mas / mbak hehe, sebatas hiburan belaka dikala banyak tugas :) ")
else :
   print("Maaf anda belum melakukan pemesanan, silahkan melakukan pemesanan di meja sebelah")
   print("Terima kasih")

print("Selesai")
input("Klik enter untuk kembali")



