from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    
#exp = raw_input("ingrese l expresion en posfija: ").split(" ")

#Lectura de la cantidad de lineas que tiene el archivo
archivo  = open("expresiones.in.txt","r")
n = len(archivo.readlines())
print(n)

for i in archivo:
    print i,
"""for i in range(1,n):
    x = archivo.readline(n)
    linea = []
    print (linea)
    pila = Pila()
    
    for i in linea:
        convertir(linea[i], pila)

print evaluar(pila.desapilar())"""
