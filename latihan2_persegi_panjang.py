panjang = float(input("Masukkan panjang (m): "))
lebar = float(input("Masukkan lebar (m): "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print("Luas :", luas, "m2")
print("Keliling :", keliling, "m")


# ==================== TRACE TABLE ====================
# Contoh input: panjang = 8, lebar = 5
#
# | Langkah | Instruksi                          | panjang | lebar | luas | keliling | Output              |
# |---------|------------------------------------|---------|-------|------|----------|---------------------|
# | 1       | panjang = float(input(...))        | 8.0     | -     | -    | -        | -                   |
# | 2       | lebar = float(input(...))          | 8.0     | 5.0   | -    | -        | -                   |
# | 3       | luas = panjang * lebar             | 8.0     | 5.0   | 40.0 | -        | -                   |
# | 4       | keliling = 2 * (panjang + lebar)   | 8.0     | 5.0   | 40.0 | 26.0     | -                   |
# | 5       | print("Luas :", luas, "m2")        | 8.0     | 5.0   | 40.0 | 26.0     | Luas : 40.0 m2      |
# | 6       | print("Keliling :", keliling, "m") | 8.0     | 5.0   | 40.0 | 26.0     | Keliling : 26.0 m   |