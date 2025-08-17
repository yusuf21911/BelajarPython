# Input pengguna
nama = input("Masukkan nama Anda: ")
usia = input("Masukkan usia Anda: ")


print(nama, "berusia", usia, "tahun")

# Cek Tipe Data dari masing- masing INPUT
print("Tipe data nama:", type(nama))
print("Tipe data usia:", type(usia))

#Ambil input harga dan jumlah dari pengguna
#Perhatikan input ini masih dalam bentuk string
harga_produk = input("Masukkan harga barang:(misal: 10000) ")
jumlah_pesanan = input("Masukkan jumlah pesanan: (misal: 2) ")

#Konversi String input menjadi angka agar bisa dihitung
harga_produk = int(harga_produk)
jumlah_pesanan = int(jumlah_pesanan)

# Hitung total harga
total_harga = harga_produk * jumlah_pesanan

#Tampilkan hasil
print("Total harga:", total_harga)
