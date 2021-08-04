print("introduceti numarul de comenzi:")
n=int(input())
print("\nlconst <dst> <val>\nadd <dst> <src0> <src>\nmul <dst> <src0> <src>\ndiv <dst> <src0> <src>\nprint <reg> \n")
cmd=[]
for i in range(n):
    cmd.append(input().split()) #comanda va fi scrisa ca un singur string, apoi impartita in ['comanda','param1','param2','param3'] [0 1 2 3]


reg=[0 for x in range(16)] #initializam 16 registre cu 0 

while n!=0: 
    for com in cmd:
    
        if com[0]=='lconst': 
            reg[int(com[1])]=int(com[2])
    
        if com[0]=='add': 
            reg[int(com[1])]=reg[int(com[2])]+reg[int(com[3])]
        
        if com[0]=='mul': 
            reg[int(com[1])]=reg[int(com[2])]*reg[int(com[3])]
        
        if com[0]=='div':
            reg[int(com[1])]=int(reg[int(com[2])]/reg[int(com[3])])
    
        if com[0]=='print': 
            print(reg[int(com[1])])
    
        n-=1    