"""
# WHILE

WHILE condicion:
    BLOQUE DE INSTRUCCIONES
    //actualizacion de contador 

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador += 1

print("----------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + "," + str(contador)
    contador = contador + 1

print (muestrame)

# Ejemplo

usuario = int(input("introduce el numero que quieras la tabla: "))

if usuario < 1:
    usuario = 1
print (f"\n########TABLA DEL NUMERO {usuario}#############")

contador = 1

while contador <= 10:
    print (f"{usuario} x {contador} = {usuario}*{contador}")
    contador = contador + 1
else:
    print("TABLA TERMINADA")


