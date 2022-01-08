
import re

listaParova = list()
skupA = list()

#za testiranje
#listaParova = [('a','b'),('a','c'),('a','d'),('a','e'),('a','f'),('b','b'),('c','c'),('d','d'),('e','e'),('f','f'),('g','b'),('g','c'),('g','d'),('g','e'),('g','f'),('g','g')]
#skupA = ['c','e','b','f','a','d','g']


# Funkcija koja iz stringa uklanja znakove [] i ' npr. [('a','b')] ispisati će kao (a, b)    
def formatStr(s)->str:
    return str(s).replace("'","").strip('[]')

#provjeravamo jesu li parovi relacije sastavljeni od elemenata skupa koji korisnik unosi
def provjeraUnosa(listaParova:list,skupA:list)->bool:
    određeniElementi = list(set(re.findall("[a-zA-z0-9]",formatStr(listaParova))))
    provjera =  all(item in skupA for item in određeniElementi)
    if not provjera:
        print('Pogreška! Unešeni elementi skupa ne odgovaraju elementima unutar unešenih parova.') 
        return False
    return True


#Relacija koja provjerava tranzitivnost binarne relacije
def tranzitivnost(listaParova:list)->bool:
    print('Tranzitivna:',end=' ')
    for element in listaParova:
        if element[0]==element[1]: continue
        B = list(e for e in listaParova if e[0]==element[1])
        if len(B) == 0: continue
        #ispitaj postoji li u orignialnoj listi (listaParova) implicirani član (ako su xRy i yRz, postoji li xRz)
        for e in B:
            implicElement = (element[0],e[1])
            # ako takav element nije pronađen Relacija nije tranzitivna - vrati False inače vrati True
            if not implicElement in listaParova: 
                print(f"NE jer za {formatStr(element)} i {formatStr(e)} ne postoji {formatStr(implicElement)} unutar liste parova")
                return False
    print("DA")
    return True

def refleksivnost(skupA:list,listaParova:list)->bool:
    print('Refleksivna:',end=' ')
    # za svaki x ∈ skupa A u mora postojati (x,x) u listi parova 
    for element in skupA:
        trazeniE = (element[0],element[0])
        if not trazeniE in listaParova:
            print(f'NE jer za element "{element}" ne postoji par {formatStr(trazeniE)} unutar liste parova')
            return False
    print("DA")
    return True

def antirefleksivnost(skupA:list,listaParova:list)->bool:
    print('Antirefleksivna:',end=' ')
    # za svaki x ∈ skupa A u NE SMIJE postojati (x,x) u listi parova 
    for element in skupA:
        trazeniE = (element[0],element[0])
        if trazeniE in listaParova:
            print(f'NE jer za element "{element}" postoji par {formatStr(trazeniE)} unutar liste parova')
            return False
    print("DA")
    return True


def simetricnost(listaParova:list)->bool:
    print('Simetrična:',end=' ')
    # za svaki (x,y) mora postojati (y,x) unutar liste parova
    for element in listaParova:
        if element[0] == element[1]: continue
        trazeniE = (element[1],element[0])
        if not trazeniE in listaParova:
            print(f'NE jer za {formatStr(element)} ne postoji {formatStr(trazeniE)} unutar liste parova')
            return False
    print('DA')
    return True


def antisimetricnost(listaParova:list)->bool:
    print('Antisimetrična:',end=' ')
    # za svaki (x,y) ne smije postojati (y,x) unutar liste parova osim kada je x==y
    for x,y in listaParova:
        if x==y: continue
        trazeniE = (y,x)
        if trazeniE in listaParova:
            print(f'NE jer za {formatStr((x,y))} postoji {formatStr(trazeniE)} unutar liste parova')
            return False
    print('DA')
    return True   


def unosPodataka():
    elementiSkupa = input('Unesite elemente skupa A u jednoj liniji\nodvajajuci ih zarezom (npr. f,g,d,e,r,t):')
    global skupA
    skupA = list(set(elementiSkupa.split(',')))
    n = int(input('Koliko parova želite unijeti?:'))
    #unos n broja parova u glavnu listu (listaParova)
    print('Unesite članove para odvojene zarezom.(npr. 1. PAR:a,b)')
    for i in range(n):
        par = input(f'{i+1}. PAR:')
        par = tuple(par.split(','))
        listaParova.append(par)
    print('Unešeni parovi su:')
    print(formatStr(listaParova))
    #ispis skupa
    print(f'Skup A = {skupA}')
    #graficki prikaz relacije
    graficki(listaParova,skupA)


def graficki(listaParova,skupA):
    skupA.sort()
    print('  ',end='')

    #header tablice
    for e in skupA:
        print(e,end=" ")
    print(' ')
    #sadrzaj tablice
    for e in skupA:
        redak = e
        elementiRetka = [el[1] for el in listaParova if el[0]==e] 
        for y in skupA:
            jednak = False
            for i in elementiRetka:
                if i == y: 
                    redak = redak + ' x'
                    jednak = True
                    break
            if not jednak: redak = redak + ' .'
        print(redak)
    

def mainFunc():
    unosPodataka()
    if not provjeraUnosa(listaParova,skupA): return

    print("\nBinarna relacija je:\n")
    #testiranje tranzitivnosti
    tranzitivna = tranzitivnost(listaParova)

    #testiranje refleksivnosti i antirefleksivnosti
    refleksivna = refleksivnost(skupA,listaParova)
    if refleksivna: 
        print('Antirefleksivna: NE jer je refleksivna')
        antirefleksivna = False
    else: antirefleksivna = antirefleksivnost(skupA,listaParova)

    #testiranje antisimetričnosti
    antisimetrična = antisimetricnost(listaParova)

    #testiranje simetričnosti i asimetričnosti
    if antisimetrična:
        print('Simetrična: NE jer je antisimetrična')
        simetricna = False
    else: simetricna = simetricnost(listaParova)

    if simetricna: print('Asimetrična: NE jer je simetrična')
    
    #asimetrična je ako je antisimetrična i antirefleksivna
    if antisimetrična and antirefleksivna: print('Asimetrična: DA jer je antisimetrična i antirefleksivna')
    else: print('Asimetrična: NE jer nije antirefleksivna')

    #ispitivanje ekvivalencije
    if refleksivna and simetricna and tranzitivna: print('Relacija ekvivalencije: DA - Relacija je tranzitivna,simetrična i refleksivna')



mainFunc()
input('\nPritisnite ENTER za kraj programa')

#TO-DO:
#funkcijska
#totalni i strogi uređaj