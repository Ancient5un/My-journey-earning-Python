print("\n PROGARAM HITUNG GAJI KARYAWAN")
print("----------------------------------")
nama = input                ("Masukkan nama karyawan             : ")
golongan = input            ("Masukkan golongan (1/2/3)          : ")
pendidikan = input          ("Masukkan pendidikan (SMA/D1/D3/S1) : ").upper()
jumlah_jam_kerja = int(input("Masukkan jumlah jam kerja          : "))
print("----------------------------------")

gaji_pokok = 300000

# tunjangan golongan
if golongan == '1':
    tjn_golongan = 0.05 * gaji_pokok
elif golongan == '2':
    tjn_golongan = 0.10 * gaji_pokok
elif golongan == '3':
    tjn_golongan = 0.15 * gaji_pokok
else:
    tjn_golongan = 0
    print("Golongan tidak valid, tunjangan golongan diatur ke 0.")

# tunjangan pendidikan
if pendidikan == 'SMA':
    tjn_pendidikan = 0.025 * gaji_pokok
elif pendidikan == 'D1':
    tjn_pendidikan = 0.05 * gaji_pokok
elif pendidikan == 'D3':
    tjn_pendidikan = 0.20 * gaji_pokok
elif pendidikan == 'S1':
    tjn_pendidikan = 0.30 * gaji_pokok
else:
    tjn_pendidikan = 0
    print("Pendidikan tidak valid, tunjangan pendidikan diatur ke 0.")

# hitung lembur
if jumlah_jam_kerja > 8:
    jam_lembur = jumlah_jam_kerja - 8
    honor_lembur = jam_lembur * 3500
else:
    jam_lembur = 0
    honor_lembur = 0
    print("Tidak ada jam lembur.")

total_gaji = gaji_pokok + tjn_golongan + tjn_pendidikan + honor_lembur
print("----------------------------------")
print("Nama Karyawan        : ", nama)
print("Golongan             : ", golongan)    
print("Pendidikan           : ", pendidikan)
print("Gaji Pokok           :  Rp ", gaji_pokok)
print("Tunjangan Golongan   :  Rp ", tjn_golongan)
print("Tunjangan Pendidikan :  Rp ", tjn_pendidikan)
print("Jam Lembur           : ", jam_lembur, "jam")
print("Honor Lembur         :  Rp ", honor_lembur)
print("Total Gaji           :  Rp ", total_gaji)
print("----------------------------------")

