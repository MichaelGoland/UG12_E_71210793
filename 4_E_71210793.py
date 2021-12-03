#Nilai = int(input["Nilai a :"])
#Nilai_2 = int(input["Nilai b :"])
#Nilai_3 = int(input["Nilai c :"])
#Nilai_4 = int(input["Nilai d :"])
#Nilai_5 = int(input["Nilai e :"])

def Nilai_Max(daftar):
    maks = 0
    for x in daftar:
        if x > maks:
            maks=x
    return maks
def Nilai_Min(daftar_1):
    min = 999999999999999
    for y in daftar_1:
        if y < min:
            min=y
    return min

jumlahAngka=[]

Angka = int(input("Berapa pilihan angka:"))
for n in range(Angka):
    nilai = int(input("Masukkan angka:"))
    jumlahAngka.append(nilai)
print(jumlahAngka)

print("Angka Terbesar:", Nilai_Max(jumlahAngka))

print("Angka Terkecil:", Nilai_Min(jumlahAngka))





