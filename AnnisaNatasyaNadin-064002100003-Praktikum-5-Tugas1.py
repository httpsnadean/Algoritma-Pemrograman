n = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]
score = 0



        
nstudent = []
repeat = 0
number = 0
while repeat == 0:
    number += 1
    x = str.upper(input('Ketik "q" untuk keluar!\nn Mahasiswa: '))
    if x == 'Q':
        repeat = 1
    else:
        if x == 'A':
            score = float(n[0])
        elif x == 'A-':
            score = float(n[1])
        elif x == 'B+':
            score = float(n[2])
        elif x == 'B':
            score = float(n[3])
        elif x == 'B-':
            score = float(n[4])
        elif x == 'C+':
            score = float(n[5])
        elif x == 'C':
            score = float(n[6])
        elif x == 'C-':
            score = float(n[7])
        elif x == 'D':
            score = float(n[8])
        elif x == 'E':
            score = float(n[9])
        else:
            print('Anda salah memasukkan huruf.')
            score = 0
        print(('\nMahasiswa{0} = {1}').format(number,score))
        nstudent.append(score)
    
average = sum(nstudent) / len(nstudent)
print(f"Nilai Rata-rata: {average}")
