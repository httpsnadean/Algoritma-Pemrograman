print("Annisa Natasya Nadin\n064002100003\nPraktikum 11 Tugas 1")

class mahasiswa:
    
    total = 0
    
    def __init__(self,nama,nim,jurusan):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.jurusan = str(jurusan)
        mahasiswa.total += 1
        
    def biodata(self):
        return str(f'{self.nama} ;  {self.nim} ; {self.jurusan}')
    
    def cetak(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Jurusan:',self.jurusan)
        print()
        input(f'Jumlah mahasiswa adalah {mahasiswa.total} orang\nPRESS ENTER')


while True:
    print(f'\nMahasiswa {(mahasiswa.total)+1}\nKetik q untuk berhenti!')
    x1 = str(input('Nama: '))
    if x1 == 'q':
        break
    x2 = str(input('NIM: '))
    x3 = str(input('Jurusan: '))
    n = mahasiswa(x1, x2, x3)
    
    n.cetak()
