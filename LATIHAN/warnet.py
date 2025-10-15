tarif_1 = 6000
tarif_2 = 5000

lama = int(input("Masukkan lama penggunaan warnet (dalam jam): "))
if lama <= 3:
    total_bayar = lama * tarif_1
else:
    total_bayar = (3 * tarif_1) + ((lama - 3) * tarif_2)
print("Total yang harus dibayar: Rp", total_bayar)  
print("Terima kasih telah menggunakan layanan kami.")