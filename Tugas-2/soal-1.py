#Pelatihan Basic Python Indonesia.Ai
#Zyrlirosa - 081287980257
#Soal 1 - Tugas 2

kontak_list = []
awal = {
        "nama" : "Ocha",
        "telp" : "0812828128",
    }
kontak_list.append(awal)

def Welcoming():
    print("Halo, selamat datang!")

def Daftar_menu():
    print("Silahkan pilih menu yang tersedia!")
    print("------MENU-----")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    jawab = int(input("Pilihan Menu : "))
    if (jawab == 1):
        jawaban_1()
        Daftar_menu()
    elif (jawab == 2):
        jawaban_2()
        Daftar_menu()
    elif (jawab == 3):
        print("Program telah selesai")
    else:
        print("Menu Tidak Tersedia")

def jawaban_1():
    for i in kontak_list:
        print("Nama     : ",i["nama"])
        print("No. Telp : ",i["telp"])

def jawaban_2():
    nama = input("Masukkan Nama anda : ")
    telp = input("Masukkan No. Telp anda : ")
    data = {
        "nama" : nama,
        "telp" : telp,
    }
    kontak_list.append(data)
    print("Kontak berhasil ditambahkan!")

Welcoming()
Daftar_menu()