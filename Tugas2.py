jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_roti_str = input("Masukkan jumlah pesanan rotiJumlah kopi yang dibeli: ")

print("Tipe data awal jumlah kopi:", jumlah_kopi_str, type(jumlah_kopi_str))
print("Tipe data awal jumlah roti:", jumlah_roti_str, type(jumlah_roti_str))

jumlah_kopi_str = int(jumlah_kopi_str)
jumlah_roti_str = int(jumlah_roti_str)

print("Tipe data setelah konversi jumlah kopi:", jumlah_kopi_str, type(jumlah_kopi_str))
print("Tipe data setelah konversi jumlah roti:", jumlah_roti_str, type(jumlah_roti_str))

harga_kopi = 5000
harga_roti = 7000

total_harga_kopi = jumlah_kopi_str * harga_kopi
total_harga_roti = jumlah_roti_str * harga_roti

print ("Harga Total Kopi: ", total_harga_kopi)
print ("Harga Total Roti: ", total_harga_roti)