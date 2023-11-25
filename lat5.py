# buat lah program untuk menentukan grade nilai dengan ketentuan :
# 80-100 dapat Aa, 70-79 dapat B, 55-69 dapat C, 45-54 data D, 0-44 dapat E
# yang di input nama dan nilai dengan keluaran : Grade sesuai nilai yang di input

nama = input("Masukkan nama : ")
nilai = float(input("Masukkan niali : "))

try:
    if 90 <= nilai <= 100:
        print("A")
    elif 70 <= nilai <= 89:
        print("B")
    elif 50 <= nilai <= 69:
        print("C")
    elif 1 <= nilai <= 49:
        print("D")
    elif nilai == 0:
        print("F")
    else:
        print("Nilai tidak valid!")
except:
    print("Kesalahan")
     