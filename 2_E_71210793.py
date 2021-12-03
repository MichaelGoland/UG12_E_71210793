'''
Hai_Tutu = input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri :")

SENIN = [' Algoritma Graf', 'Sistem Operasi', ' PAK', 'Praktikum INLAN']
SELASA = [' Matematika Teknik', ' Bhs Indonesia', ' PKN']
RABU = ['Hari rabu Anda tidak ada kelas']
KAMIS = ['IMK']
JUMAT = ['Sistem Basis Data', ' Praktikum Sistem Basis Data', ' INLAN']

HARI={'senin':SENIN, 'selasa':SELASA, 'sabu':RABU, 'kamis':KAMIS, 'jumat':JUMAT}

hari_pertama=0
for i in range(len(HARI[Hai_Tutu.lower()])):
    
    print("Kelas ke-", hari_pertama+1, " ", HARI[Hai_Tutu][hari_pertama])
    hari_pertama +=1
'''
Hai_Nama = input("Masukkan Nama :")

#Hai_Tutu = input("Hi,",Hai_Nama, " Silahkan Masukkan hari yang ingin Anda telusuri :")
Hai_Tutu = input("Hi,{} Silahkan Masukkan hari yang ingin Anda telusuri :".format(Hai_Nama))

SENIN = [' Hari ke-1 Algoritma Graf', 'Hari ke-3 Sistem Operasi', 'Hari ke-4 PAK', 'Hari ke-5 Praktikum INLAN']
SELASA = ['Hari ke-2 Matematika Teknik', 'Hari ke-4 Bhs Indonesia', 'Hari ke-6 PKN']
RABU = ['Hari rabu Anda tidak ada kelas']
KAMIS = ['Kelas ke-1 IMK', 'Kelas ke-3 LogMat', 'Kelas ke-4 Praktekkom']
JUMAT = ['Kelas ke-2 Sistem Basis Data', 'Kelas ke-4 Praktikum Sistem Basis Data', 'Kelas ke-6 INLAN']

HARI={'senin':SENIN, 'selasa':SELASA, 'rabu':RABU, 'kamis':KAMIS, 'jumat':JUMAT}

hari_pertama=0
for i in range(len(HARI[Hai_Tutu.lower()])):    
    print(HARI[Hai_Tutu][hari_pertama])
    hari_pertama +=1

