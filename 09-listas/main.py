"""
Las listas(arrays)
son colecciones de datos, bajo un unico nombre de
Para accedeer a estos valores utilizamos un indice numerico

"""
# definir una lista
nombres = ["jesus","miguel", "Pedrito"]
cantantes = list(("2pac","drake","JL"))
years = list(range(2020,2050))
variadas = ["Victor",3,"1.5",True]

# print(nombre)
# print(cantantes)
# print(years)
# print(variadas)

# modificar
nombres[1] = "Jose"
nombres[0] = "Juan"
print (nombres)

# Indices
print(nombres[0])
print(nombres[-2])
print(cantantes[1:3])
print(nombres[0:])

# Añadir elementos a una lista
cantantes.append("Kase O")
cantantes.append("Mana")
print(cantantes)



# nuevo_nombre = ""
# while nuevo_nombre != "parar":
#     nuevo_nombre = input("introduce la nueva nombre: ")
    
#     if nuevo_nombre != "parar" :
#         nombres.append(nuevo_nombre)


# # Recorrer lista
# print("\n************LISTADO DE PELICULAS*****************")

# for nombre in nombres:
#     print(f"{nombres.index(nombre)+1}.{nombre}")

# Recorrer lista
print("\n************LISTADO DE CONTACTOS*****************")
contactos = [
    [
        'Jesus',
        'jesus@gmail.com'
    ],
    [
        'Luis',
        'luis@gmail.com'
    ],
    [
        'Miguel',
        'Miguel@gmail.com'
    ]
]

# print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento}")
        else:
            print(f"Email: {elemento}")
    print ("\n")


