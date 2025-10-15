# Input data dengan validasi biar gak kosong
def get_input(prompt):
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("Input tidak boleh kosong!")

# input data diri
nim = get_input('Masukkan NIM Anda: ')
nama = get_input('Masukkan Nama Anda: ')
jurusan = get_input('Masukkan Jurusan Anda: ')
alamat = get_input('Masukkan Alamat Anda: ')

# cetak data diri
print('+=' * 30)
print('\nHasil cetak data di atas adalah sebagai berikut:\n')
print(60 * '-')
print(f'NIM     : {nim}')
print(f'Nama    : {nama}')
print(f'Jurusan : {jurusan}')
print(f'Alamat  : {alamat}')
print('+=' * 30)