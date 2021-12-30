print("Annisa Natasya Nadin\n064002100003\nPraktikum 9 Tugas 2")
judul = str(input("Masukkan judul file: "))
namaFile = (f"{judul}.txt")
f = open(namaFile, "w")
f.close()
print(f"File {namaFile} sudah dibuat. ")
print("Masukkan 'q' untuk memberhentikan program. ")

def write(string):
    file = open(f"{judul}.txt","w")
    file.write(str(string))
    file.close()

def read():
    file = open(f"{judul}.txt", "r")
    teks = file.read()
    print(teks)

x = True
while x == True:
    y = (input(""))
    if y == "q":
        print("\nTeks disimpan!")
        x = False
    else:
        write(y)
        read()
