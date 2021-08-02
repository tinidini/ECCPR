nr_inmat=[]
print("\nIntroduceti 3 numere de inmatriculare pentru verificare:")
nr=input()
while nr:
    nr_inmat.append(nr)
    nr=input()
    
jud=['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ', 'GL', 'GR', 'GJ', 'HR', 'HD', 'IL', 'IS', 'IF', 'MM', 'MH', 'MS', 'NT', 'OT', 'PH', 'SM', 'SJ', 'SB', 'SV', 'TR', 'TM', 'TL', 'VS', 'VL', 'VN']
def judet(abrev): 
    if abrev in jud:
        return True
    else:
        return False
    
  
def numere(nr, jud):
    if jud=='B':
        if len(nr)==2 or len(nr)==3:
            return True
        else: return False
    elif len(nr)==2:
        return True
    else: return False



MAJ='Q W E R T Y U I O P A S D F G H J K L Z X C V B N M'.split()
def litere_random(maj): 
    if len(maj)!=3: 
        return False
    for litera in maj:
        if litera not in MAJ:
            return False
    return True


for nr in nr_inmat:
    nr=nr.split()
    if judet(nr[0]) and numere(nr[1], nr[0]) and litere_random(nr[2]):
        print("\nNumarul "+ nr + " este valabil")