import random
import numpy as np
#base: contiene las clases y funciones para definir algoritmos ecolutivos
#creator: permite crear tipos de datos personalizados para los individuos y sus funciones de aptitud
#tools: proporciona las herramientas para la seleccion, cruce, mutacion y evaluacion de individuos
from deap import creator, base, tools, algorithms

#Se define los tipos de individuos y la funcion de aptitud(fitness)
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

#tamaño de la carpinteria
n = 16
#Configurar el toolbox para definir operadores geneticos
def inicializacion_personalizada(icls,rango_valores,longitud_cromosoma):
    cromosoma = [0] * longitud_cromosoma  # Inicializar cromosoma con ceros
    
    estaciones_estaticas = { 0: 11, 8: 9, 11: 10, 12: 8 }
   
    for i,v in zip(estaciones_estaticas.keys(),estaciones_estaticas.values()):
        cromosoma[i] = v
       # Asignar valores del 1 al 7 de forma aleatoria
    # valores_1_al_7 = list(range(rango_valores[0],rango_valores[1]+1))
    
    # random.shuffle(valores_1_al_7)
    for i in range(longitud_cromosoma):
        if i not in estaciones_estaticas.keys():
            cromosoma[i] = np.random.randint(1,8) # se asigna un valor aleatorio del 1 al 7  
    return icls(cromosoma)


toolbox = base.Toolbox()
toolbox.register("individual", inicializacion_personalizada, creator.Individual, rango_valores=(1, 7), longitud_cromosoma=n-1)
toolbox.register("poblacion", tools.initRepeat, list, toolbox.individual) #para generar los individuos

# Definir la función de mutación personalizada
def mutacion_personalizada(individual,indpb):
    # Solo mutar los valores del 1 al 7 
    for i in range(len(individual)):
        if i not in [0,8,11,12]:
            if random.random() < indpb:
                individual[i] = random.randint(1, 7)
    return individual

def fitness(vector):
    #x= ((pos_estacion % 4)+0.5)*2 obtener x
    #y= ((pos_estacion // 4)+0.5)*2 obtner y 
    recorrido = [(1,8),(8,1),(1,4),(4,5),(5,3),(3,4),(4,3),(3,1),(1,9),(9,1),(1,3),(3,1),(1,10)]
    distancia_manhattan = 0
    # if not 8 in vector: 
    for i in range(len(vector)):
        for coordenada in recorrido: 
            if vector[i] == coordenada[0]: #validar si la estacion actual se mueve a otra
                moverse_a = coordenada[1] #obtener la estacion a donde se movera
                
                #Calcular x1, y1, de la estacion que esta
                x1 = ((i % 4) + 0.5) * 2
                y1 = ((i // 4) + 0.5) * 2
                
                #Calcular x2, y2 de la estacion a la que se movera
                pos_mover = vector.index(moverse_a) #obtener la posicion en la carpinteria de la estacion 
                x2 = ((pos_mover % 4) + 0.5) * 2
                y2 = ((pos_mover // 4) + 0.5) * 2
                
                #Calcular la distancia manhattan entre las estaciones
                distancia_manhattan = distancia_manhattan + np.abs(x1-x2) + np.abs(y1-y2)
    return distancia_manhattan

toolbox.register("evaluacion", fitness) #Se registra la funcion de evaluacion (GoalTest)
toolbox.register("mate", tools.cxTwoPoint) #Registra el operador de cruce de dos puntos
toolbox.register("mutate", mutacion_personalizada,indpb=0.6) #Registra el operador de mutacion
toolbox.register("seleccion", tools.selTournament, tournsize=8) #Registra el operador de seleccion de torneo

#Se configura la poblacion inicial de n individuos
poblacion = toolbox.poblacion(n=10000)

numero_de_generaciones=500
for gen in range(numero_de_generaciones):
    print(f"Generacion {gen + 1}/{numero_de_generaciones}")
    #Generamos la desendencia
    #cxpb = probabilidad de cruce
    #mutpb = probabilidad de mutacion
    desendencia = algorithms.varAnd(poblacion, toolbox, cxpb=0.1, mutpb=0.1)
    
    #Evaluamos la desendencia
    aptitudes = toolbox.map(toolbox.evaluacion, desendencia)
    
    #Asignamos la aptitud a cada desendiente
    for aptitud, ind in zip(aptitudes, desendencia):
        #Asignamos los valores de aptitud calculados de cada individuo
        ind.fitness.values = aptitud
    
    #Seleccionamos los individuos de la siguiente generacion
    poblacion = toolbox.seleccion(desendencia, k=len(poblacion))
    
    #print el mejor individuo de la generacion
    top_ind = tools.selBest(poblacion, k=1)[0]
    print(f"Top individual of generation {gen + 1}: {top_ind}, Fitness: {top_ind.fitness.values[0]}")

#Se seleccionan los 10 mejores de la poblacion
# Select the top 10 individuals from the final population
top10 = tools.selBest(poblacion, k=10)
print("\nTop 10 individuals:")
for i, ind in enumerate(top10, 1):
    print(f"#{i}: {ind}, Fitness: {ind.fitness.values[0]}")
