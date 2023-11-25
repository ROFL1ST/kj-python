# bilangan = int(input("Masukkan Bilangan : "))
# pangkat = int(input("Masukkan pangkat : "))
# hasil = bilangan

# for i in range(pangkat-1):
#     if(pangkat == 0):
#         print("HAI")
#         hasil = 1
#     else:
#         hasil *= bilangan
# print(bilangan, "Pangkat", pangkat, "=", hasil)


# def kali_kartesian(A, B):
#     result = set()
#     for a in A:
#         for b in B:
#             result.add((a, b))
#     return result

# A = {2, 5}
# B = {3,4}
# A_x_B = kali_kartesian(A, B)
# print('A x B =', A_x_B)

# def total(angka):
#     ppn = angka * 0.1
#     service = angka * 0.05
#     total_bayar = angka + ppn + service

#     print(f"Total Pembelian: Rp{angka: 2,.2f}")
#     print(f"PPN (10%): Rp{ppn: 2,.2f}")
#     print(f"Service Charge (5%): Rp{service: 2,.2f}")
#     print(f"Total yang harus dibayarkan: Rp{total_bayar: 2,.2f}")


# val = int(input("Masukkan total pembelian: "))

# total(val)

# def cuan(angka):
#     percent = 0.23
#     profit = angka * percent
#     print(f"Keuntungan tahun ini adalah Rp.{profit: 2,.2f}")

# val = int(input('Masukkan total penjualan tahun ini: '))

# cuan(val)

# def convert_jam(detik):
#     hari = detik // 86400
#     sisa = detik % 86400
#     jam = detik // 3600
#     sisa = detik % 3600
#     menit = sisa//60
#     detik = sisa % 60
#     print(f"Berikut waktu dalam jam, menit, dan detik:")
#     print(f"Hari: {hari}")

#     print(f"Jam: {jam}")
#     print(f"Menit: {menit}")
#     print(f"Detik: {detik}")


# val = int(input("Masukkan waktu dalam detik: "))

# convert_jam(val)

# def persegi(panjang, lebar):
#     luas = panjang * lebar
#     keliling = 2*(panjang + lebar)
    
#     print(f"Persegi panjang dengan panjang = {panjang} cm dan lebar = {lebar} cm mempunyai luas = {luas} cm2 dan keliling = {keliling} cm.")

# input1 = int(input("Masukkan panjang (cm): "))
# input2 = int(input("Masukkan lebar (cm): "))

# persegi(input1, input2)

# def rata_rata(nilai1, nilai2, nilai3):
#     hasil = (nilai1 + nilai2 + nilai3) / 3

#     print("Rata-rata nilai ujian: {:.2f}".format(hasil))

# input1 = int(input("Masukkan nilai ujian 1: "))
# input2 = int(input("Masukkan nilai ujian 2: "))
# input3 = int(input("Masukkan nilai ujian 3: "))

# rata_rata(input1, input2, input3)


# # Fungsi konversi_ke_km
# # [1] Tambahkan parameter yang diperlukan
# def konversi_ke_km(angka):
#     # [2] Konversi argumen ke km dan kembalikan hasilnya.
#     km = angka * 1.6
#     return km
# # Fungsi main
# def main():
#     # [3] Minta pengguna memasukkan jarak dalam mil dalam tipe floabera point
#     mil = float(input('Masukkan jarak dalam mil: '))

#     # [4] Panggil fungsi konversi_ke_km
#     hasil = konversi_ke_km(mil)
    
#     # [5] Tampilkan hasil konversi
    
#     print(f"Jarak dalam km = {hasil:,.2f}")
# main()

# A = [2,3,5,7,11]


# [1] Import module math
import math

# Fungsi hitung_populasi
# [2] Tuliskan parameter-parameter yang diperlukan
# def hitung_populasi(PO, t):
#     # [3] Hitung populasi setelah waktu t. Gunakan fungsi dalam module math.
#     # Bulatkan ke bawah hasil penghitungan (hilangkan nilai desimalnya). Misal: hasil penghitungan 754595.685 maka nilai
#     # yang dikembalikan fungsi ini adalah 754595.
#     P = math.floor(PO * math.exp(0.1 * t))
#     return P
    
    
    
    
    

# # Fungsi main
# def main():
#     # [4] Minta input pengguna untuk populasi awal. Prompt 'Masukkan populasi awal: '
#     awal = float(input("Masukkan populasi awal: "))
    
    
#     # [5] Minta input pengguna untuk waktu. Prompt 'Masukkan waktu dalam tahun: '
#     waktu = float(input("Masukkan waktu dalam tahun: "))
    
    
#     # [6] Hitung populasi setelah waktu t dengan memanggil fungsi hitung_populasi

#     hasil = hitung_populasi(awal, waktu)

#     # [7] Tampilkan populasi akhir: Populasi akhir = <nilai_populasi_akhir>
#     print(f"Populasi akhir = {hasil}")
    
    
# # Panggil fungsi main
# main()

# def energi_kinetik(m,v):
#     return 0.5 * m * (v **  2)

# print(energi_kinetik(80,18))


# import math
# # Fungsi luas_lingkaran
# def luas_lingkaran(r):
#     luas = round(math.pi *r**2, 2)
    
#     return print("Luas lingkaran dengan radius {:.2f} = {:.2f} cm2".format(r, luas))
    
    
# # Fungsi keliling_lingkaran():
# def keliling_lingkaran(r):
#     keliling = round(2* math.pi * r, 2)
#     return print("Keliling lingkaran dengan radius {:.2f} =  {:.2f} cm2".format(r, keliling))


# # Fungsi main
# def main():
#     ruas = float(input("Masukkan radius lingkaran (cm): "))
#     luas_lingkaran(ruas)
#     keliling_lingkaran(ruas)

    
    
# # Panggil fungsi main
# main()


# def kali_kartesian(A,B):
#     list = set()
#     for a in A:
#         for b in B:
#             list.add((a,b))
    
#     return list

# def main():
#     A = {2,5}
#     B = {3,4}
    

#     print(f"A x B = {kali_kartesian(A, B)}")

# main()
    

# A = {2, 3, 4, 5, 7, 11}                               
# for elemen in A:
#     print(f"{elemen}")

# a = 5
# b= 4
# print(b * 2 == a * b / 2)

# def main():
#     pembelian = int(input("Masukkan banyak pembelian: "))
#     total = pembelian * 990000
#     diskon = 0

#     if pembelian < 10:
#         diskon = 0
#     elif pembelian < 20:
#         diskon = total * 0.20
#     elif pembelian < 50:
#         diskon = total * 0.30
#     elif pembelian < 100:
#         diskon = total * 0.40
#     else:
#         diskon = total * 0.50

#     if diskon > 0:
#         print("Diskon = Rp.{:,.2f}".format(diskon))
#         total_setelah_diskon = total - diskon
#         print("Total = Rp.{:,.2f}".format(total_setelah_diskon))
#     else:
#         print("Total = Rp.{:,.2f}".format(total))
    
# main()

# a, b, c= 2, 4,6
# if a >= -1 or a <= b:
#     print(True)
# else:
#     print(False)

# def cek_kecepatan(kecepatan):
#     # Tuliskan kode Anda di bawah.
#     if 20 <= kecepatan <= 60 :
#         print("Kecepatan normal")
#     else:
#         print("Kecepatan tidak normal")
        

# def main():
#     angka1 = int(input("Masukkan angka 1: "))
#     angka2 = int(input("Masukkan angka 2: "))
#     angka3 = int(input("Masukkan angka 3: "))
#     angka_terbesar = max(angka1, angka2, angka3)
#     print(f"Angka terbesar =  {angka_terbesar}")
 
# main()

# def main():
#     gaji = int(input("Masukkan gaji Anda: "))
#     lama_kerja = int(input("Lama bekerja (tahun): "))
#     if gaji <= 3000000 or lama_kerja <= 2:
#         print("Anda tidak terkualifikasi untuk menerima pinjaman!")
#     else:
#         print("Anda terkualifikasi untuk menerima pinjaman!")

# main()

# angka = 2                               
# while angka <= 100:                           
#     print(angka)                            
#     angka += 2

# for i in range(1,11):
#     print(i**2)

# for i in range(50,0, -2):
#     print(i)

# def main():
#     total = 0
#     for i in range(10):
#         angka = int(input("Masukkan angka: "))
#         total += angka
#     print(f"Total = {total}")
    
    
    
# main()

# def main():
#     total = 0
#     counter = 0
#     while True:
#         angka = int(input("Masukkan angka positif (akhiri dengan memasukkan angka negatif): "))
#         rata = 0
#         if counter > 0:
#             rata = total/counter
#         else:
#             rata = 0
#         if angka < 0:
#             print(f"Rata-rata angka yang dimasukkan: {rata}")
#             break
#         total += angka
#         counter += 1

# main()

# def main():
#     angka = int(input("Masukkan sebuah angka: "))
#     for i in range(angka,0,-1):
#         for i_2 in range(i):
#             print("*", end="")
#         print()

# main()


# def main():
#     jumlah_detik = int(input("Masukkan jumlah detik: "))
#     hari = jumlah_detik // 86400
#     sisa = jumlah_detik % 86400
#     jam = sisa // 3600
#     sisa = jumlah_detik % 3600
#     menit = sisa//60
#     detik = sisa % 60
#     if jumlah_detik >= 86400:
#         print(f"{hari} hari {jam} jam {menit} menit {detik} detik")
#     elif jumlah_detik >= 3600:
#         print(f"{jam} jam {menit} menit {detik} detik")
#     elif jumlah_detik >= 60:
#         print(f"{menit} menit {detik} detik")   
#     else:
#         print(f"{detik} detik")




# main()

# def main():
#     angka1 = int(input("Masukkan angka 1: "))
#     angka2 = int(input("Masukkan angka 2: "))
#     total = angka1 + angka2
#     print(f"Jumlah = {total}")
#     pilihan = input("Masukkan y untuk melanjutkan: ")
#     if pilihan == "y":
#         main()
    
# main()

# angka = [1, 2, 3, 4, 5, 6, 7, 8]
# print(angka[::2])

# nilai = [2] * 5 
# print(nilai)

# angka = [1, 2, 3, 4, 5]
# angka[0] = 99
# print(angka)

# ids = [4353, 2314, 2956, 3382, 9362, 3900]
# ids.append(5566)
# print(ids)

# ids = [4353, 2314, 2956, 3382, 9362, 3900]
# ids.insert(5, 4499)
# print(ids)

# def main():
    
#     nama_mhs = ('Budi', 'Dodi', 'Cindi', 'Kiki', 'Beti')
#     nama_list  = list(nama_mhs)
#     for i in range(len(nama_list)):
#         print(nama_list[i])
#     # Tuliskan kode Anda di bawah.
    
# # Panggil fungsi main
# main()

# def kuadrat_list(angka):
#     hasil=[]
#     for i in angka:
#         val= i**2
#         hasil.append(val)
#     return hasil

# def jumlah_list(input_list):
#     ganjil = 0
#     genap = 0
#     for i in range(len(input_list)):
#         if i % 2 == 0:
#             genap += input_list[i]
#         else:
#             ganjil += input_list[i]
#     print(f"Total elemen indeks ganjil:  {ganjil}")
#     print(f"Total elemen indeks genap:  {genap}")


# input_list1 = [1, 2, 3, 4, 5]
# jumlah_list(input_list1)


# mystr = 'yes'
# mystr += 'no'
# mystr += 'yes'
# print(mystr)

# def banyak_huruf_besar(string):
#     hitung=0

#     for i in string:
#         if i.isupper():
#             hitung += 1
#     return hitung


# Fungsi in melakukan validasi password
# def validasi_password(passwd):
#     spesial_karakter = ['$', '@', '#', '%']
    
#     # Variabel-variabel untuk menyimpan hasil pengujian ketentuan. Inisialisasi dengan False.
#     panjang_benar = False
#     ada_digit = False
#     ada_huruf_besar = False
#     ada_huruf_kecil = False
#     ada_spesial_karakter = False
    
# 	# [1] Mulai validasi dengan uji panjang karakter
#     # Untuk menguji adanya digit, huruf besar, huruf kecil, dan spesial karakter, gunakan loop yang mengiterasi passwd
#     # panjang
#     if len(passwd) >= 7 or len(passwd) <= 20:
#         panjang_benar = True
# 	# digit
#     if any(char.isdigit() for char in passwd):
#         ada_digit =  True
#     # besar
#     if any(char.isupper() for char in passwd):
#         ada_huruf_besar = True
#     # kecil
#     if any(char.islower() for char in passwd):
#         ada_huruf_kecil = True
#     # karakter
#     if any(char in spesial_karakter for char in passwd):
#         ada_spesial_karakter = True
    
#     # [2] Jika semua ketentuan terpenuhi tetapkan sebuah varibel untuk nilai kembali dengan True
#     # dan selain itu tetapkan dengan False
#     if panjang_benar and ada_digit and ada_huruf_besar and ada_huruf_kecil and ada_spesial_karakter:
#         return True
#     else:
#         return False

#     # [3] Kembalikan variabel nilai kembali yang didapatrkan dari [2]    
    

# input1 = input("Masukkan password : ")
# validasi_password(input1)

# Program ini meminta input sebuah nama dari pengguna dan menampilkan inisial dari nama tersebut
# def main():
#     # Tuliskan kode Anda di bawah dengan mengikuti petunjuk-petunjuk di bawah
#     inisial = ""
#     # [1] Minta pengguna memasukkan sebuah nama
#     nama = input("Masukkan nama: ")
#     # [2] Gunakan method split untuk memisahkan nama depan dan nama belakang
#     nama_depan, nama_belakang = nama.split()
#     # [3] Tampilkan inisial nama depan dan nama belakang dengan operasi pengindeksan list dan string
#     inisial_depan = nama_depan[0]
#     inisial_belakang = nama_belakang[0]
#     # Anda dapat membayangkan list yang berisi string sebagai nested list.
#     print(f"Inisial nama Anda: {inisial_depan.upper()}. {inisial_belakang.upper()}.")

# # Panggil fungsi main
# main()


# Program ini memroses nilai tiga ujian dari mahasiswa dalam sebuah kelas
# Program meminta pengguna memasukkan jumlah mahasiswa, meminta pengguna memasukkan
# nilai-nilai tiga ujian setiap mahasiswa, dan menampilkan rata-rata dari tiga nilai ujian dari setiap mahasiswa 
# def main():
#     # Variabel JUMLAH_UJIAN
#     JUMLAH_UJIAN = 3
#     # Variabel untuk menyimpan nilai-nilai ujian
#     nilai_ujian = []
    
#     # [1] Minta pengguna memasukkan jumlah mahasiswa 
#     jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    
#     # [2] Buat loop sambil meminta pengguna memasukkan nilai ujian setiap mahasiswa
#     print("=" * 50)
#     for i in range(jumlah_mahasiswa):
#         total_nilai = 0
#         print(f"Masukkan nilai ujian untuk mahasiswa {i + 1}")
#         print("-" * 50)

#         # [2] Gunakan nested loop untuk meminta pengguna memasukkan tiga nilai ujian dari masing-masing mahasiswa
#         for j in range(JUMLAH_UJIAN):
#             nilai = float(input(f"Masukkan nilai ujian ke-{j + 1}: "))
#             nilai_ujian.append(nilai)
#             total_nilai += nilai
        
#         # [3] Hitung rata-rata nilai ujian untuk mahasiswa ini
#         rata_rata = total_nilai / JUMLAH_UJIAN
#         nilai_ujian.append(rata_rata)
#         print("=" * 50)

#     # Menampilkan rata-rata nilai ujian setiap mahasiswa
#     for i in range(jumlah_mahasiswa):
#         print(f"Rata-rata ujian mahasiswa {i + 1}: {nilai_ujian[i * (JUMLAH_UJIAN + 1) + JUMLAH_UJIAN]:.2f}")

# # Panggil fungsi main
# main()


# Program ini mencari karakter yang terbanyak muncul dalam input
# def main():
    
#     # Variabel untuk menyimpan karakter-karakter yang terdapat dapat string yang diinput pengguna
#     karakter_list = []
#     # Variabel untuk menyimpan banyaknya karakter yang terdapat dalam string yang diinput pengguna
#     banyak_karakter = []

#     # Catatan untuk dua variabel di atas:
#     # Misalkan pengguna memasukkan 'ada', maka
#     # karakter_list akan berisi ['a', 'd']
#     # banyak_karakter akan berisi [2, 1]
#     # Yang berarti terdapat 'a' sebanyak 2 dan terdapat 'd' sebanyak 1
    

#     # [1] Minta pengguna masukkan sebuah teks dengan prompt 'Masukkan sebuah teks: ' dan simpan dalam sebuah variabel
#     input_chara = input("Masukkan sebuah teks: ")

#     # [2] Gunakan method lower untuk konversi semua karakter ke huruf kecil. Karena string immutable, Anda harus menugaskan
#     # kembali nilai kembali method ke variabel pada [1]
#     input_chara = input_chara.lower()


#     # [3] Gunakan struktur loop untuk mengterasi string input mulai dari indeks 0 sampai dengan terakhir. 
#     # Di dalam loop ini juga terdapat loop yang mengiterasi karakter_list dan menguji masing-masing karakter dalam karakter_list dengan
#     # karakter dari input_string
#     for i in input_chara:
#         if i.isalpha():
#             if i in karakter_list:
#                 index = karakter_list.index(i)
#                 banyak_karakter[index] += 1
#             else:
#                 karakter_list.append(i)
#                 banyak_karakter.append(1)


#     # [4] Cari jumlah terbanyak pada banyak_karakter dan simpan indeksnya
#     max_counter = max(banyak_karakter)
#     index_max = banyak_karakter.index(max_counter)


#     # [5] Tampilkan karakter terbanyak. Gunakan indeks yang didapat pada [4]        
#     karakter_terbanyak = karakter_list[index_max]
#     print(f"Karakter terbanyak:  {karakter_terbanyak}")

# # Panggil fungsi main
# main()


# import sifat_relasi   # import module sifat_relasi


# # Definisikan himpunan A dan relasi R
# A = {1,2,3,4,5,6}                                     
# R = {(a,b) for a in A for b in A if b % a == 0}       

# # Print R
# print('R =', sorted(R))

# # Print sifat-sifat R
# print('refkleksif: ', sifat_relasi.is_reflexive(R, A)                   )
# print('simetris: ', sifat_relasi.is_symmetric(R, A)                   )
# print('antisimetris: ', sifat_relasi.is_antisymmetric(R, A)               )
# print('transitif: ', sifat_relasi.is_transitive(A,R)                   )
# print()

# import sifat_relasi   # import module sifat_relasi


# # Definisikan himpunan A dan relasi R1, R2, R3, dan R4
# A = {1,2,3,4}                                         
# R1 = {(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)}                                                               
# R2 = {(1,1),(1,2),(2,1),(2,2),(3,3),(4,4)}                                                               
# R3 = {(1,1),(2,2),(3,3),(4,4)}                                                                           
# R4 = {(1,3),(1,4),(2,3),(2,4),(3,1),(3,4)}                                                               

# # Loop for untuk mengiterasi masing-masing relasi
# for i, R in enumerate                                                                                       :

#     # Print masing-masing anggota relasi dan sifatnya.
#     print('R =', sorted(R))

#     # Print sifat-sifat R
#     print('refkleksif: ',                                                   )
#     print('simetris: ',                                                   )
#     print('antisimetris: ',                                                   )
#     print('transitif: ',                                                   )
#     print()

# Definisikan himpunan A dan relasi R1, R2
# A = {2,3,5,7,9}                                       
# R1 = {(a,b) for a in A for b in A if b % a == 0     }   
# R2 = {(a,b) for a in A for b in A if a <= b}           

# # Gabungan R1 dan R2
# R1_u_R2 = R1.union(R2)                                                  
# # Irisan R1 dan R2
# R1_n_R2 =   R1.intersection(R2)                                                
# # R1 - R2
# R1_min_R2 = R1.difference(R2)                                                  
# # R2 - R1
# R2_min_R1 =  R2.difference(R1)                                                 

# # Tampilkan hasil
# print('R1 u R2 =', sorted(R1_u_R2))
# print('R1 n R2 =', sorted(R1_n_R2))
# print('R1 - R2 =', sorted(R1_min_R2))
# print('R2 - R1 =', sorted(R2_min_R1))


# Definisikan himpunan A dan relasi R1, R2
# A = {8,9,10,11}                                       
# R = {(a,b) for a in A for b in A if b % a ==0}        
# R_invers = {(b, a) for (a,b) in R}                                           

# # Tampilkan hasil
# print('R =', sorted(R))
# print('R invers =', sorted(R_invers))


# def get_score():
#     # Buat list kosong untuk menyimpan angka-angka yang dimasukkan pengguna
#     score_list = []

#     while True:
#         # Minta pengguna memasukkan skor berupa angka
#         skor = int(input("Masukkan skor (masukkan angka negatif untuk menyudahi): "))

#         if skor < 0:
#             break  # Akhiri loop jika angka negatif dimasukkan
#         else:
#             score_list.append(skor)  # Tambahkan skor ke dalam list

#     return score_list

# hasil = get_score()
# print(hasil)


# mystr = 'abc' * 3
# print(mystr)

# mystring = 'abcdefg'
# print(mystring[2:5])

# def balik_string(input_string):
#     # [1] Buat sebuah variabel untuk menyimpan string dengan urutan karakter terbalik. Inisialisasi dengan string kosong.
#     reversed_string = ""

#     # [2] Iterasi karakter-karakter dari input string dimulai dari indeks terakhir sampai dengan indeks pertama
#     # Konkatenasi setiap karakter ke variabel yang menyimpan string dengan urutan karakter terbalik.
#     for i in range(len(input_string) - 1, -1, -1):
#         reversed_string += input_string[i]

#     # [3] Print variabel yang menyimpan string dengan urutan karakter terbalik.
#     print(reversed_string)

# val = input("Masukkan : ")
# balik_string(val)


# def main():
#     # Gunakan list berikut untuk mendapatkan string nama bulan
#     lookup_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

#     # [1] Minta input tanggal dalam bentuk hh/bb/tttt dengan prompt 'Masukkan tanggal dalam format hh/bb/tttt: '
#     tanggal_input = input("Masukkan tanggal dalam format hh/bb/tttt: ")

#     # [2] Gunakan method split untuk memisahkan tanggal, bulan, dan tahun dan simpan ke sebuah list
#     tanggal_parts = tanggal_input.split('/')

#     if len(tanggal_parts) == 3:
#         hari, bulan, tahun = tanggal_parts
        
#         # Hapus 0 di depan hari, bulan, dan tahun jika ada
#         hari = hari.lstrip('0')
#         bulan = bulan.lstrip('0')
#         tahun = tahun.lstrip('0')
        
#         # Konversi bulan ke integer
#         bulan = int(bulan)
        
#         # [3] Gunakan struktur seleksi untuk menvalidasi apakah bulan yang dimasukkan antara 1 s.d 12
#         if bulan >= 1 and bulan <= 12:
#             bulan_str = lookup_bulan[bulan - 1]
#             print(f"{hari} {bulan_str} {tahun}")
#         else:
#             print("Anda tidak memasukkan tanggal yang benar.")
#     else:
#         print("Anda tidak memasukkan tanggal yang benar.")

# # Panggil fungsi main
# main()
# Program di atas akan meminta pengguna memasukkan tanggal dalam format "hh/bb/tttt", memisahkan tanggal, bulan, dan tahun, dan kemudian memvalidasi bulan. Jika bulan valid, program akan mencetak tanggal dalam format yang diinginkan. Jika bukan, program akan memberi tahu pengguna bahwa tanggal yang dimasukkan tidak benar.


# def my_list(input_list):
#     count = 0
#     for i in input_list:
#         if "Ruby" in i:
#             count += 1
#     return count

# my_list(["Alan", "Budi", "Jodi"])


# a, b, = 5,4
# print(b * 2 == a * b / 2)

# print("Budi", "Susi", "Jodi", "Dodi", sep="@")

# a, b, c = 2,4,6

# print(a==4 or b> 2)
# print(a >= -1 or a <= b)

# def hitung_imt(berat, tinggi):
#     imt = berat / (tinggi ** 2)
#     return imt

# if x > 100:
#     y = 20
#     z = 40

# mystring = 'abcdefg'
# print(mystring[2:5])

# Program ini menghitung jumlah digit-digit dari angka yang dimasukkan pengguna
# def main():
#     # [1] Minta input ke pengguna
#     angka = input("Masukkan sebuah angka: ")
    
#     # [2] Buat sebuah variabel akumulator
#     jumlah_digit = 0
    
#     # [3] Iterasi karakter-karakter (digit-digit) dalam string angka yang dimasukkan pengguna
#     # dan konversi ke integer untuk mendapatkan representasi integer dari digit
#     for karakter in angka:
#         digit = int(karakter)
#         jumlah_digit += digit
    
#     # [4] Tampilkan jumlah digit dengan teks: "Jumlah digit-digit dari <input_angka_pengguna> = <jumlah_digit>"
#     print(f"Jumlah digit-digit dari {angka} = {jumlah_digit}")

# # Panggil fungsi main
# main()

# # Langkah 1: Membuka File untuk ditulis (modus 'w')
# output_file = open('data.txt', 'w')

# # Langkah 2: Memroses File (Menulis ke File)
# output_file.write('Baris 1\n')
# output_file.write('Baris 2\n')

# # Langkah 3: Menutup File
# output_file.close()

# # Langkah 1: Membuka File untuk dibaca (modus 'r')
# input_file = open('data.txt', 'r')

# # Langkah 2: Memroses File (Membaca dari File) 
# isi_file = input_file.read()

# # Langkah 3: Menutup File
# input_file.close()

# # Tampilkan isi file ke layar
# print(isi_file)

# Program ini menuliskan teks "Bandung", "Jakarta", "Depok" masing-masing dalam satu baris ke file kota.txt
# def main():
#     # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dan referensikan object file ke variabel output_file
#     output = open("kota.txt", "w")
   
#     if not output:
#         print("Gagal membuat file.")
#     else:
#         city = ["Bandung", "Jakarta", "Depok"]
#         for c in city:
#             output.write(c + "\n")
#         output.close()

# main()

    
# Program ini membaca keseluruhan isi file kota.txt
# def main():
#     # Tuliskan kode Anda di bawah.
#     # [1] Tuliskan statement buka file kota.txt untuk dibaca
#     text = open("kota.txt", "r")


#     # [2] Tuliskan statement untuk membaca keseluruhan isi file kota.txt dan simpan isi file dalam variabel isi_file
#     isi = text.read()



#     # [3] Tuliskan statement untuk menutup file kota.txt
#     text.close()



#     # [4] Tuliskan statement untuk mencetak nilai dari variabel isi_file yang menyimpan isi file kota.txt
#     print(isi)


    
# # Panggil fungsi main
# main()

# Program ini menambahkan teks 'Surabaya' dan 'Medan'
# masing-masing dalam satu baris ke file kota.txt
# def main():
#     # [1] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a'
#     output = open("kota.txt", "a")



#     # [2] Tuliskan statement untuk menambahkan teks 'Surabaya' dan 'Medan' ke file kota.txt
#     if not output:
#         print("Gagal membuat file.")
#     else:
#         city = ["Surabaya", "Medan"]
#         for c in city:
#             output.write(c + "\n")
#         output.close()


    
#     # [3] Tuliskan statement untuk menutup file kota.txt



# # Panggil fungsi main
# main()

# Program ini meminta pengguna memasukkan sebuah nama kota
# dan menambahkan nama kota yang dimasukkan tersebut ke file kota.txt
# def main():
    
#     # [1] Tuliskan staement untuk meminta nama kota ke pengguna dengan prompt: "Masukkan nama kota: "
#     input_kota = input("Masukkan nama kota: ")

    
#     # [2] Tuliskan statement untuk membuka file kota.txt untuk ditulis dengan modus 'a' dan referensikan object file ke variabel output_file
#     output = open("kota.txt", "a")

    
#     # [3] Tuliskan statement untuk menulis nama kota yang dimasukkan pengguna dalam baris baru
#     if not output:
#         print("Gagal membuat file.")
#     else:
#         output.write(input_kota + "\n")


#     # [4] Tuliskan statement untuk menutup file
#     output.close()

    
    

    
#     # [5] Tuliskan statement yang menampilkan pesan "Data telah ditambahkan ke file kota.txt."

#     print("Data telah ditambahkan ke file kota.txt.")
    
# # Panggil fungsi main
# main()

# Program ini membaca file menggunakan statement with
# def main():

#     # [1] Buka file kota.txt untuk dibaca dan tugaskan object file ke variabel input_file
#     # dengan statement with. Lalu simpan seluruh isi file ke sebuah variabel bernama isi_file.
#     with open('kota.txt', 'r') as input_file:
#         isi_file = input_file.read()





#     # [2] Tampilkan isi file dengan print
#     print(isi_file)



# # Panggil fungsi main
# main()

# Program ini membaca file kota.txt dan menampilkan isi file
# dengan format: Baris <n>: <isi_file_baris_ke_n>
# def main():
    
#     # [1] Tuliskan statement untuk membuka file kota.txt untuk dibaca dan tugaskan object file ke sebuah variabel
#     with open("kota.txt", "r") as input_file:
#         isi = input_file.readlines()
         
#         for i in range(len(isi)):
#             isi[i] = isi[i].rstrip("\n")
#             print(f"Baris {i + 1}: {isi[i]}")



    
#     # [2] Tuliskan tiga statement untuk membaca tiga baris dari file kota.txt dan menyimpan isinya ke sebuah variabel




    
#     # [4] Hilangkan karakter baris baru pada masing-masing isi baris





#     # [3] Tampikan isi per baris dengan format: Baris <n>: <isi_file_baris_ke_n>




# # Panggil fungsi main
# main()


# Program ini meminta pengguna memasukkan tiga buah angka float
# dan menuliskan keduanya, masing-masing dalam satu baris, 
# ke file angka.txt
# def main():
    
#     # [1] Minta pengguna memasukkan tiga buah angka desimal
#     # Gunakan prompt "Masukkan sebuah angka desimal: " untuk angka pertama
#     # dan prompt "Masukkan sebuah angka desimal lainnya: " untuk angka kedua dan ketiga 
#     number = []
#     # angka1 = float("Masukkan sebuah angka desimal: ")

#     angka = float(input("Masukkan sebuah angka desimal: "))
#     number.append(angka)
#     for i in range(2):
#         angka2 = float(input("Masukkan sebuah angka desimal lainnya: "))
#         number.append(angka2)

    
#     with open("angka.txt", "w") as input_angka:
#         for i in range(len(number)):
#             input_angka.write(str(number[i]) + '\n')
#     input_angka.close()
#     print("Data telah berhasil disimpan dalam file angka.txt.")
    



    
#     # [2] Buka file angka.txt untuk ditulis dan tuliskan angka-angka yang didapat
#     # dari pengguna ke file tersebut masing-masing dalam baris baru.


        
    
#     # [3] Tampilkan pesan "Data telah berhasil disimpan dalam file angka.txt."


    
# # Panggil fungsi main
# main()

# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
# def main():
    
#     # [1] Buka file dengan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
#     # Lalu ambil angka pertama pada baris pertama dan angka kedua pada baris kedua, simpan
#     # angka pada setiap baris isi file masing-masing ke sebuah variabel 
#     with open('angka_float.txt', 'r') as file:
#         data = file.readlines()
#         num = []
#         for i in range(len(data)):
#             if i == 0 or i == 1:
#                 data[i] = data[i].rstrip("\n")
#                 print(f"Baris {i + 1} file angka_float.txt berisi: {data[i]}")
#                 num.append(float(data[i]))
#     file.close()
#     # [4] Hitung hasil perkalian angka pertama dan angka kedua
#     for i in range(len(num)):
#         result = num[0]*num[1]
    
#     print(f"Hasil kali baris 1 dan baris 2 = {round(result, 2)}")


        
#     # [2] Hitung hasi kali dan tampikan sesuai dengan ketentuan program yang diminta






# # Panggil fungsi main
# main()

# Program ini menuliskan angka 1 s.d 100 
# ke file daftar_angka.txt

# [1] Import module random
# import random

# # Definisi fungsi main
# def main():
        
#     # [2] Tuliskan kode untuk membuka file daftar_angka.txt untuk ditulis
#     # Generasi angka acak antara 1 s.d 100 sebanyak 100 angka dengan fungsi randint
#     # dan tulis masing-masing angka ke masing-masing baris pada file daftar_angka.txt.
#     with open("daftar_angka.txt", "w") as file:
       
#         list_number = []
#         for i in range(100):
#             number = random.randint(1, 100)
#             list_number.append(str(number))
#             file.write(list_number[-1])
#             file.write('\n')
#         file.close()







# # [3] Panggil fungsi main            
# main()

# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
# def main():
    
#     # Ikuti petunjuk pada komentar di bawah.
#     # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
#     # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    
    
#     # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
#     # dan variabel akumulator untuk menghitung total penjualan
#     penghitung_baris = 0
#     akumulator = 0
    
    
#     # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
#     with open("sales.txt", "r") as file_sales:
#     # [3] Baca baris pertama isi file dan simpan ke suatu variabel
#         isi_baris = file_sales.readline().strip()
#     # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
#     # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
#     # - inkrementasi variabel penghitung baris
#         while isi_baris != "":
#             akumulator += float(isi_baris)
#             penghitung_baris += 1
#             isi_baris = file_sales.readline().strip()
    

    
    
    
    

    
    
    
    
#     # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
#     # dan tampilkan hasilnya.    
#     if penghitung_baris != 0 :
#         rata = akumulator / penghitung_baris
#         print(f"Rata-rata penjualan: {rata:,.2f}")
#     else:
#         print("Kosong TOT")


# # Panggil fungsi main
# main()


# def main():
    
#     # Ikuti petunjuk pada komentar di bawah.
#     # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
#     # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    
    
#     # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
#     # dan variabel akumulator untuk menghitung total penjualan
#     penghitung_baris = 0
#     akumulator = 0
    
    
#     # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
#     with open("sales.txt", "r") as file_sales:
#     # [3] Baca baris pertama isi file dan simpan ke suatu variabel

#     # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
#     # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
#     # - inkrementasi variabel penghitung baris
#         for isi_baris in file_sales:
#             akumulator += float(isi_baris.strip())
#             penghitung_baris += 1

    

    
    
    
    

    
    
    
    
#     # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
#     # dan tampilkan hasilnya.    
#     if penghitung_baris != 0 :
#         rata = akumulator / penghitung_baris
#         print(f"Rata-rata penjualan: {rata:,.2f}")
#     else:
#         print("Kosong TOT")


# # Panggil fungsi main
# main()

# angka = [1, 2, 3, 4, 5]

# with open('daftar_angka.txt', 'w') as output_file:
#     output_file.writelines(angka)

# Program ini menuliskan sebuah list ke file list_angka.txt
# def main():
    
#     angka = [234, 694, 123, 789, 923, 674, 534]
    
#     # [1] Tuliskan kode untuk menuliskan list yang direferensikan oleh variabel angka
#     # ke file list_angka.txt
#     with open("list_angka.txt", "w") as op:
#         for i in angka:
#             op.write("%d\n" % i)


    
    
    
    
# # Panggil fungsi main
# main()

# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
# def main():
    
#     # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
#     rata_rata = 0.0
#     nilai_tertinggi = 0.0
#     nilai_terendah = 0.0
    
#     # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca 
#     # dan simpan isinya ke sebuah list
#     with open("daftar_nilai.txt", "r") as ip:
#         nilai = [float(line.strip()) for line in ip]

            


        
#     # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
#     # dari list




    
#     # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
#     if nilai:
#         total = sum(nilai)
#         jumlah = len(nilai)
#         rata_rata = total / jumlah
#         nilai_tertinggi = max(nilai)
#         nilai_terendah = min(nilai)



    
    
#     # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.
#     print(f"Rata-rata nilai ujian: {rata_rata:.2f}")
#     print(f"Nilai ujian tertinggi: {nilai_tertinggi}")
#     print(f"Nilai ujian terendah: {nilai_terendah}")



    
    
# # Panggil fungsi main()
# main()

# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
# def main():
#     # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
#     jumlah = int(input("Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? "))



#     # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file
#     # nilai_mahasiswa.txt
#     with open("nilai_mahasiswa.txt", "a") as inputt:
#         for i in range(jumlah):
#             print(f"Masukkan record nilai mahasiswa ke {i+1}")
#             nama = input("Nama: ")
#             nilai = float(input("Nilai: "))
#             inputt.write(nama + "\n")
#             inputt.write(str(nilai) + "\n")
#             print()
#     inputt.close()
            





# # Panggil fungsi main
# main()

# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
# def main():

#     # [1] Buka file nilai_mahasiswa.txt dengan statement with untuk dibaca
#     # Pada body statement with:
#     # - Gunakan loop while untuk membaca field-field dari semua record
#     # - Tampilkan record dengan tampilan:
#     #           Nama: <nama_mahasiswa>
#     #           Nilai: <nilai_mahasiswa>
#     with open("nilai_mahasiswa.txt", "r") as file:
#         lines = file.readlines()
#         i = 0
#         while i < len(lines):
#             nama = lines[i].strip()
#             i += 1
#             nilai = lines[i].strip()
#             i += 1
#             print(f"Nama: {nama}\nNilai: {nilai}")
#             print()

# # Panggil fungsi main
# main()

# try:
#     x = float('abc123')
#     print('Konversi berhasil.')
# except IOError:
#     print('Kode ini menyebabkan IOError.')
# except ValueError:    
#     print('Kode ini menyebabkan ValueError.')

# try:
#     y = int('x1010')
#     print(y)
# except IOError:
#     print('Kode ini menyebabkan IOError.')
# except ZeroDivisionError:
#     print('Kode ini menyebabkan ZeroDivisionError.')
# except:
#     print('Sebuah error terjadi.')

# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
# def main():
#     # [1] Tuliskan statement try/except
#     # Pada body klausa try:
#     #     - Minta dua angka ke pengguna
#     #     - Lakukan pembagian
#     # Pada body klausa except untuk ValueError
#     #     - Tampilkan pesan: "Nilai yang diinput salah."
#     # Pada body klausa except untuk ZeroDivisionError
#     #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
#     try:
#         num1 = int(input("Masukkan sebuah angka yang akan dibagi: "))
#         num2 = int(input("Masukkan sebuah angka pembagi: "))
#         result = num1 / num2
#         print(f"{num1} dibagi dengan {num2} sama dengan {result}")
#     except ValueError:
#         print("Nilai yang diinput salah.")
#     except ZeroDivisionError:
#         print("Tidak dapat membagi dengan nol.")
# # Panggil fungsi main
# main()

# def main():
#     try:
#         # [1] Minta pengguna memasukkan nama file
#         nama_file = input("Masukkan nama file: ")

#         # [2] Buka file dengan statement with dan simpan object file ke variabel
#         with open(nama_file, "r") as file:
#             # [3] Inisialisasi variabel untuk menghitung nilai
#             total_nilai = 0
#             jumlah_nilai = 0
#             nilai_tertinggi = float('-inf')
#             nilai_terendah = float('inf')

#             # [4] Loop untuk membaca setiap baris dan menghitung nilai
#             for line in file:
#                 try:
#                     nilai = float(line.strip())
#                     total_nilai += nilai
#                     jumlah_nilai += 1
#                     nilai_tertinggi = max(nilai_tertinggi, nilai)
#                     nilai_terendah = min(nilai_terendah, nilai)
#                 except ValueError:
#                     raise ValueError("Terdapat data non numerik dalam file.")

#             # [5] Hitung rata-rata dan tampilkan hasilnya
#             if jumlah_nilai > 0:
#                 rata_rata = total_nilai / jumlah_nilai
#                 print(f"Rata-rata nilai: {rata_rata:.2f}")
#                 print(f"Nilai tertinggi: {nilai_tertinggi:.2f}")
#                 print(f"Nilai terendah: {nilai_terendah:.2f}")
#             else:
#                 print("File tidak berisi nilai numerik.")

#     except FileNotFoundError:
#         print("File tidak ditemukan.")
#     except ValueError as e:
#         print(str(e))
    
# # Panggil fungsi main
# main()

# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
# def main():

#     # Variabel sebagai penanda jika nama mahasiswa yang dicari ditemukan
#     found = False
    
#     try:
#         # [1] Tuliskan statement untuk meminta nama file ke pengguna
#         # Gunakan prompt: 'Masukkan nama file: '
#         nama_file = input("Masukkan nama file: ")

#         # [2] Tuliskan staement untuk membuka file dengan nama file yang diberikan pengguna
#         # Anda dapat menggunakan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
#         with open(nama_file, "r") as file:
#             # [3] Tampilkan pesan: "File <nama_file> berhasil dibuka.". Tambahkan baris baru.
#             print(f"File {nama_file} berhasil dibuka.")
#             print()

            
#             # [4] Tuliskan statement untuk meminta nama mahasiswa yang ingin dicari
#             # Gunakan prompt: 'Masukkan nama mahasiswa yang ingin dicari: '
#             nama_siswa = input("Masukkan nama mahasiswa yang ingin dicari: ")

#             # [5] Tuliskan statement untuk membaca baris pertama dari file (nama mahasiswa).
#             line = file.readline()
            
#             # [6] Tuliskan loop while yang mengiterasi baris-baris file 
#             while line:

#                 # [7] Tuliskan statement untuk membaca nilai mahasiswa
#                 nilai = float(file.readline().strip())
                

#                 # [8] Tuliskan statement untuk menghilangkan baris baru pada nama mahasiswa dan nilai mahasiswa
#                 # Gunakan rstrip.
#                 nama_mahasiswa = line.rstrip()
                
#                 # [9] Tuliskan struktur seleksi yang menentukan apakah nama mahasiswa cocok
#                 # dengan nama yang ingin dicari
#                 if nama_siswa == nama_mahasiswa:
#                     # [10] Jika nama_mahasiswa sama dengan nama yang ingin dicari
#                     # Tampilkan Nama dan Nilai
#                     print(f"Nama Mahasiswa: {nama_mahasiswa}")
#                     print(f"Nilai: {nilai}")

#                     # [11] Tetapkan nilai variabel penanda found dengan True
#                     # Ini karena mahasiswa ditemukan
#                     found = True

#                 # [12] Tuliskan statement membaca baris berikutnya
#                 line = file.readline()


#     # [13] Tuliskan klausa except FileNotFoundError
#     # Pada body klausa except ini tampilkan: File <nama_file> tidak ditemukan.
#     except FileNotFoundError:
#         print(f"File {nama_file} tidak ditemukan.")
        
#     # [14] Tuliskan klausa else
#     # Pada body klausa else tuliskan struktur seleksi jika found tidak sama dengan True
#     # tampilkan pesan: "Nama <nama yang dicari> tidak ditemukan."
#     else:
#         if not found:
#             print(f"Nama {nama_siswa} tidak ditemukan.")
                    
# # Panggil fungsi main
# main()

# def f(x):
#     return 2*x+1                                             


# S = {-1, 0, 2, 4, 7} 

# # Buat tabel pemetaan
# print(f'| {"x":^5s} | {"f(x)":^5s} |')
# for x in sorted(S):
#     y = f(x)                                              
#     print(f'| {x:5d} | {y:5d} |')

# print()


# import sympy

# # Tetapkan x sebagai sebuah simbol
# x = sympy.Symbol('x')

# # Definisikan f dengan formula yang mengandung simbol x
# f = x**2+1                                            

# # Tetapkan Domain
# A = {2, 4, 6, 8, 10                                    }

# # Print nilai-nilai f
# for i in A:
# #Mensubtitusi simbol x pada fungsi f dengan nilai i dan mengevaluasi f
#     y = f.subs(x, i)                                      
#     print(f'f({i}) = {y}')

# print()


# import sympy

# # Tetapkan x , y sebagai sebuah simbol
# x, y = sympy.symbols("x y")

# # Gunakan fungsi solve pada modul sympy untuk mencari fungsi invers dari suatu fungsi


# # Tampilkan hasilnya
# print([{x: sympy.solve(2*x - y, x)[0]}])


# import sympy

# # Tetapkan x sebagai sebuah simbol
# x =  sympy.symbols("x")                                                 

# # Definisikan fungsi f dan g
# f =  x**2+1                                
# g =  x+2                                                 

# # Gunakan fungsi compose pada modul sympy untuk mencari komposisi dari 2 buah fungsi
# print("f o g = ",     sympy.compose(f,g)                                              )    
# print("g o f = ",            sympy.compose(g,f)                                        )    
