#!/usr/bin/env python

def Aprox(objetivo):
    """
    Ejecuta un algoritmo de aproximacion de soluciones
    Es un poco lento y no muy recomendado
    objetivo    Integeer    Numero del cual queremos obtener la raiz

    """
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def Binary(objetivo):
    """
    Utiliza el algoritmo de busqueda binaria
    El mas efectivo de todos
    objetivo    Integeer    Numero del cual queremos obtener la raiz

    """
    epsilon = 0.0001
    bajo = 0.0
    alto = max(0.0, objetivo)
    respuesta = (alto + bajo)/ 2

    while abs(respuesta**2 - objetivo) >= epsilon:

        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def Enum(objetivo):
    """
    Hace una enumeracion exahustiva de posibles soluciones hasta encontrar la correcta
    No es muy precisa
    objetivo    Integeer    Numero del cual queremos obtener la raiz

    """
    answer = 0

    while answer**2 < objetivo:
        answer += 1
        
    if answer**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {answer}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
