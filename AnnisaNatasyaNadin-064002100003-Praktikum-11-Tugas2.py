print("Annisa Natasya Nadin\n064002100003\nPraktikum 11 Tugas 2")

class mahasiswa:

    total = 0

    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.total += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.total} orang\nTekan ENTER')

class metodegetter:
    total = 0
    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.total += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.total} orang\nTekan ENTER')
   
    def nama(self):
        return self.__nama
    def nim(self):
        return self.__nim
    def jurusan(self):
        return self.__jurusan

class metodesetter:  
    total = 0
    def __init__(self,nama,nim,jurusan):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__jurusan = str(jurusan)
        mahasiswa.total += 1

    def biodata(self):
        return f"{self.nama} ; {self.nim} ; {self.jurusan}"

    def cetak(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Jurusan:',self.__jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.total} orang\nTekan ENTER')
        
    def nama(self, x1):
        self.__nama = x1

    def nim(self, x2):
        self.__nim = x2   

    def jurusan(self, x3):
        self.__jurusan = x3

while True:
    print("\nKetik -2 untuk menggunakan metode getter.")
    print("Ketik -1 untuk menggunakan metode setter.")
    print(f'Mahasiswa {(mahasiswa.total)+1}\nKetik angka selain -2 dan -1 untuk memberhentikan program.')
    metode = int(input('Masukkan pilihan (-2 atau -1): '))

    if metode == -2:
        print(f'\nMahasiswa {(mahasiswa.total)+1}')
        print("Anda menggunakan metode getter.")
        x1 = str(input('Masukkan Nama: '))
        x2 = str(input('Masukkan NIM: '))
        x3 = str(input('Masukkan Jurusan: '))
        n = metodegetter(x1, x2, x3)
        n.cetak()

    elif metode == -1:
        print(f'\nMahasiswa {(mahasiswa.total)+1}')
        print("Anda menggunakan metode setter.") 
        x1 = str(input('Masukkan Nama: '))
        x2 = str(input('Masukkan NIM: '))
        x3 = str(input('Masukkan Jurusan: '))
        n = metodesetter(x1, x2, x3)
        n.cetak()

    else :
        break
