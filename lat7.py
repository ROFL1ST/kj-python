# buat program untuk menampilkan deret bilangan ganjil
# yang di input batas deret

# deret = int(input("Masukkan batas deret : "))
# print("------------------------------------")

# for i in range(1, deret):
#     print(i*i, end=" ")

# buat program dengan output sebagai berikut menggunakan for
#           Biodata Mahasiswa
# ==========================================
# No     Nama       nilai
# =========================================

nama = ["Danendra", "Endra", "Jezz"]
nilai = [70, 100, 90]
print("Biodata Mahasiswa")
print("===================================")
print("No\t Nama\t Nilai")

for i in range(1, 3):
    print(i, "\t", nama[i], "\t", nilai[i])
print("===================================")
