import math

A = int(input("Masukkan sisi 1 : "))
B = int(input("Masukkan sisi 2 : "))
C = int(input("Masukkan sisi 3 : "))

def hitung_jari_jari_lingkaran():
    S = 1/2 * (A + B + C)
    Y = (A * B * C) / 4 * (math.sqrt(S * (S - A) * (S - B) * (S - C)))
    L = 3.14 * Y * Y
    print("jari-jari lingkaran adalah : ", Y, "\n", "luas lingkaran luar adalah : ", L)
    
hitung_jari_jari_lingkaran()