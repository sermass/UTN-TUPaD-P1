
#  1) Escribir un programa que solicite la edad del usuario.
#  Si el usuario es mayor de 18 años, deberá mostrar un mensaje
# en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad "))
if edad > 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario.
#  Si la nota es mayor o igual a 6, deberá mostrar
#  por pantalla un mensaje que diga “Aprobado”;
#  en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares.
#  Si el usuario ingresa un número par, imprimir por en pantalla
#  el mensaje "Ha ingresado un número par"; en caso contrario,
#  imprimir por pantalla "Por favor, ingrese un número par".
#  Nota: investigar el uso del operador de módulo (%) en Python
#  para evaluar si un número es par o impar.

par = int(input("Ingrese un numero par "))
if par%2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")


# 4) Escribir un programa que solicite al usuario su edad e imprima
#  por pantalla a cuál de las siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años.
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad "))
if edad < 12:
    print("Niño/a")
elif edad >=12 and edad < 18:
    print("Adolecente")
elif edad >=18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a mayor")


#5) Escribir un programa que permita introducir contraseñas
#  de entre 8 y 14 caracteres (incluyendo 8 y 14).
#  Si el usuario ingresa una contraseña de longitud adecuada,
#  imprimir por en pantalla el mensaje "Ha ingresado una
#  contraseña correcta"; en caso contrario, imprimir por pantalla
#  "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#  Nota: investigue el uso de la función len() en Python para
#  evaluar la cantidad de elementos que tiene un iterable tal
#  como una lista o un string.

contraseña = input("Ingrese una contraseña (debe tener entre 8 y 14 caracteres)")
longitud = len(contraseña)
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6)La moda (mode -valor mas comun-), la mediana (median -valor central-)
#  y la media (mean -promedio-) son parámetros   estadísticos 
#  que se pueden utilizar para predecir la forma de una
#  distribución normal a partir del siguiente criterio:
#  ● Sesgo positivo o a la derecha: cuando la media es mayor
#    que la mediana y, a su vez, la mediana es mayor que la moda.
#  ● Sesgo negativo o a la izquierda: cuando la media es menor
#    que la mediana y, a su vez, la mediana es menor que la moda.
#  ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que
#  tome la lista numeros_aleatorios, calcule su moda, su mediana y
#  su media y las compare para determinar si hay sesgo positivo,
#  negativo o no hay sesgo. Imprimir el resultado por pantalla.


#Importo del paquete stadistics las funciones: mode, median, mean
from statistics import mode, median, mean 

#importo el paquete random
import random

#creo una lista de 50 numeros aleatorios con numeros enteros del 1 al 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)

mediana = median(numeros_aleatorios)

media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
     print("Sesgo negativo")
elif media == mediana and mediana == moda:
     print("Sin sesgo")
else:
    print("media: ", media," mediana: ",media, "moda: " , moda, )


#7) Escribir un programa que solicite una frase o palabra al usuario.
#  Si el string ingresado termina con vocal, añadir un signo
#  de exclamación al final e imprimir el string resultante
#  por pantalla; en caso contrario, dejar el string tal cual
#  lo ingresó el usuario e imprimirlo por pantalla.


frase = input("Ingrese una frase o palabra ")

#Averiguo la longitud de la frase para saber cual es la ultima letra
longitud_frase = len(frase)

#Averiguo cual es la ultima letra y la pongo en minuscula
ultima_letra = frase[longitud_frase - 1].lower()

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(frase + "!")
else:
    print(frase)


#8) Escribir un programa que solicite al usuario que ingrese su
#  nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

#El programa debe transformar el nombre ingresado de acuerdo
#  a la opción seleccionada por el usuario e imprimir el resultado
#  por pantalla.

nombre = input("Ingrese su nombre ")
txt = """tipee:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula. """

opcion = int(input(txt))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La seleccion debe ser 1, 2 o 3")

# Otra opcion es utilizar match:
match opcion:
    case 1:
        print(nombre.upper())
    case 2:
        print(nombre.lower())
    case 3:
        print(nombre.title())
    case _:
        print("La seleccion debe ser 1, 2 o 3")


#9) Escribir un programa que pida al usuario la magnitud
#  de un terremoto, clasifique la magnitud en una de las siguientes
#  categorías según la escala de Richter e imprima el resultado 
# por pantalla:
#    ● Menor que 3: "Muy leve" (imperceptible).
#    ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#    ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#    ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#    ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#    ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input("Ingrese la magnitud del terremoto "))
if magnitud_terremoto < 3:
     print("'Muy leve' (imperceptible).")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
     print("'Leve' (ligeramente perceptible).")
elif magnitud_terremoto >= 4  and magnitud_terremoto < 5:
     print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
     print('"Fuerte" (puede causar daños en estructuras débiles).')
elif magnitud_terremoto >=6 and magnitud_terremoto < 7:
     print('"Muy Fuerte" (puede causar daños significativos).')
else:
     print('"Extremo" (puede causar graves daños a gran escala).')



#10) Utilizando la información aportada en la siguiente tabla sobre 
# las estaciones del año Periodo del año

# -----------------------------------------------------------------------    
# !                             ! Estación en el    ! Estación en el    !
# !                             ! hemisferio norte  ! hemisferio sur    !
# !_____________________________!___________________!___________________!
# ! Desde el 21 de diciembre    !                   !                   !
# ! hasta el 20 de marzo        !    Invierno       !       Verano      !
# ! (incluidos)                 !                   !                   !
# !_____________________________!___________________!___________________! 
# ! Desde el 21 de marzo        !                   !                   !
# ! hasta el 20 de junio        !    Primavera      !       Otoño       !
# ! (incluidos)                 !                   !                   !
# !_____________________________!___________________!___________________! 
# ! Desde el 21 de Junio        !                   !                   !
# ! hasta el 20 de Septiembre   !    Verano         !       Invierno    !
# ! (incluidos)                 !                   !                   !
# !_____________________________!___________________!___________________! 
# ! Desde el 21 de septiembre   !                   !                   !
# ! hasta el 20 de Diciembre    !    Otoño          !       Primavera   !
# ! (incluidos)                 !                   !                   !
# !_____________________________!___________________!___________________! 
# 
# Escribir un programa que pregunte al usuario en cuál hemisferio
#  se encuentra (N/S), qué mes del año es y qué día es.
#  El programa deberá utilizar esa información para imprimir por pantalla
#  si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("""Indique en que hemisferio se encuentra:
                   N: Norte
                   S: Sur """).lower()

mes = int(input("""Indique que mes del año es:
            Opciones: 
            1 = Enero
            2 = Febrero
            3 = Marzo
            4 = Abril
            5 = Mayo
            6 = Junio
            7 = Julio
            8 = Agosto
            9 = Septiembre
           10 = Octubre
           11 = Noviembre
           12 = Diciembre
            """))
dia = int(input(" Indique que dia es "))


if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == "n":
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == "n":
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == "n":
        print("Verano")
    else:
        print("Invierno")
if (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
    if hemisferio == "n":
        print("Otoño")
    else:
        print("Primavera")