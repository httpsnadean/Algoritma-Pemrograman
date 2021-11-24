def edit():
    nadin = open('mybio.txt','w')
    
    n1 = str(input('Nama : '))
    n1 = list(n1.split(' '))
    n1c = [str.capitalize(x) for x in n1]
    n1x = ' '.join(n1c)
    n2 = str(input('Umur : '))
    n3 = str.upper(input('Alamat : '))
    n4 = str(input('Email : '))
    n5 = str(input('Dosen Wali : '))
    n5 = list(n5.split(' '))
    n5c = [str.capitalize(x) for x in n5]
    n5x = ' '.join(n5c)
    
    text = str(f'''
    Nama: {n1x}
    Umur: {n2}
    Alamat: {n3}
    Email: {n4}
    Dosen Wali: {n5x}
    ''')
    
    nadin.write(str(text))
    
    nadin.close()

    print('File "mybio.txt" sudah tersimpan.')

def baca():
    dean = open('mybio.txt','r')
    for i in dean:
        print(i)
        
    dean.close()
    
while True:
    opsi = str.lower(input('\n\nProgram Biodata Editor\na. Edit\nb. Baca\n\n= '))
    if opsi == 'a':
        edit()
    elif opsi == 'b':
        baca()
        input('Klik Enter')
    else:
        print('Invalid')
