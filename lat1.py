# buat program untuk menentukan kelulusan mahasiswa 
# variabel yang di input adalah nama dan nilai

nama = input("Masukkan nama : ")
nilai = int(input("Masukkan nilai : "))

if (nilai > 60):
    print("selamat", nama, "anda dinyatakan lulus")
else:
    print("Anda tidak lulus")


