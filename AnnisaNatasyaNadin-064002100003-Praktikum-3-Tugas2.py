from math import sqrt

print("Mencari Akar Persamaan Kuadrat dan Determinan")
print("=============================================")

A = int(input("Masukkan nilai A = "))
B = int(input("Masukkan nilai B = "))
C = int(input("Masukkan nilai C = "))

det = B ** 2 - 4 * A * C

if A == 0:
    print("Nilai A tidak boleh = 0")
else:
    print(f"Persamaan Kuadrat = {A}x^2 + {B}x + {C}")
    print(f"Determinan = {det}")

    if det < 0 :
        print("Persamaan tersebut merupakan akar imaginer.")
        print(f"Akar x1 = -{B} + Akar {det} / {B} * {A}")
        print(f"Akar x1 = -{B} - Akar {det} / {B} * {A}")
    elif det == 0:
        x1 = -B / (2 * A)
        x2 = x1
        print("Persamaan tersebut memiliki akar kembar.")
        print("Akar x1 =", x1)
        print("Akar x2 =", x2)
    elif det > 0:
        x1 = (-B + sqrt(det)) / (2 * A)
        x2 = (-B - sqrt(det)) / (2 * A)
        print("Persamaan tersebut memiliki akar berbeda.")
        print("Akar x1 =", x1)
        print("Akar x2 =", x2)
