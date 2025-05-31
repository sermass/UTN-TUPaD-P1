# Programa que le pide al usuario que ingrese primero la raiz del arbol
#  y luego los hijos que desee. Para terminar de ingresar hijos pide que se ingrese un 0
# Una vez corrido el programa muestra la forma del arbol a 90º y los recorridos:
# preorden,inorden y posorden



# Cada nodo se representa como: [valor, hijo_izquierdo, hijo_derecho]

def crear_arbol(valor):
    return [valor, [], []]

# La funcion insertar selecciona de que lado del arbol coloca el
# nuevo valor segun sea mayor o menor que el nodo en que esta parado.
# Toma dos parametros: nodo que es el sub-arbol, y nuevo_valor que es 
# el hijo ingresado

def insertar(nodo, nuevo_valor):
    if nuevo_valor < nodo[0]:
        insertar_izquierda(nodo, nuevo_valor)
    else:
        insertar_derecha(nodo, nuevo_valor)


# La funcion insertar_izquierda toma los mismos parametros que insertar
# y se fija si hay un valor en el nodo siguiente. Si no hay, crea el nuevo nodo.
# Si ya hay un valor vuelve a consultar (por recursividad con la funcion insertar)
# como es el nuevo_valor con el actual nodo. Esto lo repite hasta encontrar un 
# nodo vacio para insertar

def insertar_izquierda(nodo, nuevo_valor):
    subarbol_izq = nodo[1]
    if subarbol_izq:
        insertar(subarbol_izq, nuevo_valor)
    else:
        nodo[1] = [nuevo_valor, [], []]



# La funcion insertar_derecha es similar a la izquierda

def insertar_derecha(nodo, nuevo_valor):
    subarbol_der = nodo[2]
    if subarbol_der:
        insertar(subarbol_der, nuevo_valor)
    else:
        nodo[2] = [nuevo_valor, [], []]


# Las funciones recorrido son recursivas y cambian entre
#  una y otra en la posicion en que se encuetra la ejecucion del print

def preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        preorden(arbol[1])
        preorden(arbol[2])

def inorden(arbol):
    if arbol:
        inorden(arbol[1])
        print(arbol[0], end=' ')
        inorden(arbol[2])

def postorden(arbol):
    if arbol:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0], end=' ')

def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)
        print('   ' * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)


#---------------------------------------------------
# probar ingresando en este orden:
# 6 4 5 8 3 9 7
# para tener un arbol con todas las ramas

raiz = int(input(" Ingrese el valor raiz "))
arbol = crear_arbol(raiz)

print ("Ahora inserte tantos hijos como quiera. Para terminar tecla '0'")
hijo = int(input("Ingrese un hijo "))
insertar(arbol, hijo)
while hijo != 0:
    hijo = int(input("Ingrese un hijo "))
    if hijo != 0:
        insertar(arbol, hijo)

print("Árbol visualizado (rotado 90°):")
imprimir_arbol(arbol)

# Recorridos
print("\nRecorrido Preorden:")
preorden(arbol)

print("\nRecorrido Inorden:")
inorden(arbol)

print("\nRecorrido Postorden:")
postorden(arbol)
