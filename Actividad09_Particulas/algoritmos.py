import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt(pow((x_2 - x_1), 2) + pow((y_2 - y_1), 2))

def busqueda_profundidad(grafo, origen):
    visitados = []
    pila = []
    recorrido = []
    
    visitados.append(origen)
    pila.append(origen)
    
    while pila:
        vertice = pila[-1]
        recorrido.append(vertice)
        pila.pop()
        
        for key, value in grafo.items():
            if key not in visitados:
                visitados.append(key)
                pila.append(key)
                
    #print("Profundidad: ", recorrido) 
    return recorrido
   
def busqueda_amplitud(grafo, origen):
    visitados = []    
    cola = []
    recorrido = []
    
    visitados.append(origen)
    cola.append(origen)
    
    while cola:
        #print("Recorrido: ", recorrido)
        vertice = cola[0]
        recorrido.append(vertice)
        cola.pop(0)
        
        for key, value in grafo.items():
            if key not in visitados:
                visitados.append(key)
                cola.append(key)
    
    #print("Amplitud: ", recorrido)
    return recorrido
    
    
    
    
    
    
