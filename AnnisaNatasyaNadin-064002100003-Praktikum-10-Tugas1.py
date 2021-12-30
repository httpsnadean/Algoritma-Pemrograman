print("Annisa Natasya Nadin\n064002100003\nPraktikum 10 Tugas 1")
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
                if arr[j] > arr[j+1] : 
                        arr[j], arr[j+1] = arr[j+1], arr[j]

def binarySearchAppr (sor, start, end, a):
   if end >= start:
      mid = start + (end- start)//2
      if sor[mid] == a:
          return mid
      elif sor[mid] > a:
          return binarySearchAppr(sor, start, mid-1, a)
      else:
          return binarySearchAppr(sor, mid+1, end, a)
   else:
      return -1
  
arr = [5,9,24,39,50]
b = input('Masukkan angka: ')
b = int(b)
bubbleSort(arr)
hasil = binarySearchAppr(arr, 0, len(arr)-1, b)
hasil = int(hasil)
print(f'Data menjadi terurut: {arr} ')
if hasil != -1:
    print('Angka terdapat di arr: ' +str(hasil))
else:
    print('Angka tidak terdapat di arr. ')
