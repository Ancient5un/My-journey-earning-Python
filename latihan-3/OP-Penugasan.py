def operasi_penugasan(operasi, simbol):
    print(f"\n--- OPERASI {operasi.upper()} DENGAN PENUGASAN ---")
    try:
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        
        a = angka1
        if operasi == "penjumlahan":
            a += angka2
        elif operasi == "pengurangan":
            a -= angka2
        elif operasi == "perkalian":
            a *= angka2
        elif operasi == "perpangkatan":
            a **= angka2
        elif operasi == "pembagian":
            if angka2 == 0:
                print("Error: Pembagian dengan nol!")
                return
            a /= angka2
        elif operasi == "pembagian bulat":
            if angka2 == 0:
                print("Error: Pembagian dengan nol!")
                return
            a //= angka2
        elif operasi == "modulus":
            if angka2 == 0:
                print("Error: Modulus dengan nol!")
                return
            a %= angka2
        
        print(f"Hasil: {angka1} {simbol} {angka2} = {a}")
        print(40 * '=')
        
    except ValueError:
        print("Error: Masukkan angka yang valid!")
    except Exception as e:
        print(f"Error: {e}")

print("OPERATOR PENUGASAN ARITMATIKA")
print("=" * 40)

# Daftar operasi
operasi_list = [
    ("penjumlahan", "+=", "+"),
    ("pengurangan", "-=", "-"),
    ("perkalian", "*=", "*"),
    ("perpangkatan", "**=", "**"),
    ("pembagian", "/=", "/"),
    ("pembagian bulat", "//=", "//"),
    ("modulus", "%=", "%")
]

for operasi, simbol_penugasan, simbol_operasi in operasi_list:
    operasi_penugasan(operasi, simbol_operasi)

print("\nSemua operasi selesai!")