cantantes = ["2pac", "Drake","Julio Iglesias","mana"]
numeros = [1,2,5,8,3,4]

# Ordenar
print(numeros)

numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("SOAD") 
cantantes.insert(1 , "Los prisionero")

# print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("mana")
# print(cantantes)

# Dar la vuelta
numeros.reverse()
# print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# Contar el numero de elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("SOAD"))

# Unir listas
cantantes.extend(numeros)
print(cantantes)