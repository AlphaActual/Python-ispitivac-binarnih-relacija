
import re

listaParova = list()
skupA = list()


# Relacija koja iz stringa uklanja znakove [] i ' npr. [('a','b')] ispisati će kao (a, b)    
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
    for element in listaParova:
        #ako su x i y jednaki testiraj dalje (Relacija je tranzitivna)
        if element[0]==element[1]: continue
        #napravi novu listu svih elemenata čiji je prvi član jedank drugom članu trenutnog elementa
        B = list(e for e in listaParova if e[0]==element[1])
        #ako je lista prazna, nije pronađen niti jedan takav element, nastavi testiranje idućeg člana
        if len(B) == 0: continue
        #ispitaj postoji li u orignialnoj listi A implicirani član (ako su xRy i yRz, postoji li xRz)
        for e in B:
            implicElement = (element[0],e[1])
            # ako takav element nije pronađen Relacija nije tranzitivna - vrati False inače vrati True
            if not implicElement in listaParova: 
                print(f"Relacija NIJE tranzitivna jer za {formatStr(element)} i {formatStr(e)} ne postoji {formatStr(implicElement)} unutar liste parova")
                return False
    print("Relacija JE tranzitivna")
    return True

def refleksivnost(skupA:list,listaParova:list)->bool:
    # za svaki x ∈ skupa A u mora postojati (x,x) u listi parova 
    for element in skupA:
        trazeniE = (element[0],element[0])
        if not trazeniE in listaParova:
            print(f'Relacija NIJE refleksivna jer za element "{element}" ne postoji par {formatStr(trazeniE)} unutar liste parova')
            return False
    print("Relacija JE refleksivna")
    return True

def antirefleksivnost(skupA:list,listaParova:list)->bool:
    # za svaki x ∈ skupa A u NE SMIJE postojati (x,x) u listi parova 
    for element in skupA:
        trazeniE = (element[0],element[0])
        if trazeniE in listaParova:
            print(f'Relacija NIJE antirefleksivna jer za element "{element}" postoji par {formatStr(trazeniE)} unutar liste parova')
            return False
    print("Relacija JE antirefleksivna")
    return True


def simetricnost(listaParova:list)->bool:
    for element in listaParova:
        if element[0] == element[1]: continue
        trazeniE = (element[1],element[0])
        if not trazeniE in listaParova:
            print(f'Relacija NIJE simetrična jer za {formatStr(element)} ne postoji {formatStr(trazeniE)} unutar liste parova')
            return False
    print('Relacija JE simetrična')
    return True
      


def unosPodataka():
    elementiSkupa = input('Unesite elemente skupa A u jednoj liniji odvajajuci ih zarezom (npr. f,g,d,e,r,t):')
    global skupA
    skupA = list(set(elementiSkupa.split(',')))
    n = int(input('Koliko parova želite unijeti?:'))
    #unos n broja parova u glavnu listu (listaParova)
    print('Unesite članove para odvojene zarezom.(npr. #1 PAR:a,b)')
    for i in range(n):
        par = input(f'{i+1}. PAR:')
        par = tuple(par.split(','))
        listaParova.append(par)
    print('Unešeni parovi su:')
    print(formatStr(listaParova))
    #ispis skupa
    print(f'Skup A = {skupA}')
    



def mainFunc():
    unosPodataka()
    if not provjeraUnosa(listaParova,skupA): return

    tranzitivnost(listaParova)

    refleksivna = refleksivnost(skupA,listaParova)
    if refleksivna: print('Funkcija NIJE antirefleksivna')
    else: antirefleksivnost(skupA,listaParova)

    simetricna = simetricnost(listaParova)
    if simetricna: print('Relacija NIJE asimetrična')
    #else asimetričnost()


mainFunc()
input('Pritisnite ENTER za kraj programa')