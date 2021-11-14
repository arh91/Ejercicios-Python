'''
Created on 27 abr. 2020

@author: PackardBell
'''

class Cliente():
    
    def __init__(self,nombre,telefono,ciudad):
        self.nombre = nombre
        self.telefono = telefono
        self.ciudad = ciudad
    
         
    def ObtenerPrefijo(self):
        prefijo = ""
        telefono = str(self.telefono)
        t = list(telefono)
        
        for indice in range(3):           
            prefijo += t[indice]
                   
        print("El prefijo es "+prefijo)
        
        
    def ImprimirDatos(self):
        datos = ("El nombre del cliente es {}, el telefono es {} y la ciudad es {}")
        print(datos.format(self.nombre, self.telefono, self.ciudad))
        