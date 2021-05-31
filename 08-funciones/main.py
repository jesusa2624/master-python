"""
Una FUNCION es un conjunto de instrucciones agrupadas bajo un nombre completo que puede reutilizarse invocando a la funcion tantas veces como sea necesario

def nombreDeMiFuncion(parametros):
    # instrucciones
nombreDeMiFuncion (mi_parametro)
nombreDeMiFuncion (otro_parametro)

"""

# Ejemplo 1
print ("############ EJEMPLO N° 1##################")

def nombrePersona():
    print("Jesus")
    print("Juan")
    print("Miguel")
    print("Carlos")
    print("Luis")
    print("\n")

# Invocar Funcion
nombrePersona()
nombrePersona()
nombrePersona()

# Ejemplo 2: PARAMETROS
# print ("############ EJEMPLO N° 2##################")


# def mostrarTuNombre(nombre, edad):
#     print(f"Tu nombre es: {nombre} y tu edad {edad} ")

#     if edad >= 18:
#         print("Es mayor de edad")

# pepito = input("Introduce tu nombre:")
# juancito = int(input("Introduce tu edad:"))
# mostrarTuNombre(pepito,juancito)

# Ejemplo 3: PARAMETROS
print ("############ EJEMPLO N° 3##################")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(0,11):
        operacion = numero * contador
        print(f"{numero}x{contador}={operacion}")

    print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1: PARAMETROS
print ("############ EJEMPLO N° 3.1##################")

for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4
print ("############ EJEMPLO N° 4 ##################")

# Parametros opcionales

def getEmpleado(nombre, dni = None):
    print("empleado")
    print(f"Nombre: {nombre}")
    

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Jesus Anglas", 73266230)

# Ejemplo 5: return
print ("############ EJEMPLO N° 5 ##################")

def saludame(nombre):
    saludo = f"Hola saludos, {nombre}"

    return saludo

print(saludame("Jesus Anglas"))

# Ejemplo 6: return
print ("\n############ EJEMPLO N° 6 ##################")

def calculador(num1, num2, basicas = False):

    suma = num1+num2
    resta = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(div)

    return cadena

print(calculador(56,5))

# Ejemplo 7: return
print ("\n############ EJEMPLO N° 7 ##################")

def getNombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"El apellido es {apellidos}"
    return texto

def devuelveTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Jesus","Anglas"))

# Ejemplo 8: return
print ("\n############ EJEMPLO N° 8 ##################")

dime_el_year = lambda year: f"el año es {year * 50}"

print(dime_el_year(2034))




    

