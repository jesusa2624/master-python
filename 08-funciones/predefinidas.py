nombre = "JEsus Anglas"

# Funciones generales
print(type(nombre))

# Detectar el tipado

comprobar = isinstance(nombre,int)

if comprobar:
    print("Esa variable es un string")
else:
    print("no es una cadena")

if not isinstance(nombre,float):
    print("no es flotante")


# Limpiar espacios
frase = "     mi contenido   "

print(frase.strip())


# Eliminar variables

year = 2021
print(year)

del year
# print(year)

# Comprobar variables vacias

texto = " FF "

if len(texto) <= 0:
    print("la variable esta vacia")
else:
    print("La variable tiene contenido:", len(texto))

# encontrar caracteres

frase = "la vida es bella"

print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y minuscula

print(nombre)
print(nombre.lower())
print(nombre.upper())

