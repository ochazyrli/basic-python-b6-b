import math

def luas_lingkaran(r):
    luas = math.pi*r*r
    print("Luas Lingkaran dengan jari jari {} adalah : {:.2f} cm\u00b2".format(r,luas))

def keliling_lingkaran(r):
    keliling = 2*math.pi*r
    print("Keliling Lingkaran dengan jari jari {} adalah : {:.2f} cm\u00b2".format(r,keliling))

r = int(input("Jari - jari lingkaran : "))

luas_lingkaran(r)
keliling_lingkaran(r)