cant = int(input("Ingrese la cantidad de terminos: "))
num1 = 0
num2 = 1
fibonacci = 0
for i in range(cant):
    print(fibonacci)
    fibonacci = num1 + num2
    num2 = num1
    num1 = fibonacci
