import sys
import time
sys.setrecursionlimit(100000000)
class Nodo:
    def __init__(self,estado:list[list[int]],g:int,h:int) -> None:
        self.estado = estado
        self.h = h
        self.g = g 
        self.f = g + h
    def __repr__(self) -> str:
        return f"""({self.estado},{self.f})"""

prueba = [[2,1,3],[4,0,6],[5,7,8]]
meta = [[1,2,3],[4,5,6],[7,8,0]]
bl :list[list[list[int]]] = []
lista_de_nodos:list[Nodo] = [Nodo(prueba,0,0)]

def goal_test(ea:Nodo):
    return ea.estado == meta

def diferentes_posiciones(ea:list[list[int]]):
    contador = 0
    for i in range(len(ea)):
        for j in range(len(ea)):
            if ea[i][j] != meta[i][j]:
               contador += 1
    return contador

def encontrar_cero(ea:Nodo):
    for i in range(len(ea.estado)):
        for j in range(len(ea.estado)):
            if ea.estado[i][j] == 0:
                return i , j
    return [-1,-1]

def expand(ea:Nodo):
    g = ea.g
    hijos:list[Nodo] = []
    renglon , columna =  encontrar_cero(ea) 
    if renglon > 0:
        nuevo_estado = intercambiar(ea, renglon, columna, renglon - 1, columna)
        h = diferentes_posiciones(nuevo_estado)
        if not esta_creado(nuevo_estado):  
            hijos.append(Nodo(nuevo_estado,g+1,h))
            bl.append(nuevo_estado)

    if renglon < 2:
        nuevo_estado = intercambiar(ea, renglon, columna, renglon + 1, columna)
        h = diferentes_posiciones(nuevo_estado)
        if not esta_creado(nuevo_estado):  
            hijos.append(Nodo(nuevo_estado,g+1,h))
            bl.append(nuevo_estado)

    if columna > 0:
        nuevo_estado = intercambiar(ea, renglon, columna, renglon, columna - 1)
        h = diferentes_posiciones(nuevo_estado)
        if not esta_creado(nuevo_estado):  
            hijos.append(Nodo(nuevo_estado,g+1,h))
            bl.append(nuevo_estado)

    if columna < 2:
        nuevo_estado = intercambiar(ea, renglon, columna, renglon, columna + 1)
        h = diferentes_posiciones(nuevo_estado)
        if not esta_creado(nuevo_estado):  
            hijos.append(Nodo(nuevo_estado,g+1,h))
            bl.append(nuevo_estado) 
    return hijos


def intercambiar(ea:Nodo,fila_vacia,col_vacia,fila_nueva,columna_nueva):
    nuevo_estado = [fila.copy() for fila in ea.estado]
    nuevo_estado[fila_vacia][col_vacia], nuevo_estado[fila_nueva][columna_nueva] = nuevo_estado[fila_nueva][columna_nueva], nuevo_estado[fila_vacia][col_vacia]
    return nuevo_estado

def esta_creado(ea):
    for e in bl:
        if e == ea:
            return True
    return False

def a_estrella(f:list[Nodo]):
    if len(f) == 0:
        print(f"solucion no encontrada")
        return 
    ea = f.pop(0)
    print("nodo actual: ",ea)
    if goal_test(ea):
        print(f"solucion encontrada en {ea}")
        return
    os = expand(ea)
    os = sorted(os,key=lambda e: e.f) 
    f.extend(os) 
    # print(f)
    # time.sleep(2)
    a_estrella(f)

f = lista_de_nodos
a_estrella(f)


