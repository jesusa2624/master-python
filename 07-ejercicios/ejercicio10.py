alumnos = 3
contador = 0
aprobados = 0
jalados = 0

while contador <= alumnos:
    nota = int(input (f"Que nota quieres ponerle al alumno {contador} :"))
    
    if nota >= 13 and nota <=20 :
        print (f" el alumno {contador} esta aprobado")
        aprobados += 1
    elif nota < 13:
        print (f" el alumno {contador} esta desaprobado ")
        jalados += 1
    

    contador +=1


print (f"aprobados = {aprobados}")
print (f"desaprobados = {jalados}")

