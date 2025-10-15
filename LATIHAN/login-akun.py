var_is = True
while var_is == True:
    print("Masukkan Email :")
    email = input()
    if email == "a@gmail.com":
        print("Masukkan Password:")
        password = input()
        if password == "udin":
            var_is = False
        else:
            print("Password anda salah, silahkan coba lagi!")
    else:
        print("EMail anda salah, silahkan coba lagi!")
print("Email dan Password benar!")
