#!/usr/bin/env python

import os
import Algorithms as alg
def main():
    os.system("clear")
    try:
        print(f'Bienvenido \nEste programa retornara la raiz cudrada de algun numero \n Se puede elegir entre diferentes algoritmos para llevar a cabo la tarea')

        print('Algoritmos: \n1.-Busqueda Binaria\n2.-Enumeracion exhaustiva\n3.-Aproximacion de soluciones')

        objetivo = int(input("Escriba el numero del que desea obtener la raiz cuadrada: \n>>"))
        
        algoritmo = int(input('Que algoritmo quiere usar? \n>>'))

        if algoritmo == 2:
            alg.Enum(objetivo)

        elif algoritmo == 3:
            alg.Aprox(objetivo)
            
        elif algoritmo >= 4:
            print("Por favor escoge una opcion de algoritmo valido!")
            
        else:
            alg.Binary(objetivo)

        repeat = input('Quiere repetir la operacion (Y/n)?')
        if repeat.upper() == 'Y':
            main()
        else:
            os.system("clear")
            exit()

    except ValueError:
        print(f'Por favor, introduce los valores requeridos!')

repeat = 'N'
if __name__=='__main__':
    main()
