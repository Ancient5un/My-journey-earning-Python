print("OPERATOR LOGIKA, IDENTITAS, DAN BITWISE")
print("=" * 40)

# Data nilai siswa
mtk = 60
ipa = 50

print(f"Nilai Matematika: {mtk}")
print(f"Nilai IPA: {ipa}")

# Operator Logika
print("\n--- OPERATOR LOGIKA ---")
if mtk > 60 and ipa > 60:
    print("Lulus dengan predikat A")
elif mtk > 60 or ipa > 60:
    print("Lulus dengan predikat B")
else:
    print("Tidak lulus")

# Operator Identitas
print("\n--- OPERATOR IDENTITAS ---")
print(f"mtk is ipa: {mtk is ipa}")
print(f"mtk is not ipa: {mtk is not ipa}")

# Operator Keanggotaan
print("\n--- OPERATOR KEANGGOTAAN ---")
power_ranger = ["Red", "Blue", "Black", "Yellow", "Pink"]
warna_dicari = "Red"
print(f"List Power Ranger: {power_ranger}")
print(f"'{warna_dicari}' in power_ranger: {warna_dicari in power_ranger}")
print(f"'Green' not in power_ranger: {'Green' not in power_ranger}")

# Operator Bitwise
print("\n--- OPERATOR BITWISE ---")
a = 12  # 1100 dalam biner
b = 5   # 0101 dalam biner

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"a & b (AND) = {a & b} -> {bin(a & b)}")
print(f"a | b (OR)  = {a | b} -> {bin(a | b)}")
print(f"a ^ b (XOR) = {a ^ b} -> {bin(a ^ b)}")
print(f"~a (NOT)    = {~a} -> {bin(~a & 0b1111)} (4-bit)")
print(f"a << 1 (Left Shift) = {a << 1} -> {bin(a << 1)}")
print(f"a >> 1 (Right Shift)= {a >> 1} -> {bin(a >> 1)}")