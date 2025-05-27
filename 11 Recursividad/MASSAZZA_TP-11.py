#Práctico 11: Aplicación de la Recursividad

# 1) Crea una función recursiva que calcule el factorial de un número.
#  Luego, utiliza esa función para calcular y mostrar en pantalla el
#  factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorialDeCadaNumero(num):    
    if num == 1 or num == 0:
        print(1)
    else:
        print(factorial(num) )
        factorialDeCadaNumero(num -1)

def factorial(n):
    if n == 0:
       return 1
    else:
       return n * factorial(n-1)

print("Se calcularan todos los factoriales desde el numero que se ingrese hasta el 1")
numero = int(input("Ingrese un numero "))

# Se llama a la funcion recursiva con el valor del numero que en cada ciclo
#  llama a la funcion factorial
factorialDeCadaNumero(numero) 


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta la 
# posición que el usuario especifique.

def fibonacci(posicion):
    if posicion == 0 or posicion == 1:
        return posicion
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion -2)

numero = int(input("Ingrese un numero: "))

for i in range(numero + 1):    
    print(f"f({i}) es: {fibonacci(i)}")



# 3) Crea una función recursiva que calcule la potencia de un número base
# elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba 
# esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)
    
base = int(input("Ingrese base: "))
exponente = int(input("Ingrese exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


# 4) Crear una función recursiva en Python que reciba un número entero
#  positivo en base decimal y devuelva su representación en binario
#  como una cadena de texto.

def decimalABinario(num):
    if num == 0:
        return ""
    else:
       return decimalABinario(num//2) + str(num % 2)
        
numero = int(input("Ingrese el numero que desea pasar a binario ")) 

print(f" El numero {numero} en binario es {decimalABinario(numero)}")


# 5) Implementá una función recursiva llamada es_palindromo(palabra)
#  que reciba una cadena de texto sin espacios ni tildes, y devuelva
#  True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().


def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:-1])
        


print("Dada una palabra se verifica si es palindromo")
palabra = input("Ingrese la palabra ").upper()
lista = list(palabra)
print( palindromo(lista))


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que
#  reciba un número entero positivo y devuelva la suma de todos sus dígitos.

# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n//10 == 0:
        return n % 10

    else:
        return suma_digitos(n//10) + n % 10

num = int(input("Ingrese el numero para sumar sus digitos "))
print(f"La suma de los digitos del numero {num} es: {suma_digitos(num)}")



# 7) Un niño está construyendo una pirámide con bloques.
#  En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1),
#  y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques
# en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return contar_bloques(n - 1) + n
    
base = int(input("Ingrese la cantidad de bloques que tiene la base "))
print(f"\n Cantidad de bloques necesarios para una piramide de base = {base} es: {contar_bloques(base)}\n")


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba
#  un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas
#  veces aparece ese dígito dentro del número.

# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4

def contar_digito(numero, digito):
    if numero//10 == 0:
        if numero % 10 == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return contar_digito(numero//10, digito) + 1
        else:
            return contar_digito(numero//10, digito)

num = int(input("Ingrese numero al que desea contar los digitos "))
digito = int(input("Ingrese el digito que quiere contar "))
print(f"El digito {digito} se repite en {num}, {contar_digito(num, digito)} veces")