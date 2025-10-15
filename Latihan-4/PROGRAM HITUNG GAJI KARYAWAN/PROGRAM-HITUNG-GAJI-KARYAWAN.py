# gaji pokok & tarif
gaji_pokok = 300000
tarif_lembur_per_jam = 3500

# persentase tunjangan golongan
golongan_persen = {
    '1': 0.05,
    '2': 0.10,
    '3': 0.15
}

# persentase tunjangan pendidikan
pendidikan_persen = {
    'SD': 0.0,
    'SMP': 0.0,
    'SMA': 0.025,
    'D1': 0.05,
    'D3': 0.20,
    'S1': 0.30
}

print("PROGRAM HITUNG GAJI KARYAWAN\n")
nama = input("Masukkan nama karyawan: ").strip()
golongan = input("Masukkan golongan (1/2/3): ").strip()
pendidikan = input("Masukkan pendidikan (SD/SMP/SMA/D1/D3/S1): ").strip().upper()

try:
    jumlah_hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: ").strip())
    jam_kerja_per_hari = int(input("Masukkan jam kerja dalam sehari: ").strip())
except ValueError:
    print("Input jumlah/ jam harus berupa angka. Program selesai.")
    raise SystemExit

# hitung lembur
jam_lembur_per_hari = max(0, jam_kerja_per_hari - 8)
total_jam_lembur = jam_lembur_per_hari * jumlah_hari_kerja
honor_lembur = total_jam_lembur * tarif_lembur_per_jam

# tunjangan berdasarkan golongan & pendidikan
tunjangan_golongan = gaji_pokok * golongan_persen.get(golongan, 0)
tunjangan_pendidikan = gaji_pokok * pendidikan_persen.get(pendidikan, 0)

# total gaji
total_gaji = gaji_pokok + tunjangan_golongan + tunjangan_pendidikan + honor_lembur

# format rupiah (koma diganti titik)
def fmt_rp(x):
    return "Rp " + f"{x:,.0f}".replace(",", ".")

print("\n--- Detail Karyawan ---")
print(f"Nama                : {nama}")
print(f"Golongan            : {golongan} (Tunjangan: {fmt_rp(tunjangan_golongan)})")
print(f"Pendidikan          : {pendidikan} (Tunjangan: {fmt_rp(tunjangan_pendidikan)})")
print(f"Gaji pokok          : {fmt_rp(gaji_pokok)}")
print(f"Jam kerja/hari      : {jam_kerja_per_hari} jam")
print(f"Jam lembur/hari     : {jam_lembur_per_hari} jam")
print(f"Jumlah hari kerja   : {jumlah_hari_kerja} hari")
print(f"Total jam lembur    : {total_jam_lembur} jam")
print(f"Honor lembur        : {fmt_rp(honor_lembur)}")
print(f"Total gaji (bulan)  : {fmt_rp(total_gaji)}")
# ...existing code...