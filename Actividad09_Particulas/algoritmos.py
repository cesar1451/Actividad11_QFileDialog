import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt(pow((x_2 - x_1), 2) + pow((y_2 - y_1), 2))

def busqueda_profundidad(grafo, origen):
    #Inicialización de listas
    visitados = []
    pila = []
    recorrido = []
    
    visitados.append(origen)
    pila.append(origen)
    
    #mientras la pila no este vacía
    while pila:
        vertice = pila.pop()
        recorrido.append(vertice)
        
        adyacentes = grafo[vertice]
        for adyacente in adyacentes:
            ady = adyacente[0]
            if ady not in visitados:
                visitados.append(ady)
                pila.append(ady)
                
    #print("Profundidad: ", recorrido) 
    return recorrido
   
def busqueda_amplitud(grafo, origen):
    visitados = []    
    cola = []
    recorrido = []
    
    visitados.append(origen)
    cola.append(origen)
    
    while cola:
        vertice = cola.pop(0)
        recorrido.append(vertice)
    
        adyacentes = grafo[vertice]
        for adyacente in adyacentes:
            ady = adyacente[0]
            if ady not in visitados:
                visitados.append(ady)
                cola.append(ady)
    
    #print("Amplitud: ", recorrido)
    return recorrido
    
    
    
    
    
    
