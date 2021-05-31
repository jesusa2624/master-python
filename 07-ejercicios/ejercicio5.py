
num1 = int(input("Introduce el primer numero:"))
num2 = int(input("Introduce el segundo numero:"))

while num1 <= num2:
    print (num1)

    if num1 > num2:
        print (num2)
        break
    num1 += 1