print("Menentukan Jenis Segitiga")
print("=========================")
x = int(input("Sisi A: "))
y = int(input("Sisi B: "))
z = int(input("Sisi C: "))

if x + y <= z or x + z <= y or y + z <= x :
    print("Bukan segitiga")
elif x == y and y == z :
    print("Segitiga sama sisi")
elif x == y or x == z or y == z :
    print("Segitiga sama kaki")
elif (x*x + y*y == z*z) or (x*x + z*z == y*y) or (z*z + y*y == x*x) :
    print("Segitiga Siku-siku")
else:
    print("Segitiga sembarang")
