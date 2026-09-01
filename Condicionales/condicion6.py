num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
acum = 0
if num1 > num2:
    acum = num1
else:
    acum = num2
if acum < num3:
    acum = num3

print("El numero mayor de los tres numeros es:", acum)
