n=int(input())
Zaruri=[]
for i in range(n):
    Zaruri.append(input().split())
    

suma=0
for zar in Zaruri: 
    for i in range(1,7): 
        if str(i) not in zar: #fata nu este vizibila
            suma+=i 
            
#afisare
print(suma)