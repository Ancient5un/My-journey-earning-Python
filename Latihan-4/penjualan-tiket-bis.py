# Program Penjualan Tiket Bus

print("--------------------------------------------------")
print("               PENJUALAN TIKET BUS")
print("                        XYZ")
print("--------------------------------------------------")

# Input data pembeli
nama = input("Nama Pembeli : ")
hp = input("No. Handphone : ")
kode = input("Kode Jurusan yang dipilih (SBY/JKT/BDG) : ").upper()

# Data jurusan
if kode.upper() == "SBY":
    kota = "Surabaya"
    harga = 300000
elif kode.upper() == "JKT":
    kota = "Jakarta"
    harga = 350000
elif kode.upper() == "BDG":
    kota = "Bandung"
    harga = 320000
else:
    kota = "Tidak diketahui"
    harga = 0

jumlah = int(input("Jumlah Beli : "))

print("--------------------------------------------------")

# Hitung total & potongan
total = harga * jumlah

# contoh diskon 10% jika beli lebih dari 2 tiket
if jumlah > 2:
    potongan = total * 0.10
else:
    potongan = 0

total_bayar = total - potongan

# input uang bayar
print(f"potongan yang didapat :  {potongan}")
print(f"Total Bayar :  {total_bayar}")
uang = float(input("Masukkan Uang Bayar : "))

# hitung uang kembali
kembali = uang - total_bayar
print(f"Uang Kembali :  {kembali}")
