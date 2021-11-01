def average_score():
    score = 0    
    rep = 1
    num = 0
    while rep == 1:
        num += 1
        z = str(input('Tekan "ENTER" untuk berhenti.\nMasukkan nilai siswa: '))
        if z == '':
            num -= 1
            rep = 0
        else:
            if z == 'A': 
                score += float(4)
                a = '4'
            elif z == 'A-':
                score += float(3.75)
                a = '3,75'
            elif z == 'B+':
                score += float(3.50)
                a = '3,5'
            elif z == 'B':
                score += float(3.00)
                a = '3'
            elif z == 'B-':
                score += float(2.75)
                a = '2,75'
            elif z == 'C+':
                score += float(2.50)
                a = '2,5'
            elif z == 'C':
                score += float(2.00)
                a = '2'
            elif z == 'C-':
                score += float(1.75)
                a = '1,75'
            else:
                print('The data is invalid.')
                num -= 1
                a = 'The number is invalid.'
            print(f"Nilai ke-{num} = {a}")
    average = score / num
    return average

print("Rata-rata:" ,average_score())
