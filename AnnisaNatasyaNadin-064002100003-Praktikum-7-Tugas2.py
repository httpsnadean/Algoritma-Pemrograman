print("Annisa Natasya Nadin\n064002100003\nProgram Bilangan Ordinal")
def bil_ordinal(num):
    ordinal_dict = {1: "st", 2: "nd", 3: "rd"}
    a, mod = divmod(num, 10)
    suffix = a % 10 != 1 and ordinal_dict.get(mod) or "th"
    print(f"{num}, '{suffix}'")
    
print("Ketik -1 untuk menghentikan program")

loop = True
while loop == True:
    num = int(input("Masukan Angka : "))
    if num == -1:
        loop = False
        break
    else:
        bil_ordinal(num)
