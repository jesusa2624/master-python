# num1 = int(input("ingrese su numero 1:"))
# num2 = int(input("ingrese su numero 2:"))

# print (f""" {num1}x{num2} = {num1 * num2} 
# {num1}+{num2} = {num1 + num2} 
# {num1}-{num2} = {num1 - num2} 
# {num1}/{num2} = {num1 / num2} """)

#EJERCICIOS CHENCHO

# num1 = int(input("ingrese su numero 1:"))
# num2 = int(input("ingrese su numero 2:"))
# operacion = input("ingrese su operacion:")

# if operacion == "+":
#     print (f" {num1}+{num2} = {num1 + num2}")
# elif operacion == "-":
#     print (f" {num1}-{num2} = {num1 - num2}")
# elif operacion == "x":
#     print (f" {num1}x{num2} = {num1 * num2}")
# elif operacion == "/":
#     print (f" {num1}/{num2} = {num1 / num2}")
# else:
#     print ("No reconoce esta operacion")



# while True:
#     edad = int(input("INGRESE SU EDAD: "))
#     if edad >= 18:
#         print ("tu pase a la felicidad")
#     else:
#         print ("no ingresas pulpin")
#     if edad == 23:
#         print ("no ingresas pedofilo")
#         break


# while True:
#     numero = int(input("INGRESE SU NUMERO: ")) 
#     if numero == 0:
#         print ("se acabo")
#         break

num1 = int(input("INGRESE SU NUMERO 1: "))
while True:
    num2 = int(input(f"INGRESE SU NUMERO MAYOR QUE {num1} : "))

    if num1 < num2:
        print (f" {num2} es mayor que {num1}")
        break

if num1 > num2:
        print (f"{num1} no es mayor que {num2}")
    

        