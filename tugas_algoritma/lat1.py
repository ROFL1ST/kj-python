# def tampilkan_angka(i):
#     print("pengulangan ke-{i}")


# angka = int(input("Masukkan angka pengulangan : "))
# tampilkan_angka(angka)

# def kali(a,b):
#     if(b == 0):
#         return 0
#     else:
#         return a+kali(a,b-1)

# angka1 = int(input("Masukkan nilai A : "))
# angka2 = int(input("Masukkan nilai B : "))

# print(angka1, "X", angka2, " = ", kali(angka1, angka2))

# def pangkat(x,y):
#     if(y==0):
#         return 1
#     else:
#         return x*pangkat(x,y -1)

# bil = int(input("Masukkan angka : "))
# pang = int(input("Masukkang pangkat : "))

# print(bil, " ^ ", pang, " = ", pangkat(bil, pang))

# def factorial(n):
#     if(n == 0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# angka = int(input("Masukkan angka : "))
# print(angka, "! = ", factorial(angka))

# def fibonacci(n):
#     if(n == 0):
#         return 0
#     elif(n == 1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)


# angka = int(input("Masukkan angka : "))
# print(angka, "Deret pertama fibonacci")
# for i in range(angka):
#     print(fibonacci(i), end=" ")

def kalkulasi(a, b):
    while b != 0:
        angka1 = a // b
        angka2 = a % b
        print(f"{a} = {angka1} * {b} + {angka2}")
        a = b
        b = angka2
    
angka1 = int(input("Masukkan A : "))
angka2 = int(input("Masukkan B : "))
print(kalkulasi(angka1, angka2))

if(angka2 == 1):
    print("B dapat digunakan sebagai kunci")
else:
    print("B tidak dapat digunakan sebagai kunci")
# print(20 % 8)
