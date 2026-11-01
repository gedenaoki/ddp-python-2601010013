nama_barang = input("Masukkan nama barang: ")
harga_satuan = int(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah
ppn = subtotal * 0.11
total = subtotal + ppn

print(f"Subtotal {subtotal}, PPN {ppn}, Total {total}")