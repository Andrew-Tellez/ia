from csv import reader

from persona import Persona


def leer_archivo(archivo):
    lista: list[Persona] = []
    with open(archivo) as f:
        lectura = reader(f)
        for row in lectura:
            nombre, peso, estatura = row  
            lista.append(Persona(nombre, int(peso), float(estatura)))
        return lista

def merge_sort(elementos,key)->list[Persona]:
    if len(elementos) <= 1:
        return elementos

    medio = len(elementos) // 2
    izquierda = elementos[:medio]
    derecha = elementos[medio:]

    lista_izquierda = merge_sort(izquierda, key)
    lista_derecha = merge_sort(derecha, key)
    elementos = merge(lista_izquierda, lista_derecha,key)

    return elementos

def merge(izquierda, derecha,key):
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            if getattr(izquierda[i], key) < getattr(derecha[j], key):
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

class Lista:
    def __init__(self, elementos,key="nombre"):
        self.elementos = elementos
        self.key = key

    def insertar(self,persona:Persona):
        if self.existe(persona):  
            print("la persona ya existe")
        else:
            i = 0
            while i < len(self.elementos)and getattr(persona,self.key) > getattr(self.elementos[i],self.key):
                i+=1
            self.elementos.insert(i,persona)

    def remover(self,persona:Persona):
        if self.existe(persona):
            self.elementos.remove(persona)
        else:
            print("no existe la persona")

    def existe(self,persona:Persona)->bool:
        if persona in self.elementos:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"{self.elementos}"
