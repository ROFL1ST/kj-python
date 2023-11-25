# listA = [1, 2, 3, 4]
# setA = {29,8,7}

# listA.append(999)
# listA.append(777)

# # set
# setA.add(77)
# setA.add(88)
# print("Sebelum")
# print(f"List\t: {listA}")
# print(f"Set\t: {setA}")
# # Menggabungkan List dan Set dengan menggunakan .extend()
# listA.extend(setA)
# print("\nSesudah")
# print(f"List\t: {listA}")


# nilai = [1,2,3,4]
# print(nilai[3])
# nilai2= (80,90,100)


# kata = input("Masukkan kata : ")
# print('Hasil nya [:]', kata[:])
# print("Hasilnya [:]", kata[5:])

# kalimat = input("Masukkan input : ")
# dibalik = kalimat[::-1]
# if kalimat== dibalik:
#     print (f"Kalimat {kalimat} palindrom")
# else:
#     print (f"Kalimat {kalimat} bukan palindrom")

# def pal(w):
#     kata = str(w)[::-1]

#     if str(w) == kata:
#         return True
#     return False


# K = input("Masukkan kata : ")
# print(pal(K))

# X = input("Masukkan kata/kalimat : ")
# pal = True
# panjangX = len(X)
# for i in range(panjangX//2):
#     if X[i] != X[-i - 1]:
#         pal = False
#         break
#     if pal:
#         print("Iya, itu palindrome.")

#     else:
#         print("Tidak, bukan palindrome.")

listSiswa = []


def pilihanNya():
    print("\n Silahkan pilih menu : ")
    print("=========================")
    print("1. Masukkan data")
    print("2. Logout")
    print("=========================")
    pil = int(input("Masukkan pilihan anda : "))
    return pil


def masukkanData():
    siswa = {}
    masNPM = input("Masukkan NPM : ")
    siswa['npm'] = masNPM
    nama = input("Masukkan nama : ")
    siswa['nama'] = nama
    tglLahir = input("Masukkan tanggal lahir : ")
    siswa['tgl_lahir'] = tglLahir
    alamat = input("Masukkan alamat : ")
    siswa['alamat'] = alamat
    listSiswa.append(siswa)

while True:
    pil=pilihanNya()
    if pil==2:
        break
    elif pil==1:
        jalankan = masukkanData()
    else:
        continue

print(listSiswa)
    
    
