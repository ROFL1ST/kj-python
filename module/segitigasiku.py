import math

def luas(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling(alas, tinggi):
    sisimiring = math.sqrt(alas**2 + tinggi**2)
    return alas + tinggi +sisimiring
