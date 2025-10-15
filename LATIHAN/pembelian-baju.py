kode_baju = input("Masukkan kode baju (SP/AD): ").upper()
ukuran_baju = input("Masukkan ukuran baju (S/M/L/XL): ").upper()

if kode_baju == "SP":
    merk = "SuperDry"
    if ukuran_baju == "S" or ukuran_baju == "s":
        harga = 450000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 500000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 550000
    elif ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 600000
    else:
        harga = 0
        print("Ukuran baju tidak tersedia.")

elif kode_baju == "AD":
    merk = "Adidas"
    if ukuran_baju == "S" or ukuran_baju == "s":
        harga = 400000
    elif ukuran_baju == "M" or ukuran_baju == "m":
        harga = 450000
    elif ukuran_baju == "L" or ukuran_baju == "l":
        harga = 500000
    elif ukuran_baju == "XL" or ukuran_baju == "xl":
        harga = 550000
    else:
        harga = 0
        print("Ukuran baju tidak tersedia.")
else :
    merk = ""
    harga = 0
    print("Kode baju tidak tersedia.")
    
print("\n--- Detail Pembelian Baju ---")
print("Merk baju:" +str (merk))
print("Harga baju: Rp", (harga))
print("---     Terima Kasih     ---""\n")