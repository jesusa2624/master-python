"""
# condicional IF

SI se_cumple_esta_condicion
    Ejecutar grupo de instrucciones

SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instruccion
else:
    otras instrucciones

# Operadores de comparacion

== igual
!= diferente
< menor que
> mayor que
<=menor igual que
>= mayor igual que

# Operadores logicos 

and Y
or O
! negacion
not no

"""

# Ejemplo n°1

print ("\n*************EJEMPLO 1****************")

color = "rojo"
# color = input("adivina cual es mi color favorito:")

if color == "rojo":
    print("en HORABUENA")
    print("El color es rojo")
else:
    print("color incorrecto")


# Ejemplo n°2

print ("\n*************EJEMPLO 2****************")

year = 2020
# year = int(input("en que año estamos:"))

if year < 2021:
    print("Estamos antes de 2021 ")

else:
    print("es un año despues a 2021")

# Ejemplo n°3

print ("\n*************EJEMPLO 3****************")

nombre = "Jesus Anglas"
ciudad = "Lima"
continente = "America"
edad = 55

# edad = int(input("ingrese su edad:"))

if edad >= 18:
    print("usted es mayor de edad")
    if continente != "America":
        print("el usuario no es americano")
    else:
        print(f"usted vive en el continente de {continente} en la ciudad de {ciudad} ")
else:
    print("usted es menor de edad ")


# Ejemplo n°4
print ("\n*************EJEMPLO 4****************")

# dia = int(input("introduce el numero del dia de la semana: "))
dia = 2

if dia == 1:
    print ("Es lunes")
elif dia == 2:
    print ("Es martes")
elif dia == 3:
    print ("Es miercoles")
elif dia == 4:
    print ("Es jueves")
elif dia == 5:
    print ("Es viernes")
else:
    print ("Es fin de semana")


# Ejemplo n°5
print ("\n*************EJEMPLO 5****************")

edad_minima = 18
eda_maxima = 65

edad_oficial = 17
# edad_oficial = int(input("Introduce tu edad:"))

if  edad_oficial >= edad_minima and edad_oficial <= eda_maxima :
    print ("esta en edad de trabajar")
else:
    print ("no esta en edad para trabajar")


# Ejemplo n°6
print ("\n*************EJEMPLO 6****************")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Peru":
    print(f"{pais} ES un pais que habla castellano")
else:
    print(f"{pais} no es un pais que habla castellano ")


# Ejemplo n°7
print ("\n*************EJEMPLO 7****************")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Peru"):
    print(f"{pais} no es un pais que habla castellano")
else:
    print(f"{pais} es un pais que habla castellano ")



# Ejemplo n°8
print ("\n*************EJEMPLO 8****************")

pais = "Peru"

if pais != "Mexico" and pais != "España" and pais != "Peru":
    print(f"{pais} no es un pais que habla castellano")
else:
    print(f"{pais} es un pais que habla castellano ")



# multiplo = int(input("ingrese su numero:"))
multiplo = 26

if multiplo % 3 == 0  :
    print ("Es multiplo de 3")
else:
    print("no es multiplo de 3")