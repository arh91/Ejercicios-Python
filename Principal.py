'''
Created on 27 abr. 2020

@author: PackardBell
'''
from Cliente import Cliente

def main():
 
                
    nombre = input("Introduzca el nombre")
    telefono = int(input("Introduzca el telefono"))
    ciudad = input("Introduzca la ciudad")
    
      
    cliente = Cliente(nombre,telefono,ciudad)
    
    tecla = int(input("Pulse la tecla 1 para ver el prefijo del telefono del cliente."+"%s"+" Pulse 2 si quiere ver los datos del cliente."))
    
    if tecla==1:
        cliente.ObtenerPrefijo()
    else:
        cliente.ImprimirDatos()
        

main()