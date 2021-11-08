print("Annisa Natasya Nadin\n064002100003\nProgram Bilangan Prima")
def cek_bil(bil):
    if bil == 1:
        print(f"Bilangan ini {bil} merupakan bilangan prima")
    elif bil == 2:
        print(f"Bilangan ini {bil} merupakan bilangan prima")
    else:
        global x 
        for x in range(2, bil):
            if bil % x == 0:
                stat = 0 
                break
            else:
                stat = 1 
        cek_stat(stat)
        
def cek_stat(stat):
    if stat == 0:
        print(f"Bilangan ini {bil} merupakan bilangan prima")
        print(f"{x} kali {bil//x} = {bil}")
    else:
        print(f"{bil} merupakan bilangan prima")

a = 1
while a == 1:                    
    bil = int(input("Masukkan bilangan : "))
    cek_bil(bil)                 
bil = int(input("Masukkan bilangan : "))
cek_bil(bil)
