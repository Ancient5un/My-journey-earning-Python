#----Program Menentukan grade nilai---
#--- programmer : BBJ ----------
#-------------------------------
abs = int(input('Masukan Nilai Absen: '))
tgs = int(input('Masukan Nilai Tugas: '))
uts = int(input('Masukan Nilai uts  : '))
uas = int(input('Masukan Nilai Uas  : '))

akhir =(0.2*abs)+(0.2*tgs)+(0.3*uts)+(0.3*uas)
if akhir > 85 :
    grade ="A"

else:
    if akhir > 65 :
        grade ="B"
    else:
         if akhir > 50 :
              grade ="C"
         else:
              if akhir > 30:
                  grade = "D"
              else:
                  grade = "E"
print('------------------------')
print("Nilai Akhir :",akhir)
print("Gradenya    :",grade)