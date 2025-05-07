# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


multiplos_de_4 = []
for i in range(1, 101):
    if i % 4 == 0:
        multiplos_de_4.append(i)
print(multiplos_de_4)


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista2 = [1, "ser", True, None, 2.5]
print(f"El penultimo objeto de la lista es {lista2[-2]}")


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

lista3 = []
for i in range(3):
    palabra = input("ingresa una palabra ")
    lista3.append(palabra)
print(f"lista3 =  {lista3}")


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar
# cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "Loro"
animales[-1] = "oso"
print(animales)


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# La funcion max(numeros) busca el maximo valor en la lista numeros
# El metodo lista.remove(x) saca el elemento x de la lista
# entonces numeros.remove(max(numeros)) saca de la lista numeros el maximo valor entre sus elementos
# La lista impresa quedaria [8, 15, 3, 7]

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista6 = list(range(10, 31, 5))
print(lista6)
print(lista6[0:2])


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Chrysler"
autos[2] = "Chevron"
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.

dobles = []
lista8 = list(range(5, 16, 5))
print(lista8)
for i in lista8:
    dobles.append(i*2)
print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras =  [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#item a)
compras[2].append("jugo")

#item b)
compras[1][1] = "tallarines"

#item c)
compras[0].remove("pan")

print(compras)


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla. 

lista_anidada = [15, True, [25.5, 57.9, 30.6,], False]
print(lista_anidada)
