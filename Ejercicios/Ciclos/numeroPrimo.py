num = int(input("ingrese su numero: "))
primo = 0
if num < 0:
    print("Error: numero no es positivo")
for i in range(num + 1):
    if num % (i + 1) == 0:
        primo += 1
if primo == 2:
    text = f"El numero {num} es primo"
else:
    text = f"El numero {num} no es primo"
print(text)