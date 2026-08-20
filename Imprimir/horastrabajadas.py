# Entrada
horasTrabajadas = input ("Ingrese el numero de horas trabajadas: ")
horasValor = input("Ingrese el valor de cada hora: ")

# Proceso

salarioBruto = float(horasValor) * float(horasTrabajadas)
descuento = salarioBruto * 0.12
salarioTotal = salarioBruto - descuento

# Salida

print("El salario bruto es: ", salarioBruto)
print("El descuento que le hace a su salario da: ", descuento)
print("El salario total es: ", salarioTotal)