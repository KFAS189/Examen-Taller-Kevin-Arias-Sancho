"""
Kevin Arias Sancho
2019209063
link de github:

"""

#1
def combinaciones(H, D):
    if isinstance (H, list) and (D, list):
        return combinaciones2(H, D)
    else:
        return "error"
def combinaciones2(H, D):
    if D == []:
        return combinaciones3(H)
    else:
        return [H[0] + D[0]] + combinaciones2( H, D[1:])
def combinaciones3(H):
    if H == []:
        return []
    else:
        return combinaciones2(H[1:], D)

#2
from math import sqrt
def std(lista, avg):
    if isinstance (lista, list):
        return std_aux(lista, avg)
    else:
        return "error"
def std_aux(lista, avg):
    if lista == []:
        return []
    else:
        return sqrt((((lista[0] - avg)**2)/len(lista)-1)+std_aux(lista[1:], avg))

#3
def zScore(listaX, S, avg):
    if isinstance (listaX, list):
        return zScore_aux(listaX, S, avg)
    else:
        return "error"
def zScore_aux(listaX, S, avg):
    if ListaX == []:
        return[]
    else:
        return[(listaX[0]-avg)/S]+ zScore_aux(listaX[1:], S, avg)
    
    
#4
def rScore(Zx, Zy):
    if len(Zx) == len(Zy):
        return rScore_aux(Zx, Zy, len(Zx))
    return "error"
def rScore_aux(Zx, Zy, n):
    if n == 1:
        return "error"
    if Zx == []:
        return []
    if Zy == []:
        return []
    else:
        return ((Zx[0]*Zy[0])/n-1)+ rScore_aux(Zx[1:], Zy[1:], n)
