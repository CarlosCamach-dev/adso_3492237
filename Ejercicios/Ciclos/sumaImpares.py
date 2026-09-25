num = int(input("ingrese su numero: "))
suma = 0
if num <= 0:
    print("Error: numero no es positivo")
for i in range(num + 1):
        if i % 2 != 0:
            suma += i

print("La suma de los numeros impares es:", suma)