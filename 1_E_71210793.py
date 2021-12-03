Bilangan_Awal = int(input("Masukkan awal deret :"))
Bilangan_Akhir = int(input("Masukkan akhir deret :"))

x = []
for i in range(Bilangan_Awal, Bilangan_Akhir):
    if i%2 == 0:
        if i%5 != 0 and i%9 != 0:
            x.append(i)
            #print(x) 
print(*x)        