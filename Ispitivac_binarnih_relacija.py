set1 = (('b','b'),('c','b'),('c','d'),('e','b'),('e','d'),('e','f'))
set2 = (('b','b'),('c','b'),('c','d'),('e','b'),('e','d'),('e','f'),('f','b'))
set3 = (('b','b'),('c','b'),('c','d'),('e','b'),('e','d'),('e','f'),('a','e'))
set4 = (('b','b'),('c','b'),('c','d'),('e','b'),('e','d'),('e','f'))
set5 = (('b','b'),('c','b'),('c','d'),('e','b'),('e','d'),('e','f'))

def searchTuple(element,myTuple):  
    return element in myTuple

def tranzitivnost(A):
  for par in A:
    if par[0]==par[1]: continue
    B = tuple(e for e in A if e[0]==par[1])
    if len(B) == 0: continue
    for e in B:
      trazeni = (par[0],e[1])
      if not searchTuple(trazeni,A): return False
  return True
      


print("Funkcija JE tranzitivna") if tranzitivnost(set1) else print("Funkcija NIJE tranzitivna")
print("Funkcija JE tranzitivna") if tranzitivnost(set2) else print("Funkcija NIJE tranzitivna")
print("Funkcija JE tranzitivna") if tranzitivnost(set3) else print("Funkcija NIJE tranzitivna")