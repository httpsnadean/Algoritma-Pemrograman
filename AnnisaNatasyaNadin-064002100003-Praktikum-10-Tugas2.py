print("Annisa Natasya Nadin\n064002100003\nPraktikum 10 Tugas 2")
def bubbleSort(arr):
    count = 0
    n = len(arr) 
    for i in range(n): 
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    return arr
    
    if count == 0:
        return arr
    else:
        bubbleSort(arr)

while True:
    while True:
        try:        
            sort = str(input("Masukkan bilangan: (1,3,5,..)\n")).split(",")
            sort = [int(i) for i in sort]
        except:
            print("\nTidak valid!\nBukan termasuk bilangan bulat.")
        else:
            break
    
    print(f"\n\nList: {sort}")
    
    bubbleSort(sort)  
    print(f"\n\nList diurutkan: {sort}")
