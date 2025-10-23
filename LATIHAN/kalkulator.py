import math

while True:
    print("\n" + "="*40)
    print("🧮  \033[92m=== KALKULATOR SEDERHANA ===\033[0m  🧮")
    print("="*40)

    angka1 = float(input("Masukkan angka pertama: "))
    operasi = input("Pilih operasi (+, -, x, /, ^, %, √): ")

    if operasi in ["+", "-", "x", "/", "^", "%"]:
        angka2 = float(input("Masukkan angka kedua: "))

        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "x":
            hasil = angka1 * angka2
        elif operasi == "/":
            if angka2 == 0:
                print("Tidak bisa di bagi 0")
                continue
            hasil = angka1 / angka2
        elif operasi == "^":
            hasil = angka1 ** angka2
        elif operasi == "%":
            hasil = angka1 % angka2

        print("="*35)
        hasil = round(hasil, 2)
        print(f"Hasil: {angka1} {operasi} {angka2} = {hasil}")
        print("="*35)

    elif operasi == "√":
        hasil = math.sqrt(angka1)
        print("="*35)
        print(f"Hasil: √{angka1} = {hasil}")
        print("="*35)

    else:
        print("Operasi yang anda masukkan salah!")

    repeat = input("Hitung lagi? (y/n): ").lower()
    if repeat != "y":
        break

print("Terima kasih telah memakai layanan kalkulator sederhana kami ✨\n")
