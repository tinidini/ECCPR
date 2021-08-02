#citire
print("\nIntroduceti numarul de zile")
n=input()
n=int(n)

print("\nCati bani primeste de la tatal sau in fiecare zi?")
l_bani=input()

l_bani=l_bani.split()
bani=[]
for i in l_bani:
    bani.append(i)

cost_bomboana=[]
aroma_bomboana=[]
i=0
print("Introduceti costul si aroma bomboanei din ziua respectiva ('cost' 'aroma')")
while i<n:
    print("\nZiua "+str(i+1))
    cost_ar=input()
    cost_ar=cost_ar.split()
    cost_bomboana.append(cost_ar[0])
    aroma_bomboana.append(cost_ar[1])
    i+=1

#prelucrare
cumparate=[]
zi=0
fericire=0
balance=0

while zi<n:
    balance+=int(bani[zi]) #suma primita de la tata
    if int(cost_bomboana[zi])<=balance: #verif daca isi permite
        balance-=int(cost_bomboana[zi]) #daca isi permite cumpara 
        fericire+=int(aroma_bomboana[zi]) #fericire++
        cumparate.append(aroma_bomboana[zi]) #keep track
    else: #nu isi permite
        i=0
        for x in cumparate:
            if int(aroma_bomboana[zi])>int(x): i+=1  #verif daca a cumparat ceva mai scump zilele trecute
        if i==(zi): fericire-=int(aroma_bomboana[zi]) # scade fericirea
    zi+=1

#afisare
print("Fericirea baiatului:")
print(fericire)