list_nim = []
list_uts = []
list_uas = []
list_total = []


banyak_data = int(input("Masukan Jumlah data yang ingin anda masukan: "))

for i in range(banyak_data):
    print("\n*********************************************\n")
    print("Data ke-"+ str(i + 1))
    list_nim.append(input("Masukan NIM Anda       : "))
    list_uts.append(int(input("Masukan Nilai UTS Anda : ")))
    list_uas.append(int(input("Masukan Nilai UAS Anda : ")))
print("\n*********************************************")


print("===============================================================")
print("|          NIM          |  NILAI UTS  |  NILAI UAS  |  TOTAL  |")
print("===============================================================")
for i in range(banyak_data):
    list_total.append(int(list_uts[i] + list_uas[i])/2)
    print(f"|        {list_nim[i]}       |      {list_uts[i]}     |     {list_uas[i]}      |   {list_total[i]}  |")
print("===============================================================")
