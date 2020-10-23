from .particula import Particula
import json

class AdminParticula:
    def __init__(self):
        self.__lista = []
        
    def agregar_inicio(self, particula:Particula):
        self.__lista.insert(0, particula)
    
    def agregar_final(self, particula:Particula):
        self.__lista.append(particula)
    
    def mostrar(self):
        for particula in self.__lista:
            print(particula)
            
    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__lista
        )
    
    def guardar(self, ubicacion):
        try: #validar que se pudo hacer 
            with open(ubicacion, 'w') as archivo: #Escribir en el archivo
                lista = [par.to_dic() for par in self.__lista]
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
                #los parametros del diccionario a parametros validos con ayuda del constructor
            return 1
        except:
            return 0

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