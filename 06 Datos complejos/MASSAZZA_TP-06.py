# #1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# # Añadir las siguientes frutas con sus respectivos precios:
# # ● Naranja = 1200
# # ● Manzana = 1500
# # ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir las nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# #  actualizar los precios de las siguientes frutas:
# # ● Banana = 1330
# # ● Manzana = 1700
# # ● Melón = 2800

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario actualizado
print(precios_frutas)

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# #  crear una lista que contenga únicamente las frutas sin los precios.


# Obtener solo los nombres de las frutas (claves del diccionario)
frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
#  Ejemplo: {juan:1234, ana:5678}  consultar juan --> muestra 1234


agenda = {}

# Cargar 5 contactos
print("Carga de 5 contactos:")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = telefono  # Guardar en el diccionario

# Consultar un contacto
consulta = input("Ingrese el nombre a buscar (o '0' para terminar): ")

while consulta != '0':
    if consulta in agenda:
        print(f"El teléfono de {consulta} es: {agenda[consulta]}")
    else:
        print(f"{consulta} no está en la agenda.")

    consulta = input("\nIngrese otro nombre a buscar (o '0' para terminar): ")


#5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# ejemplo : entrada "hola mundo hola"
#           salida palabras unicas:{'hola', 'mundo'}
#            recuento: {'hola':2, 'mundo':1}
#

# Solicita frase al usuario
frase = input("Ingresa una frase: ")

# Dividir la frase en palabras (separadas por espacios)
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("\nPalabras únicas:", palabras_unicas)

# Diccionario con cantidad de veces de cada palabra
cantidad_de_veces = {}
for palabra in palabras:
    if palabra in cantidad_de_veces:
        cantidad_de_veces[palabra] += 1
    else:
        cantidad_de_veces[palabra] = 1

print(f"\n frecuencia: {cantidad_de_veces}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.
#   ejemplo: alumnos = {sofia:(7,8,9), luis:(6,7,7)}

# Diccionario para almacenar alumnos y sus notas
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = notas

# Calcular y mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}") 


#7) Dado dos sets de nombres, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Conjuntos de estudiantes aprobados
parcial1 = {"Juan", "María", "Carlos", "Ana", "Sergio"}
parcial2 = {"Ana", "Pedro", "Carlos", "Sofía", "Sergio"}

# Estudiantes que aprobaron ambos parciales (intersección)
aprobados_ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", aprobados_ambos)

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
aprobados_solo_uno = parcial1 ^ parcial2
print("\nAprobaron solo uno de los dos:", aprobados_solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial (unión)
aprobados_al_menos_uno = parcial1 | parcial2
print("\nAprobaron al menos un parcial:", aprobados_al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario inicial de productos y stock
stock_productos = {
    'Manzanas': 50,
    'Bananas': 30,
    'Naranjas': 40,
    'Leche': 20
}


while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar stock")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")

        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario.")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        
        if producto in stock_productos:        
            unidades = int(input(f"Ingrese las unidades a agregar a {producto}: "))
            stock_productos[producto] += unidades
            print(f"Stock actualizado: {producto} ahora tiene {stock_productos[producto]} unidades")
        else:
            print(f" El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
    
    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:        
            unidades = int(input(f"Ingrese el stock inicial de {producto}: "))
            stock_productos[producto] = unidades
            print(f"Producto '{producto}' agregado con {unidades} unidades")            
        else:
            print(f"El producto '{producto}' ya existe. Use la opción 2 para agregar unidades.")
    
    elif opcion == '4':
        print("Hasta luego")
        break
    
    else:
        print(" Opción no válida. Intente nuevamente.")

# Mostrar stock final (opcional)
print("\n--- Stock Final ---")
for producto, unidades in stock_productos.items():
    print(f"{producto}: {unidades} unidades")


#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#  Ejemplo: agenda = {('lunes', '10:00'): 'reunion',
#                     ('martes', '15:00'): 'clase de ingles'
#                   }

#Permití consultar qué actividad hay en cierto día y hora

agenda = {}

def agregar_evento():
    dia = input("Ingrese el día (ej: lunes): ")
    hora = input("Ingrese la hora (ej: 15:30): ")
    evento = input("Ingrese el evento: ")
    clave = (dia, hora)
    
    agenda[clave] = evento


def consultar_evento():
    dia = input("Ingrese el día a consultar: ")
    hora = input("Ingrese la hora a consultar: ")
    clave = (dia, hora)
    
    if clave in agenda:
        print(f"Evento: {agenda[clave]}")
    else:
        print("No hay eventos programados para esa fecha y hora.")

def mostrar_agenda():
    if not agenda:
        print("La agenda está vacía.")
        return
    
    print("\n--- Agenda Completa ---")
    for (dia, hora), evento in sorted(agenda.items()):
        print(f"{dia.capitalize()} {hora}: {evento}")

# Programa principal


while True: 
        
    print("\n--- Agenda de Eventos ---")
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Mostrar agenda completa")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        agregar_evento()
    elif opcion == '2':
        consultar_evento()
    elif opcion == '3':
        mostrar_agenda()
    elif opcion == '4':
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
#  Ejemplo: original:{argentina: bsas, uruguay:montevideo}
#           invertido:{bsab:argentina, montevideo:uruguay}
#
# # Diccionario original (país: capital)
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'España': 'Madrid',
    'Francia': 'París'
}

# Invertir el diccionario (capital: país)
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("Diccionario original (País → Capital):", paises_capitales)
print("\nDiccionario invertido (Capital → País):", capitales_paises)