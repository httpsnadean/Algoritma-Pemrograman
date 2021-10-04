from math import sin, cos, atan2, radians, sqrt, ceil

print("Menghitung Jarak antara Dua Titik di Permukaan Bumi")
x1 = float(input("Masukkan Garis Lintang 1 : "))
x2 = float(input("Masukkan Garis Lintang 2 : "))
y1 = float(input("Masukkan Garis Bujur 1 : "))
y2 = float(input("Masukkan Garis Bujur 2 : "))

R = 6371
x1, x2, y1, y2 = map(radians, [x1, x2, y1, y2])
dlintang = x2 - x1
dbujur = y2 - y1
a = sin(dlintang/2)**2 + cos(x1) * cos(x2) * sin(dbujur/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
d = R * c

print("========================")
print(f"Jarak = {ceil(d)} km")
print("========================")
