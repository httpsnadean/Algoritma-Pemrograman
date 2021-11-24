print("Annisa Natasya Nadin\n064002100003\nProgram Perpangkatan Rekursif")
def pangkat(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a * pangkat(a, abs(b)-1))
    else:
        return a * pangkat(a, b-1)

while True:
    a = int(input("Masukkan angka : "))
    b = int(input("Masukkan pangkat : "))
    print(pangkat(a, b),"\n")
