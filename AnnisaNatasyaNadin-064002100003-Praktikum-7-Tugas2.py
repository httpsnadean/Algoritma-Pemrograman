print("Annisa Natasya Nadin\n064002100003\nProgram Bilangan Ordinal")
def bil_ordinal(num):
    ordinal_dict = {1: "st", 2: "nd", 3: "rd"}
    z, mod = divmod(num, 10)
    suffix = z % 10 != 1 and ordinal_dict.get(mod) or "th"
    print(f"{num}, '{suffix}'")
    
print("Enter -1 to stop the program.")

loop = True
while loop == True:
    num = int(input("Enter the number: "))
    if num == -1:
        loop = False
        break
    else:
        bil_ordinal(num)
