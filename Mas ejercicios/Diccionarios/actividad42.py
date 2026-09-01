agendaTelefonica = {}
cant = int(input("Dime la cantidad de contactos que hay: "))
for i in range(cant):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    agendaTelefonica[nombre] = numero 

buscador = input("Ingrese el nombre del contacto que quiere buscar: ")
if buscador in agendaTelefonica: #el in sirve para verificar si el dato esta en el diccionario
    agendaTelefonica.get(buscador) #Sirve para que puedas sacar el key de lo que quiere el usuario
    print(f"Telefono de {nombre}: {numero}")

