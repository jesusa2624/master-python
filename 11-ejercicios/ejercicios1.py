# Crear lista
numeros = [18,2,39,45,5,61,7,82]

# Crear funcion que recorra lista y devuelca string

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado 

# Recorrer lista
print(f"\n*********RECORRER LISTAS********************")

# for numero in numeros:
#     print (numero)



# if usu == range(0,9):
#     print (usu)


# Ordenar y mostrar
print("*************ORDENAR Y MOSTRAR****************")
numeros.sort()
print(mostrarLista(numeros))

# Ordenarsu longitud
print("*************MOSTRAR sus lONGITUD****************")
print(len(numeros))

# Ordenar su BUSQUEDA
print("*************BUSQUEDA****************")
usu = int(input("Introducir el numero deseado:"))
print (usu)
