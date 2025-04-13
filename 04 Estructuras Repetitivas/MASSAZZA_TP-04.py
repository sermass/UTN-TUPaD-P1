# 1) Crea un programa que imprima en pantalla
#  todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, 
# mostrando un número por línea.

for x  in range(100 + 1):
    print(x)



# 2) Desarrolla un programa que solicite al usuario un número
#  entero y determine la cantidad de dígitos que contiene.


print("Ingrese un numero entero de una o varias cifras")
numero = int(input())

#digito es la variable que cuenta los digitos
digito = 1

#'Ultimo' es la variable centinela que se hace verdadera cuando 
# es el ultimo digito
ultimo = False

while not ultimo:
    # a numero lo divido por 10 par desplazarme por los digitos
    # tomo sucesivamente la parte entera de esa division hasta que sea 0
    numero = int(numero/10)

    if numero != 0:
        digito += 1
    else:
        ultimo = True
print(f"El numero ingresad tiene {digito} digitos" )


# 3) Escribe un programa que sume todos los números enteros comprendidos
#   entre dos valores dados por el usuario, excluyendo esos dos valores.

print("Ingrese el rango de valores que desea sumar")
print("desde ")

cota_inf = int(input()) 
print("Hasta ")
cota_sup = int(input())
#Inicializo la variable suma
suma = 0

for x in range(cota_inf + 1,cota_sup):
     suma += x
print(f"La suma de los numeros comprendidos entre {cota_inf} y {cota_sup} es {suma}")   


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("Ingrese los numeros que desea sumar. Para finalizar, ingrese 0")
numero = int(input())
suma = 0
while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese otro numero "))
print(f"La suma de los numeros ingresados es: {suma}")



# 5) Crea un juego en el que el usuario deba adivinar un número 
# aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos 
# intentos fueron necesarios para acertar el número.

import random 
num_secreto = random.randrange(0, 9) 
contador = 1

num_tentativo = int(input("Elija un numero del 0 al 9 "))
while num_tentativo != num_secreto:
    num_tentativo =  int(input("Uff le pifiò, elija otro numero del 0 al 9 "))
    contador += 1
print(f"Bravo!! acertó el numero en {contador} intentos!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares
#  comprendidos entre 0 y 100, en orden decreciente.

#Como es decreciente va de mayor a menor
desde = 100
hasta = 0
for x in range(desde ,hasta -2, -2):
    print(x)


# 7) Crea un programa que calcule la suma de todos los números comprendidos
#  entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero entero. Se sumaran todos los numeros del 0 hasta ese numero inclusive "))
suma = 0
for x in range(0, numero + 1):
    suma += x
print(f"La suma es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros.
#  Luego, el programa debe indicar cuántos de estos números son pares,
#  cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar
# preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 5
cont_imp = 0
cont_par = 0
cont_neg = 0
cont_pos = 0

print(f"Ingrese los {cantidad_numeros} numeros")
for x in range(cantidad_numeros):
    num = int(input(f" numero {x +1}: "))
    if num > 0:
        cont_pos += 1
    elif num < 0:
        cont_neg += 1
    if num != 0 and num % 2 == 0:
        cont_par += 1
    elif num != 0:
        cont_imp += 1
print(f"""         La cantidad de numeros negativos es: {cont_neg}\n
        La cantidad de numeros positivos es: {cont_pos}\n
        La cantidad de numeros pares es: {cont_par}\n
        La cantidad de numeros impar es: {cont_imp}\n""")


# 9) Elabora un programa que permita al usuario ingresar 
# 100 números enteros y luego calcule la media de esos valores.
#  (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 5
suma = 0
print(f"Ingrese los {cantidad_numeros} numeros enteros")
for x in range(cantidad_numeros):
    num = int(input(f" numero {x +1}: "))
    suma += num
print(f"La media de los numeros ingresados es: {suma/cantidad_numeros}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


numero = int(input("ingrese un numero "))

#separo el digito menos significativo del numero tomando la division entera por 10
digito = int(numero / 10)

# En la variable 'oremun' guardo el digito menos significativo extraido con el resto en base 10
oremun = numero % 10

while digito != 0:
    #Ahora la variable 'digito' tiene un digito menos vuelvo a calcular el resto de la division por 10 
    resto = digito % 10

    #finalmente en 'oremun' desplazo el digito que tenia y le sumo el nuevo
    oremun = oremun * 10 + resto
    digito = int(digito / 10)
    
    

print(f"el numero {numero} al reves es {oremun} ")
