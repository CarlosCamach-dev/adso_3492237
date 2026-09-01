nombreCliente = input("Ingrese el nombre del cliente: ")
nombreMascota = input("Ingrese el nombre de la mascota: ")
especie = input("Ingrese que especie de animal es: ")
atencion = input("Que atencion recibio la mascota: ")
pago = 0
if atencion == "Consulta":
    pago = 40000
elif atencion == "Examenes":
    pago = 30000
elif atencion == "Diagnostico":
    pago = 50000
elif atencion == "Urgencia":
    pago = 80000
elif atencion == "Tratamiento":
    pago = 60000

iva = pago * 0.19
pagoTotal = pago + iva

print('='*50)
print(" ")
print("     Clinica Veterinaria     ")
print(" ")
print('='*50)
print(" ")
print(f"Nombre del dueño: {nombreCliente}")
print(f"Nombre de la mascota: {nombreMascota}")
print(f"Especie de la mascota: {especie}")
print(f"Atencion de la mascota: {atencion}")
print(" ")
print('='*50)
print(" ")
print(f"Pago de {atencion}: {pago}")
print(f"Iva: {iva}")
print(f"Pago total: {pagoTotal}")
print(" ")
print('='*50)