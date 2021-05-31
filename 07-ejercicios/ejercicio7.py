num1 = int(input("Escribe el primer numero:"))
num2 = int(input("Escribe el segundo numero:"))

for x in range(num1,(num2+1)):
    if x % 2 == 0:
        print(f"{x} es numero par")
    else:
        print(f"{x} no es par")