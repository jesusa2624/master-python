"""
Existe las variables locales y globales

"""
frase = "ni los genios son tan genios,ni los idiotas son tan idiotas"

print(frase)

def holaMundo ():
    frase = "Hola Mundo"
    print("dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "vjesus@gob.pnp"
    print("dentro : website")

    return "dato devuelto: " + str(year)

print(holaMundo())
print(website)