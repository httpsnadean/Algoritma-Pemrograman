x = True
while x == True:
    print("Ketik 0 untuk menghentikan program.")
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan == 0:
        x = False
        print("Terimakasih & sampai jumpa.")
    else:
        if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
            if bulan == 2:
                tahun = int(input("Masukkan tahun: "))
                if (tahun%4==0):
                    print("Ada 29 hari dalam sebulan.")
                else:
                    print("Ada 28 hari dalam sebulan.")
            else:
                if bulan in [1,3,5,7,8,10,12]:
                    print("Ada 31 hari dalam sebulan.")
                else:
                    print("Ada 30 hari dalam sebulan.")
        else:
            print("Data invalid:", bulan)
