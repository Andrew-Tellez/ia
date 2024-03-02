from lista import leer_archivo, Lista, merge_sort
from persona import Persona


key = "nombre"
nombre: str = ""
peso: int = 0
estatura: float = 0.0
archivo: str = "edt/personas.csv"
opcion: str = ""

lista_de_personas = leer_archivo(archivo)
orden = merge_sort(lista_de_personas, key)
lista = Lista(orden, key)
while True:
    print(
        "opciones : insertar(i),remover(r),ordenar(o),desplegar elementos(d),salir(s)\n"
    )
    opcion = input("ingrese una de las opciones: ")
    if opcion == "i":
        nombre = input("coloque el nombre completo: ")
        peso = int(input("coloque la peso: "))
        estatura = float(input("coloque la estatura: "))
        lista.insertar(Persona(nombre, peso, estatura))
        print("\n")
    if opcion == "r":
        nombre = input("coloque el nombre completo: ")
        peso = int(input("coloque la peso: "))
        estatura = float(input("coloque la estatura: "))
        lista.remover(Persona(nombre, peso, estatura))
        print("\n")
    if opcion == "o":
        key = input(
            "coloque el criterio de ordenamiento ('nombre','peso','estatura'): "
        )
        orden = merge_sort(lista.elementos, key)
        lista.elementos = orden
        print("\n")
    if opcion == "d":
        print(lista)
        print("\n")
    if opcion == "s":
        break
