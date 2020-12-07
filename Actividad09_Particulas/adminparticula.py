from .particula import Particula
import json
from pprint import pprint, pformat

class AdminParticula:
    def __init__(self):
        self.__lista = []
        self.__grafo = {}
        self.__bandera = False
        
    def agregar_inicio(self, particula:Particula):
        self.__lista.insert(0, particula)
    
    def agregar_final(self, particula:Particula):
        self.__lista.append(particula)
    
    def mostrar(self):
        for particula in self.__lista:
            print(particula)
    
    def sort_id(self):
        self.__lista.sort(key=lambda particula: particula.id)
    
    def sort_distancia(self):
        self.__lista.sort(key=lambda particula: particula.distancia, reverse=True)
        
    def sort_velocidad(self):
        self.__lista.sort(key=lambda particula: particula.velocidad)
            
    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__lista
        )
    
    def __len__(self): #sobrecargar len
        return len(self.__lista)
    
    def __iter__(self):  #Retornar contador 
        self.cont = 0
        
        return self
    
    def __next__(self): #Iterar sobre la lista para retornar un objeto particula
        if self.cont < len(self.__lista):
            particula = self.__lista[self.cont]
            self.cont += 1 
            return particula #Retornar una particula
        else:
            raise StopIteration #Mandar una exepción
    
    def guardar(self, ubicacion):
        try: #validar que se pudo hacer 
            with open(ubicacion, 'w') as archivo: #Escribir en el archivo
                lista = [par.to_dict() for par in self.__lista]
                #print(lista)
                json.dump(lista, archivo, indent=5) #Conversión al archivo json
            return 1
        except:
            return 0
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo) #Cargar los datos del archivo en la lista 
                self.__lista = [Particula(**par) for par in lista] # ** decirle que convierta 
            return 1
        except:
            return 0
    def get_grafo(self):
        return self.__grafo
    
    def mostrar_grafo(self):
        grafo = pformat(self.__grafo, indent=1)
        #print(grafo)
        return grafo
    
    def mandar_particulas_grafo(self):
        if not self.__bandera:
            for particula in self.__lista:
                self.insertar_grafo(particula)
                self.__bandera = True
    
    def insertar_grafo(self, particula:Particula):
        origen = (particula.origen_x, particula.origen_y)
        destino = (particula.destino_x, particula.destino_y)
        
        arista_o_d = (destino, particula.distancia)
        arista_d_o = (origen, particula.distancia)
        
        if origen in self.__grafo:
            self.__grafo[origen].append(arista_o_d)
        else:
            self.__grafo[origen] = [arista_o_d]
        if destino in self.__grafo:
            self.__grafo[destino].append(arista_d_o)
        else:
            self.__grafo[destino] = [arista_d_o]
        

'''
p01 = Particula(1, 21, 15, 11, 5, 60, 100, 0, 255, 211.7)
p02 = Particula(2, 15, 90, 6, 55, 43, 0, 0, 100, 12.43)
p03 = Particula(3, 34, -41, 22, -5, 90, 255, 0, 200, 92.4)

admin = AdminParticula()
admin.agregar_final(p01)
admin.agregar_inicio(p02)
admin.agregar_inicio(p03)
admin.mostrar()
'''
