print("Annisa Natasya Nadin\n064002100003\nMenghitung Bilangan Fibonacci")
def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))
   
def cetak(x):
    if x <= 0:
        print("Masukkan hanya bilangan positif.")
    else:
       print('Bilangan Fibonacci ke-'+str(x),'adalah',fib(x))

while True:
    try:
        num = int(input("Masukkan bilangan: "))
    except ValueError:
        print("Invalid, masukkan hanya bilangan bulat.\n")
    else:
        cetak(num)
