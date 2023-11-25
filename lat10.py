import statistics
inputan = input("Masukkan deret bilangan (Pisahkan dengan koma) : ")
data  = []
for i in inputan.split(","):
    data.append(int(i))

# # rata = statistics.mean(data)
# # tengah = statistics.median(data)
# # print(f"Data :{data}")
# # print(f"Rata :{rata}")
# # print(f"Nilai Tengah :{tengah}")

# # data = [4,1,5,20,10]
# # data.sort()
# # print(data)

# def nilai_tengah(deret):
#     deret.sort()
#     n= len(deret)
#     i_tengah = n//2

#     if n%2 == 1:
#         return deret[i_tengah]
#     else:
#         return (deret[i_tengah-1]+deret[i_tengah])/2
# print(f"Data :{data}")
# print(f"Nilai Tengah : {nilai_tengah(data)}")

# def nilaiTerbanyak(deret):
#     muncul = {}
#     for i in deret:
#         if i in muncul:
#             muncul[i] += 1
#         else:
#             muncul[i] = 1
    
#     bilanganTerbesar = list(muncul.keys())[0]
#     for i in muncul.keys():
#         if muncul[i] > muncul[bilanganTerbesar]:
#             bilanganTerbesar = i
    
#     return bilanganTerbesar

print(f"Data: {data}")
print(f"Bilangan Terbanyak: {statistics.mode(data)}")