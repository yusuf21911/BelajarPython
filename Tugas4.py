# Operasi Pada String
# 1. Input nama pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")

# 2. Gabungkan string untuk pesan terima kasih
pesan_terima_kasih = "Terima kasih, " + nama_pelanggan + " sudah berbelanja di Coffee Shop Bahagia!"

# 3. Cetak pesan terima kasih dengan garis pemisah
garis = "*" * 25
print(garis)
print(pesan_terima_kasih)
print(garis)

# 4. Contoh data produk dan harga
nama_produk = "Kopi Pagi"
total_harga = 36001.0

# 5. Cetak pesan dengan f-string
print(f"Total harga {nama_produk} adalah Rp{total_harga}")
