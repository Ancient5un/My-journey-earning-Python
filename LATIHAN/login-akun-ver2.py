var_is  = True
while var_is == True:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username == "admin" and password == "admin123":
        print("Login Berhasil!")
        var_is = False
    else:
        print("Username atau Password Salah. Silakan coba lagi.")   
        var_is = True
        continue
print("Selamat datang di sistem kami.")

