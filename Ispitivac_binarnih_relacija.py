import re
import random
import time

###___SPREMISTA_PODATAKA___
listaParova = list()
skupA = list()


###___POMOCNE_FUNKCIJE___

#Funkcija koja iz stringa uklanja znakove [] i ' npr. [('a','b')] ispisati ce kao (a, b)    
def formatStr(s)->str:
    return str(s).replace("'","").strip('[]')

def randomSlovo(slova)->str:
    return random.choice(slova)

# Funkcija koja provjerava jesu li parovi relacije sastavljeni od elemenata skupa koji korisnik unosi
def provjeraUnosa(listaParova:list,skupA:list)->bool:
    određeniElementi = list(set(re.findall("[a-zA-z0-9]",formatStr(listaParova))))
    provjera =  all(item in skupA for item in određeniElementi)
    if not provjera:
        print('Pogreska! Uneseni elementi skupa ne odgovaraju elementima unutar unesenih parova.') 
        return False
    return True

def unosPodataka():
    # ukloni prethodne unose (ako ih ima)
    global skupA
    global listaParova
    listaParova.clear()
    skupA.clear()

    elementiSkupa = input('Unesite elemente skupa A u jednoj liniji\nodvajajući ih zarezom (npr. f,g,d,e,r,t):')
    skupA = list(set(elementiSkupa.split(',')))
    n = int(input('Koliko parova zelite unijeti?:'))
    #unos n broja parova u glavnu listu (listaParova)
    print('Unesite oba clana para odvojena zarezom.')
    for i in range(n):
         par = input(f'{i+1})PAR:')
         par = tuple(par.split(','))
         listaParova.append(par)
    
    
def ispisUlaznihPodataka():
    print('\nUneseni parovi su:')
    print(formatStr(listaParova))
    #ispis skupa
    stringSkupa = str(skupA).replace("[","{").replace("]","}")
    print(f'\nSkup A = {stringSkupa}')

    #ispis u file
    with open('Relacije.txt', 'a') as f:
        print('\nUneseni parovi su:', file=f)
        print(formatStr(listaParova), file=f)
        print(f'\nSkup A = {stringSkupa}', file=f)
    #graficki prikaz relacije
    graficki(listaParova,skupA)

def welcome():
    #vremenska oznaka
    seconds = time.time()
    local_time = time.ctime(seconds)
    
    with open('Relacije.txt', 'a') as f:
        print("__________Dobrodosli u Ispitivac binarnih relacija v1.0__________".center(65, ' '))
        print("\nLokalno vrijeme:", local_time, file=f)
        print("__________Dobrodosli u Ispitivac binarnih relacija v1.0__________".center(65, ' '), file=f)




#funkcija koja graficki iscrtava elemente binarne relacije
def graficki(listaParova:list,skupA:list):
    with open('Relacije.txt', 'a') as f:

        skupA.sort()
        print()
        print("", file=f)
        print('  ',end='')
        print('  ',end='', file=f)

        #header tablice
        for e in skupA:
            print(e,end=" ")
            print(e,end=" ", file=f)
        print(' ')
        print(' ', file=f)
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
            print(redak, file=f)
        

def uredjivanjeParova():
    global skupA
    global listaParova
    while (True):
        odabir = input("\nZelite li editirati parove binarne relacije?(da/ne):")
        if(odabir != "DA" and odabir != "da" and odabir != "Da"): break
        else:
            while(True):
                odabir = int(input("Zelite li: 1) dodati nove parove ili 2) obrisati pojedine parove:"))
                if(odabir == 1 or odabir == 2): break
            if(odabir == 1):
                parovi = input("Unesite parove koje Zelite DODATI u ovom formatu (x,y) (x,z) (z,x):")
                parovi = parovi.split() #lista stringova, potrebno je pretvoriti ju u listu tuople parova
                noviParovi = list()
                for item in parovi:
                    noviParovi.append((item[1],item[3]))
                #provjeri odgovaraju li uneseni parovi elementima zadanog skupa
                if provjeraUnosa(noviParovi,skupA): 
                    listaParova = listaParova + noviParovi
                    ispisUlaznihPodataka()
                    ispitivanjeRelacija()
            elif(odabir == 2):
                parovi = input("Unesite parove koje Zelite OBRISATI u ovom formatu (x,y) (x,z) (z,x):")
                parovi = parovi.split() #lista stringova, potrebno je pretvoriti ju u listu tuople parova
                noviParovi = list()
                for item in parovi:
                    noviParovi.append((item[1],item[3]))
                #provjeri odgovaraju li uneseni parovi elementima zadanog skupa
                if provjeraUnosa(noviParovi,skupA):
                    #brisanje iz liste
                    for item in noviParovi:
                        if item in listaParova:
                            listaParova.remove(item)
                    ispisUlaznihPodataka()
                    ispitivanjeRelacija()


###___IZBORNIK___

def GlavniIzbornik()-> int:
    opcije = ("1. Unos novog skupa i parova binarne relacije\n"
              "2. Generiranje nasumicnog skupa i relacije nad njime")
    print(f"{'||||||||||||Glavni Izbornik||||||||||||'.center(65, ' ')}\nOdaberite jednu od opcija:\n{opcije}")
    odabir = int(input())
    return odabir 
    
###___GLAVNE FUNKCIJE___

def tranzitivnost(listaParova:list)->bool:
    with open('Relacije.txt', 'a') as f:
        print('Tranzitivna:',end=' ')
        print('Tranzitivna:',end=' ',file=f)
        for element in listaParova:
            if element[0]==element[1]: continue
            B = list(e for e in listaParova if e[0]==element[1])
            if len(B) == 0: continue
            #ispitaj postoji li u orignialnoj listi (listaParova) implicirani clan (ako su xRy i yRz, postoji li xRz)
            for e in B:
                implicElement = (element[0],e[1])
                # ako takav element nije pronađen Relacija nije tranzitivna - vrati False inace vrati True
                if not implicElement in listaParova: 
                    print(f"NE jer za {formatStr(element)} i {formatStr(e)} ne postoji {formatStr(implicElement)} unutar liste parova")
                    print(f"NE jer za {formatStr(element)} i {formatStr(e)} ne postoji {formatStr(implicElement)} unutar liste parova",file=f)
                    return False
        print("DA")
        print("DA",file=f)
        return True


def refleksivnost(skupA:list,listaParova:list)->bool:
    with open('Relacije.txt', 'a') as f:
        print('Refleksivna:',end=' ')
        print('Refleksivna:',end=' ',file=f)
        # za svaki x ∈ skupa A mora postojati (x,x) u listi parova 
        for element in skupA:
            trazeniE = (element[0],element[0])
            if not trazeniE in listaParova:
                print(f'NE jer za element "{element}" ne postoji par {formatStr(trazeniE)} unutar liste parova')
                print(f'NE jer za element "{element}" ne postoji par {formatStr(trazeniE)} unutar liste parova',file=f)
                return False
        print("DA")
        print("DA",file=f)
        return True


def antirefleksivnost(skupA:list,listaParova:list)->bool:
    with open('Relacije.txt', 'a') as f:
        print('Antirefleksivna:',end=' ')
        print('Antirefleksivna:',end=' ',file=f)
        # za svaki x ∈ skupa A u NE SMIJE postojati (x,x) u listi parova 
        for element in skupA:
            trazeniE = (element[0],element[0])
            if trazeniE in listaParova:
                print(f'NE jer za element "{element}" postoji par {formatStr(trazeniE)} unutar liste parova')
                print(f'NE jer za element "{element}" postoji par {formatStr(trazeniE)} unutar liste parova',file=f)
                return False
        print("DA")
        print("DA",file=f)
        return True


def simetricnost(listaParova:list)->bool:
    with open('Relacije.txt', 'a') as f:
        print('Simetricna:',end=' ')
        print('Simetricna:',end=' ',file=f)
        # za svaki (x,y) mora postojati (y,x) unutar liste parova
        for element in listaParova:
            if element[0] == element[1]: continue
            trazeniE = (element[1],element[0])
            if not trazeniE in listaParova:
                print(f'NE jer za {formatStr(element)} ne postoji {formatStr(trazeniE)} unutar liste parova')
                print(f'NE jer za {formatStr(element)} ne postoji {formatStr(trazeniE)} unutar liste parova',file=f)
                return False
        print('DA')
        print('DA',file=f)
        return True


def antisimetricnost(listaParova:list)->bool:
    with open('Relacije.txt', 'a') as f:
        print('Antisimetricna:',end=' ')
        print('Antisimetricna:',end=' ',file=f)
        # za svaki (x,y) ne smije postojati (y,x) unutar liste parova osim kada je x==y
        for x,y in listaParova:
            if x==y: continue
            trazeniE = (y,x)
            if trazeniE in listaParova:
                print(f'NE jer za {formatStr((x,y))} postoji {formatStr(trazeniE)} unutar liste parova')
                print(f'NE jer za {formatStr((x,y))} postoji {formatStr(trazeniE)} unutar liste parova',file=f)
                return False
        print('DA')
        print('DA',file=f)
        return True   

def ispitivanjeRelacija():
    with open('Relacije.txt', 'a') as f:
        print("\nBinarna relacija je:\n")
        print("\nBinarna relacija je:\n", file=f)

    #testiranje tranzitivnosti
    tranzitivna = tranzitivnost(listaParova)

    #testiranje refleksivnosti i antirefleksivnosti
    refleksivna = refleksivnost(skupA,listaParova)
    if refleksivna:
        with open('Relacije.txt', 'a') as f: 
            print('Antirefleksivna: NE jer je refleksivna')
            print('Antirefleksivna: NE jer je refleksivna', file=f)
        antirefleksivna = False
    else: antirefleksivna = antirefleksivnost(skupA,listaParova)

    
    #testiranje simetricnosti
    simetricna = simetricnost(listaParova) 
    
    #testiranje antisimetricnosti
    antisimetricna = antisimetricnost(listaParova)

    #testiranje asimetričnosti
    if (simetricna):
        with open('Relacije.txt', 'a') as f:
            print('Asimetricna: NE jer je simetricna')
            print('Asimetricna: NE jer je simetricna',file=f)
    elif (antisimetricna and antirefleksivna):
        with open('Relacije.txt', 'a') as f:
            print('Asimetricna: DA jer je antisimetricna i antirefleksivna')
            print('Asimetricna: DA jer je antisimetricna i antirefleksivna',file=f)
    elif (antisimetricna and not antirefleksivna):
        with open('Relacije.txt', 'a') as f:
            print('Asimetricna: NE jer nije antirefleksivna')
            print('Asimetricna: NE jer nije antirefleksivna',file=f)
    elif (not antisimetricna and not antirefleksivna):
        with open('Relacije.txt', 'a') as f:
            print('Asimetricna: NE jer nije antirefleksivna niti antisimetricna')
            print('Asimetricna: NE jer nije antirefleksivna niti antisimetricna',file=f)
    else:
        with open('Relacije.txt', 'a') as f:
            print('Asimetricna: NE jer nije antisimetricna')
            print('Asimetricna: NE jer nije antisimetricna',file=f)
    

    
    
    with open('Relacije.txt', 'a') as f:
        #ispitivanje ekvivalencije
        if refleksivna and simetricna and tranzitivna:
            print('Relacija ekvivalencije: DA - Relacija je tranzitivna, simetricna i refleksivna')
            print('Relacija ekvivalencije: DA - Relacija je tranzitivna, simetricna i refleksivna',file=f)

        #ispitivanje relacije uređaja
        if tranzitivna and antirefleksivna and antisimetricna: 
            print('Strogi uređaj! Antirefleksivna, tranzitivna, antisimetricna')
            print('Strogi uređaj! Antirefleksivna, tranzitivna, antisimetricna',file=f)
        elif tranzitivna and refleksivna and antisimetricna:
            print('Parcijalni uređaj! Refleksivna, tranzitivna, antisimetricna')
            print('Parcijalni uređaj! Refleksivna, tranzitivna, antisimetricna',file=f)



def generirajRelaciju():
    global skupA
    global listaParova
    skupA.clear()
    listaParova.clear()

    #random broj elemenata skupa 4-7
    brElemenata = random.randrange(4, 7)
    #popunjavanje skupa A sa jedinstvenim elementima (slova od a-z)
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    while(len(skupA) != brElemenata):
        randSlovo = randomSlovo(abeceda)
        if(randSlovo in skupA): continue
        else: skupA.append(randSlovo)
    #popunjavanje liste parova binarnih relacija novim clanovima
    #broj mogućih parova je broj elemenata skupa^2
    brParova = random.randrange(1, brElemenata*brElemenata+1)
    while(len(listaParova) != brParova):
        noviPar = (randomSlovo(skupA),randomSlovo(skupA))
        if(noviPar in listaParova): continue
        else: listaParova.append(noviPar)

    

###___MAIN FUNKCIJA___

def mainFunc():
    
    
    while (True):
        odabir = GlavniIzbornik()
        if(odabir == 1 or odabir == 2): break
        else: print("Krivi odabir, pokusajte ponovo!")

    if(odabir == 1): 
        unosPodataka()
        if not provjeraUnosa(listaParova,skupA): return
        ispisUlaznihPodataka()
        ispitivanjeRelacija()
        uredjivanjeParova()
    elif(odabir == 2): 
        generirajRelaciju()
        ispisUlaznihPodataka()
        ispitivanjeRelacija()
        uredjivanjeParova()

    
    
###___POCETAK_PROGRAMA___

welcome()
while True:
    mainFunc()
    izbor = input('\nZelite li novi unos? da/ne:')
    print('\n')
    if izbor == 'NE' or izbor == 'ne' or izbor == 'Ne': break
   
input("Kraj programa! Pritisnite ENTER.")    
