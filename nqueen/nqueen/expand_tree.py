from arbol import Nodo

def expand(current_state:Nodo):
    expanded_nodes:list[Nodo] = []
    # Copia el estado actual y coloca el nuevo valor en la posición válida
    for index in range(len(current_state.dato)):
        new_state = Nodo(current_state.dato.copy(),current_state)
        if new_state.dato[index] < len(current_state.dato)-1:
            new_state.dato[index]+=1
            expanded_nodes.append(new_state)
    return expanded_nodes

def expand_gs(current_state:list[int]):
    expanded_nodes:list[list[int]]=[]

    cantidad_elementos = len(current_state)
    for i in range(cantidad_elementos): # columna 
        for j in range(cantidad_elementos): # renglon
            if j != current_state[i]:
                estado = current_state.copy()
                estado[i] = j
                expanded_nodes.append(estado.copy())
                

    menores = sorted([(goal_test(e),e) for e in expanded_nodes])
    
    return menores[0][1]

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
    return ataques

print(expand_gs([0,2,3,1]))
