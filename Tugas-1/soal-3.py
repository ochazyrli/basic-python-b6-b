#Pelatihan Basic Python Indonesia.Ai
#Zyrlirosa - 081287980257
#Soal 3

nilai_teori = float(input("Nilai ujian teori: "))
nilai_praktik = float(input("Nilai ujian praktik :"))

if nilai_teori >70 and nilai_praktik >70:
    print("Selamat anda lulus")
elif nilai_teori >70 and nilai_praktik <70:
    print("Anda mengulang ujian Praktik")
elif nilai_teori <70 and nilai_praktik > 70:
    print("Anda mengulang ujian Teori")
else :
    print("Anda mengulang semua")