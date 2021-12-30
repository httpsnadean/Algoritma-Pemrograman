print("Annisa Natasya Nadin\n064002100003\nPraktikum 12 Tugas 2")
judul = str(input("Masukkan judul file : "))
namafile = (f"{judul}.csv")
f = open(namafile, "w")
f.close()

print(f"File {namafile} sudah dibuat. ")
print("Ketik 0 untuk memberhentikan program. ")

file = open('Negara.csv','r')

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        x1.append(p1)
        p2 = cache[1]
        x2.append(p2)
        p3 = cache[2]
        x3.append(p3)
        p4 = int(cache[3])
        x4.append(p4)
        p5 = int(cache[4])
        x5.append(p5)

data.add("Negara", x1)
data.add("Ibukota", x2)
data.add("Benua", x3)
data.add("Luas", x4)
data.add("Populasi", x5)

import pandas as DATAFILE

def write(string):
    file = open(f"{judul}.csv","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{judul}.csv", "r")
    teks = file.read()
    print(teks)

z = True
while z == True:
    hasil = DATAFILE.DataFrame(data)
    print('\nData Luas dan Populasi di Dunia\n\n', hasil)
    print("Ketik -2 untuk mencari rata-rata.")
    print("Ketik -1 untuk mencari standar devisiasi.")
    
    isi = int(input("Masukkan pilihan Anda :"))
    mean = hasil.groupby(["Benua"]).mean()
    std = hasil.groupby(["Benua"]).std()
    if isi == 0:
        print("\nTeks disimpan!")
        z = False
    elif isi == -2:
        print('\nRata-rata :\n', mean)
        write(mean)
        read()
    elif isi == -1:
        print('\nStandar Deviasi :\n', std)
        write(std)
        read()
