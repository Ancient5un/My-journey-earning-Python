import pandas as pd

list_nim = []
list_uts = []
list_uas = []
list_total = []
list_status = []


banyak_data = int(input("Masukan Jumlah data yang ingin anda masukan: "))

for i in range(banyak_data):
    print("\n*********************************************\n")
    print("Data ke-"+ str(i + 1))
    list_nim.append(input("Masukan NIM Anda       : "))
    list_uts.append(int(input("Masukan Nilai UTS Anda : ")))
    list_uas.append(int(input("Masukan Nilai UAS Anda : ")))
print("\n*********************************************")
for i in range(banyak_data):
    total_nilai = int(list_uts[i] + list_uas[i])/2
    list_total.append(total_nilai)
    if total_nilai >= 70:
        list_status.append("Lulus")
    else:
        list_status.append("Tidak Lulus")

siswa = {
    "NIM" : list_nim,
    "Nilai UTS": list_uts,
    "Nilai UAS": list_uas,
    "Rata-rata": list_total,
    "Status": list_status
}

data_siswa = pd.DataFrame(siswa)
print("============== Daftar Nilai Siswa =============")
print(data_siswa)
print("===============================================")
