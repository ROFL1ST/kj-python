# input1 = int(input("Masukkan A : "))
# input2 = int(input("Masukkan B : "))

# def kalkulasi(a, b):
#     hasil = 0
#     if(b == 0):
#         print("Masukkan angka diatas 0")
#         return print(a)
#     else:
#         while b != 0:
#             angka1 = a // b
#             angka2 = a % b
#             print(f"{a} = {angka1} * {b} + {angka2}")
#             a = b
#             b = angka2
#             hasil = a
#             # return print(b)
#         if(hasil == 1):
#             print(input2, "dapat digunakan sebagai kunci")    
#         else:
#             print(input2, "tidak dapat digunakan sebagai kunci")
        


# # print(kalkulasi(angka1, angka2))
# kalkulasi(input1, input2)

# # print(20 % 8)
    

# cek bilangan prima

# bil = int(input("Masukkan bilangan : "))
# def prima(angka):

data = ["Danen", "Endra", "Jezz", "Hai"]
print("Isi data mahasiswa adalah {}".format(data[3]))
print("Semua data : ada {} orang".format(len(data)))

for maha in data:
    print(maha)