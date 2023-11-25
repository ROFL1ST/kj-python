# seorang pegawai akan mendapat bonus 15% jika berhasil
# menjual produk di toko di atas harga toko
# beri pesan selamat jika berhasil jika tidak beri pesan coba terus

harga_barang = int(input("Masukkan harga barang : "))

harga_jual = int(input("Masukkan harga jual : "))
pegawai = "danen"

if (harga_barang < harga_jual):
    bonus = harga_jual*0.15
    print("Selamat", pegawai, "anda mendapatkan bonus sebesar Rp.", bonus)
else:
    print("Coba lagi")
