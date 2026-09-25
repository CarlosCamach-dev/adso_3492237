listaNumero = []
cant = int(input("Ingrese la cantidad de números: "))
for i in range(cant):
    listaNumero.append(int(input("Ingrese el número: ")))
listaNumero.sort()
print(listaNumero)
print("El segundo numero mayor es:", listaNumero[-2])