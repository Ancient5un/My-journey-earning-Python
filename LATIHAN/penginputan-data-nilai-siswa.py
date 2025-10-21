# program untuk iterasi list menggunakan pengindeksan

mapel = ["matematika", "bahasa indonesia", "bahasa inggris", "ipa", "ips"]

for i in range(len(mapel)): #harus pakai len() untuk mengetahui panjang list
    print("saya suka mata pelajaran", mapel[i])

count = 0
while count <= 5:
    print("nilai count:", count)
    count += 1
print("selesai")

ulang = 2
for i in range(ulang):
    print("Data  ke-" + str (i + 1))
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    nilai_uas = float(input("Masukkan Nilai UAS: "))
    print(f"nim anda adalah {nim},",f"nama anda adalah {nama},", f"nilai UTS anda adalah {nilai_uas},")
    print("-------------------------------")