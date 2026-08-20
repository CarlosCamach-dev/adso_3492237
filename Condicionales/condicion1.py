horasTrabajadas = float(input("Cuantas horas trabaja la persona?: "))
valorHoras = float(input("Cuanto es el valor de cada hora?: "))
print('+'*50)
if horasTrabajadas > 40:
        extra = horasTrabajadas - 40
        pago = horasTrabajadas * valorHoras + (extra * (horasTrabajadas * 2))

pago = horasTrabajadas * valorHoras

print(f"El pago que debe recibir el empleado es: {pago:.0f}")