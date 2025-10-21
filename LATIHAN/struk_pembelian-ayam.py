
# gerobak friend chicken 
print("\n-------------------------------")
print("|  GEROBAK FRIEND CHICKEN     |")
print("-------------------------------")
print("| Kode  | Jenis  |     Harga  |")
print("-------------------------------")
print("|  A    | Dada   |  Rp. 25000 |")
print("|  B    | Paha   |  Rp. 20000 |")
print("|  C    | Sayap  |  Rp. 15000 |")
print("-------------------------------\n")

# input banyak jenis yang dipesan
banyak = input("Masukkan banyak Jenis yang anda pesan: ")

# list untuk menyimpan kode jenis dan banyak potong
list_kode = []
list_banyak_potong = []
list_harga_satuan = []

# input kode jenis dan banyak potong
for i in range (int(banyak)):
    print("\n"+"="*30+("\n"))
    print("jenis ke- " + str(i+1))
    kode = input("Masukkan Kode Jenis (A/B/C): ").upper()
    banyak_potong = int(input("Masukkan Banyak Potong: "))
    print("\n"+"="*30)

# menentukan harga satuan berdasarkan kode jenis
    if kode == "A":
        harga_satuan = 25000
    elif kode == "B":
        harga_satuan = 20000
    elif kode == "C":
        harga_satuan = 15000
    else:
        harga_satuan = 0

    list_kode.append(kode)
    list_banyak_potong.append(banyak_potong)    
    list_harga_satuan.append(harga_satuan)


# # menampilkan struk pesanan
print("\n|===============================================|")
print("|            GEROBAK FRIEND CHICKEN             |")
print("|-----------------------------------------------|")
print("| NO | Jenis    |  Harga   | Banyak  |  Total   |")
print("|    | potong   |  satuan  |  beli   |  Harga   |")
print("|-----------------------------------------------|")

jumlah_harga = 0
for i in range (int(banyak)):
    total = list_harga_satuan[i] * list_banyak_potong[i]
    jumlah_harga += total
    pajak = jumlah_harga * 0.1
    print(f"|  {i+1} | {list_kode[i]}        |  {list_harga_satuan[i]:,.0f}  |    {list_banyak_potong[i]}    |  {total:,.0f}  |")
print("|===============================================|")
print(f"                        Jumlah Harga : Rp. {jumlah_harga:,.0f}")
print(f"                        pajak (10%)  : Rp. {pajak:,.0f}")
print(f"                        Total Bayar  : Rp. {jumlah_harga + pajak:,.0f}")
print("terima kasih telah berbelanja di gerobak friend chicken")