#Alumno: MassazzaSergio
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla
#  un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”,
#  el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será
#  más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Hola, ingresa tu nombre: ")
print(f"Hola {nombre}!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y
#  lugar de residencia e imprima por pantalla una oración con los datos ingresados.
#  Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,
#  el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”.
#  Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.

print("Por favor, ingrese sus datos: ")
nombre = input("nombre: ")
apellido = input("apellido: ")
edad = input("edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4) Crear un programa que pida al usuario el radio de un círculo
#  e imprima por pantalla su área y su perímetro.

radio = int(input("Por favor, ingrese el radio del circulo en cm: "))
pi = 3.1416
perimetro = 2*pi*radio
area = pi*radio**2
print(f"El circulo tiene un perimetro de {perimetro}cm y un area de {area:.2f}cm cuadrados")


#5) Crear un programa que pida al usuario una cantidad de segundos
#  e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese los segundos: "))
horas = segundos/(60*60)
print(f"{segundos} segundos equivalen a {horas:.2f} horas")


# 6) Crear un programa que pida al usuario un número 
# e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))
print(f"""\n{numero} x 1 = {numero}
{numero} x 2 = {numero*2}
{numero} x 3 = {numero*3}
{numero} x 4 = {numero*4}
{numero} x 5 = {numero*5}
{numero} x 6 = {numero*6}
{numero} x 7 = {numero*7}
{numero} x 8 = {numero*8}
{numero} x 9 = {numero*9}
{numero} x 10 = {numero*10} """)


# 7) Crear un programa que pida al usuario dos números
#  enteros distintos del 0 y muestre por pantalla el resultado
#  de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(f"""\nLa suma de los dos numeros es: {num1 + num2}
\nEl resultado de restar el primer numero menos el segundo es: {num1 - num2}
\nLa multplicacion de ambos numeros es: {num1 * num2}
\nEl resultado de dividir el primer numero por el segundo es: {num1 / num2}""")


#8) Crear un programa que pida al usuario su altura y su peso e imprima 
# por pantalla su índice de masa corporal. Tener en cuenta que 
# el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2

altura = float(input("Ingrese su altura en Mts: "))
peso = float(input("Ingrese su peso en Kgs: "))
imc = f"{(peso/(altura**2)):.2f}"  #  imc guarda el calculo del IMC redondeado a 2 decimales con ':.2f'
print(f"Su IMC es de: {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima 
# por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Ingrese la temperatura en celsius: "))
farenheit = f"{(9/5 * celsius + 32):.2f}" 
print(f"La temperatura en farenheit es: {farenheit}")


# 10) Crear un programa que pida al usuario 3 números e 
# imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese primer el numero: "))
num2 = float(input("Ingrese segundo el numero: "))
num3 = float(input("Ingrese tercer el numero: "))
print(f"El promedio de los 3 numeros es: {(num1 + num2 + num3)/3} ")
