
n = int(input("Masukkan Angka :"))
j=int(n)
pola=[]
for i in range (n+1):
    bintang="" 
    for n in range(2*i-1):
       
        if n%2==0:
            bintang+= "*"
        else:
            bintang+= " "

    p=str(" "*(j)+bintang+" "*(j))
    pola.append(str(p))
    j-=1


for i in range(len(pola)): 
    print(pola[i])
for i in range(len(pola)-2,-1,-1): 
    print(pola[i])    


