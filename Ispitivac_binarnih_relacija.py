
listaParova = []
import re


# funkcija koja iz stringa uklanja znakove [] i ' npr. [('a','b')] ispisati će kao (a, b)    
def formatStr(s)->str:
    return str(s).replace("'","").strip('[]')

#funkcija koja provjerava tranzitivnost binarne relacije
def tranzitivnost(A:list)->bool:
    for element in A:
        #ako su x i y jednaki testiraj dalje (funkcija je tranzitivna)
        if element[0]==element[1]: continue
        #napravi novu listu svih elemenata čiji je prvi član jedank drugom članu trenutnog elementa
        B = list(e for e in A if e[0]==element[1])
        #ako je lista prazna, nije pronađen niti jedan takav element, nastavi testiranje idućeg člana
        if len(B) == 0: continue
        #ispitaj postoji li u orignialnoj listi A implicirani član (ako su xRy i yRz, postoji li xRz)
        for e in B:
            implicElement = (element[0],e[1])
            # ako takav element nije pronađen funkcija nije tranzitivna - vrati False inače vrati True
            if not implicElement in A: 
                print(f"Funkcija NIJE tranzitivna jer za {formatStr(element)} i {formatStr(e)} ne postoji {formatStr(implicElement)} unutar skupa A")
                return False
    print("Funkcija JE tranzitivna")
    return True
      


def unosPodataka():
    n = int(input('Koliko parova želite unijeti?:'))
    #unos n broja parova u glavnu listu (listaParova)
    for i in range(n):
        print(f'#{i+1} PAR')
        x = input(f'(_,y):')
        y = input(f'({x},_):')
        listaParova.append((x,y))
    print('Unešeni parovi su:')
    print(formatStr(listaParova))
    #na temelju unešenih parova ispisuje se skup svih članova 
    skupA = set(re.findall("[a-zA-z0-9]",formatStr(listaParova)))
    print(f'Skup A = {skupA}')

#pozivi funkcija
unosPodataka()
tranzitivnost(listaParova)