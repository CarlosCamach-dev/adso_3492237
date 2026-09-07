registro = {}
suma = 0
promedio = 0
cant = int(input("Ingrese la cantidad de empleados: "))
for i in range(cant):
    identificacion = input("Ingrese el numero de identificacion del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    registro[identificacion] = salario

for identificacion, salario in registro.items():
    suma += salario

promedio = suma / cant

print(f"Promedio de salarios: ${promedio:.2f}")