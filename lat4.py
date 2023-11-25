# buat program untuk membandingkan dua buah bilangan
# mis = x dan y
x=int(input("Masukkan nilai x  : "))
y=int(input("Masukkan nilai y : "))

# if(x>y):
#     print(x, "Lebih besar dari", y)
# elif(x<y):
#     print(x, "Lebih kecil dari", y)
# else:
#     print(x, "sama dengan", y)


# nested
if(x>y):
    print(x, "Lebih besar dari", y)
else:
    if(x<y):
        print(x, "lebih kecil dari", y)
    else:
        print(x, "sama dengan", y)