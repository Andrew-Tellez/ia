from expand_tree import expand, expand_gs
from arbol import Nodo
import sys

sys.setrecursionlimit(1000000)

def goal_test(reinas:list[int]):
    ataques : int = 0
    for i in range(0,len(reinas)-1):
        for j in range(i+1,len(reinas)):
            if reinas[i] == reinas[j]: # horizontal
                # print(f"horizotal {i}=={j}")
                ataques += 2
            if abs(i-j) == abs(reinas[i]-reinas[j]): # diagonal
                # print(f"diagonal {i}|{j}")
                ataques += 2
    return ataques==0

def bfs(f:list[Nodo]):
    if len(f) == 0:
        print("solucion no encontrada")
        return None

    ea = f.pop(0)
    if goal_test(ea.dato):
        print(f"solucion encontrada {ea.dato}")
        cadena = f"{ea.dato}-->"
        while ea.padre is not None:
            cadena += f"{ea.padre.dato}-->"
            ea = ea.padre
        print(cadena)
        return  
            
    f.extend(expand(ea))
    bfs(f)

def dfs(f:list[Nodo]):    
    if len(f) == 0:
        print("solucion no encontrada")
        return None

    ea = f.pop(0)
    if goal_test(ea.dato):
        print(f"solucion encontrada {ea.dato}")
        cadena = f"{ea.dato}-->"
        while ea.padre is not None:
            cadena += f"{ea.padre.dato}-->"
            ea = ea.padre
        print(cadena)
        return  

    f[0:0] = expand(ea)
    dfs(f)

raiz= Nodo([0,0,0,0])

def ldfs(F:list[Nodo], nivel:int, limite:int):
    if len(F) == 0:
        print("Solucion no encontrada")
        return False
    
    estado_actual = F.pop(0)
    
    if goal_test(estado_actual.dato):
        print("Solucion encontrada: ", estado_actual.dato)
        return True
        
    if (nivel < limite-1):
        F[0:0] = expand(estado_actual)
        nivel += 1
    else:
        print("Se llego al limite, comienza la siguiente iteracion ", limite)
        return False
    
    return ldfs(F, nivel, limite)

limite = 1000
# while(True):
#     solucion = ldfs([raiz], nivel=0, limite=limite)
    
#     if (solucion):
#         break

#     # se reinicia el arreglo
#     raiz = Nodo([0,0,0,0])

#     # incremento para la próxima iteración
#     limite += 10000

def gs(f:list[Nodo]):
    if len(f) == 0:
        print("NO se encontró la solucion")
        return
    ea = f.pop(0)
    if goal_test(ea.dato):
        print("solucion encontrada en",ea.dato)
        return
    mejor_hijo = expand_gs(ea.dato)
    gs([Nodo(mejor_hijo)])

gs([Nodo([1,0,0,2])])
