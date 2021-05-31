"""
# FOR

for variable in elemento_iterable (lista,rango,etc)
    BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado= 0
for contador in range(0,10):
    print ("voy por el " + str(contador))

    resultado = resultado + contador


# Ejemplo con tablas de multiplicar
print ("\n**********EJEMPLO 1***************")

multiplicar = int(input("ingrese su numero de tu tabla:"))

if multiplicar < 1 :
    multiplicar = 1

print(f"\n####Tabla de multiplicar del numero {multiplicar} ###")

for numero_tabla in range(0,13):
    print(f"{multiplicar} x {numero_tabla} = {multiplicar*numero_tabla}")
else:
    print ("Tabla finalizada")
