# Actividades:
# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# #Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# #Programa principal
imprimir_hola_mundo()

#--------------------------------------------------------------------

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# #Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!!")

# #Programa principal
name = input("Ingrese su nombre ")
saludar_usuario(name)

#--------------------------------------------------------------------

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

# #Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# #Programa principal
name = input("Ingrese su nombre ")
surname = input("Ingrese su apellido ")
age = input("Ingrese su edad ")
residence = input("Ingrese su lugar de residencia ")
informacion_personal(name, surname, age, residence)

#---------------------------------------------------------------------

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

import math
pi = math.pi

# #Definicion de funciones
def calcular_area(radio):
    area = pi*(radio**2)
    print(f"El area de la circunsferencia de radio {radio} es {area} cms cuadrados")

def calcular_perimetro(radio):
    perimetro = 2*pi*radio
    print(f"El perimetro del circunsferencia de radio {radio} es {perimetro} cms")

# #Programa principal
radius = float(input("Ingrese el radio de la circunsferencia en cm "))
calcular_area(radius)
calcular_perimetro(radius)

#---------------------------------------------------------------------

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

# #Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos/(60**2)
    print(f"{segundos} segundos son {horas} horas ")

# #Programa principal
seconds = int(input("Ingrese la cantidad de segundos "))
segundos_a_horas(seconds)

#---------------------------------------------------------------------

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# #Definicion de funciones
def tabla_multiplicar(numero):
    print(" -----------")
    for i in range(1,11):

        print(f"| {i} x {numero} = {i*numero} ")
    print(" -----------")

# #Programa principal
print("De que numero quiere realizar la tabla?")
num = int(input("Ingrese el numero "))
tabla_multiplicar(num)

#---------------------------------------------------------------------

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

# #Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multip = a*b
    if b != 0:
        div = a/b
    else:
        print("No se puede dividir por 0")
        div = None
    print(f"""La suma entre los numeros es: {suma}
La resta entre los numeros es: {resta}
La multiplicacion entre los numeros es {multip} 
La division entre ambos es {div}""")

# #Programa principal
print("Ingrese los dos numeros a calcular")
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))
operaciones_basicas(num1, num2)

#---------------------------------------------------------------------

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

# #Definicion de funciones
def calcular_imc(peso, altura):
    IMC = peso / (altura)**2
    print(f"El IMC calculado es: {IMC:.2f}")

# #Programa principal
weight = float(input("Ingrese su peso en kg "))
height = float(input("Ingrese su altura en mts "))
calcular_imc(weight, height)

#---------------------------------------------------------------------

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# #Definicion de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 +32
    print(f"{celsius} grados celcius son {fahrenheit} grados fahrenheit")

# #Programa principal
grados_celsius = float(input("Ingrese los grados celsius "))
celsius_a_fahrenheit(grados_celsius)

#---------------------------------------------------------------------

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# # Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    print(f"El promedio entre {a}, {b} y {c} es {promedio}")

# # Programa principal
print("Ingrese 3 numeros para calcular el promedio")
num1 = float(input("Ingrese el primer numero "))
num2 = float(input("Ingrese el segundo numero "))
num3 = float(input("Ingrese el tercer numero "))
calcular_promedio(num1, num2 ,num3)