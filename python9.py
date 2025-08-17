#Data
harga_kopi = int(input("Masukkan harga kopi: "))
jumlah_kopi  = int(input("Masukkan jumlah kopi: "))

harga_donat = int(input("Masukkan harga donat: "))
jumlah_donat = int(input("Masukkan jumlah donat: "))

uang_pelanggan = int(input("Masukkan uang pelanggan: "))

isi_donat_per_paket = int(input("Masukkan isi donat per paket: "))

#Menghitung total Penjualan
total_harga_kopi = harga_kopi * jumlah_kopi 
total_harga_donat = harga_donat * jumlah_donat 
total_keseluruhan = total_harga_kopi + total_harga_donat
print("Total penjualan:", total_keseluruhan)

#Menghitung rata rata harga dengan operator / (pemabgian float)
total_item_terjual = jumlah_kopi + jumlah_donat
rata_rata_harga = total_keseluruhan / total_item_terjual
print("Rata-rata harga per item:", rata_rata_harga)

#Menghitung kembalian dengan operator (pengurangan)
kembalian = uang_pelanggan - total_keseluruhan
print("Kembalian yang harus dikembalikan:", kembalian)

#Menghitung berapa banyak paket donat (isi) yang bisa dibuat
paket_donat = jumlah_donat // isi_donat_per_paket
print("Jumlah paket donat yang bisa dibuat:", paket_donat)  

#Menghitung sisa donat diluar paket dengan operator % (modulo atau modulus)
sisa_donat_diluar_paket = jumlah_donat % isi_donat_per_paket
print("Sisa donat diluar paket:", sisa_donat_diluar_paket)