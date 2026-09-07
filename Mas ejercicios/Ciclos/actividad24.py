num = int(input("ingrese su numero: "))
fact = 1
if num <= 0:
    print("Error: numero no es positivo")
for i in range(num):
    fact *= (i + 1)

print(fact)
    