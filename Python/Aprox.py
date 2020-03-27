#!/usr/bin/env python

objective = int(input('Escoje un numero: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objective) >= epsilon and respuesta <= objective:
    respuesta += paso

if abs(respuesta**2 - objective) >= epsilon:
    print(f'No se encontro la raiz de {objective}')
else:
    print(f'La raiz cuadrada de {objective} es {respuesta}')