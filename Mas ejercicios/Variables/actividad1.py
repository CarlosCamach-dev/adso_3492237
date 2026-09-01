nombre = input("Ingrese el nombre del empleado: ")
cantHoras = int(input("Ingrese las horas teabajadas del empleado: "))
valHoras = int(input("Ingrese el valor de las horas: "))

salario = cantHoras * valHoras

print('-'*50)
print("Nombre del empleado:", nombre)
print(" ")
print("Horas trabajadas del empleado:", cantHoras)
print(" ")
print(f"Valor por hora: ${valHoras}")
print(" ")
print(f"Salario total: ${salario}")
print('-'*50)
