# # Fungsi ini mencari nilai maksimum dari sebuah list secara rekursif
# def maksimum_rekursif(data):
#     # Tuliskan kode Anda di bawah.
#     # [1] Gunakan statement if bersarang untuk mencari nilai maksimum
#     # [2] Statement if bagian pertama memastikan jumlah data ada lebih dari 1 elemen
#     # [3] Statement if bagian kedua (didalam if bagian pertama) menentukan apakah 
#     # elemen pertama list lebih besar dari elemen lainnya
#     if len(data) > 1:
#         maksimum_sisa = maksimum_rekursif(data[1:])
#         return data[0] if data[0] > maksimum_sisa else maksimum_sisa
#     else:
#         return data[0]

    
# def kali(x, y):
#     if y == 0:
#         return 0
    
#     else:
#         return x+ kali(x,y -1)

        
# def binary_search_rekursif(num, data):
#     if len(data) == 0:
#         return -1
#        # Jika data tidak kosong, dapatkan indeks tengah dari data
#     mid_index = len(data) // 2
#     # Struktur seleksi:
#     # 1. Jika elemen tengah sama dengan num kembalikan indeks tengah
#     if data[mid_index] == num:
#         return mid_index
#     # 2. Jika elemen tengah lebih besar, lakukan pemanggilan rekursif terhadap paruh atas data
#     elif data[mid_index] > num:
#         return binary_search_rekursif(num, data[:mid_index])
#     # 3. Jika elemen tengah lebih kecil, lakukan pemanggilan rekursif terhadap paruh bawah data
#     else:
#         result = binary_search_rekursif(num, data[mid_index + 1:])
#         return -1 if result == -1 else mid_index +1 + result

# Fungsi sortir menerima argumen list dan
# mengembalikan list yang tersortir
# def sortir(data):
#     # [1] Tuliskan kode algoritma penyortiran di bawah
#     nilai = len(data)
#     for i in range(nilai):
#         for j in range(0, nilai - i - 1):
#             if data[j] > data[j + 1]:
#                 data[j], data[j +1] = data[j+1], data[j]
#     return data
    
    
    

# # Fungsi median menerima argumen sebuah list
# # dan mengembalikan nilai median dari data dalam list tersebut
# def median(data):
#     # [2] Gunakan fungsi sortir untuk menyortir data
#     # [2] Gunakan fungsi sortir untuk menyortir data
#     data_sortir = sortir(data)
    
#     # [3] Hitung median dengan dua kondisi untuk jumlah data genap dan jumlah data ganjil
#     n = len(data_sortir)
#     if n % 2 == 0:
#         # Jumlah data genap
#         mid1 = data_sortir[n // 2 - 1]
#         mid2 = data_sortir[n // 2]
#         return (mid1 + mid2) / 2
#     else:
#         # Jumlah data ganjil
#         return data_sortir[n // 2]
    

# Fungsi bantu untuk mencari indeks dari nilai minimum dalam data
# Fungsi ini mengembalikan indeks nilai minimum dari data
# def indeks_minimum(data):
#     # [1] Tuliskan kode untuk mencari indeks nilai minimum
#     # dan kembalikan indeks tersebut.
#     mid_index  = 0
#     for i in range(1, len(data)):
#         if data[i] < data[mid_index]:
#             mid_index =i
#     return mid_index





# # Fungsi penyortiran seleksi secara rekursif
# def selection_sort_rekursif(data):
    
#     # [2] Base Case: Data kosong atau hanya mempunyai satu elemen
#     # Tidak perlu sortir, kembalikan data apa adanya
#     if len(data) <= 1:
#         return data
    


        
#     # [3] Recursive Case: Data dengan dua atau lebih elemen
#     # Cari indeks nilai minimum dan dapatkan nilai minimum
#     # Konkatenasi list berisi nilai minimum dengan list berisi data dengan nilai minimum dihilangkan
#     min_index = indeks_minimum(data)
#     min_value = data[min_index]

#     return [min_value] + selection_sort_rekursif(data[:min_index] + data[min_index +1:])



# from segitigasiku import luas, keliling
# # Fungsi main menguji module 
# def main():
    
#     # [2] Minta pengguna untuk memasukkan alas dan tinggi
#     a = int(input("Masukkan panjang alas (cm): "))
#     t = int(input("Masukkan tinggi (cm): "))

    
#     # [3] Hitung luas dan keliling dengan menggunakan fungsi pada module
#     luas_segitiga = luas(a,t)
#     keliling_segitiga = keliling(a,t)

    
#     # [4] Tampilkan luas dan keliling dengan presisi 2 desimal
#     print(f"Luas segitiga: {luas_segitiga:.2f} cm2")
#     print(f"Keliling segitiga: {round(keliling_segitiga, 2)} cm")


# # Panggil fungsi main
# main()



# [1] Impor module statistik yang Anda upload
# from statistik import mean, median, variance, standard_deviation


# # Fungsi main menggunakan module statistik
# # dan menampilkan statistik dari data dalam sebuah file
# def main():
#     try:
#         # [2] Minta user memasukkan nama file yang berisi data
#         # dengan prompt: 'Masukkan nama file: '
#         filename = input('Masukkan nama file: ')

#         # [3] Struktur try/except untuk error file tidak ditemukan
#         # dan file berisi data non numerik
#         try:
#             with open(filename, 'r') as file:
#                 # Baca isi file dan ubah menjadi list of float
#                 data = [float(line.strip()) for line in file]

#                 # Gunakan fungsi-fungsi pada module yang Anda tulis
#                 # untuk mendapatkan nilai mean, variansi, standard deviasi, median, dan modus
#                 mean_val = mean(data)
#                 variance_val = variance(data)
#                 std_deviation_val = standard_deviation(data)
#                 median_val = median(data)

#                 # Tampilkan nilai-nilai tersebut dengan presisi dua desimal
#                 print(f"Mean dari data: {mean_val:.2f}")
#                 print(f"Variansi dari data: {variance_val:.2f}")
#                 print(f"Standar Deviasi dari data: {std_deviation_val:.2f}")
#                 print(f"Median dari data: {median_val:.2f}")

#         except FileNotFoundError:
#             print(f"File {filename} tidak ditemukan.")
        
#         except ValueError:
#             print(f"File {filename} berisi data non-numerik.")

#     except Exception as e:
#         print(f"Terjadi kesalahan: {str(e)}")
  


    
#     # [3] Struktur try/except untuk error file tidak ditemukan
#     # dan file berisi data non numerik
#     # Baca isi file dan gunakan fungsi-fungsi pada module yang Anda tulis
#     # untuk mendapatkan nilai mean, variansi, standard deviasi, median dan modus.
#     # Dan tampilkan nilai-nilai tersebut dengan presisi dua desimal.








        
# # Panggil fungsi main
# main()