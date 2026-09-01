listaEstudiantes = {}
cant = int(input("Dime la cantidad de estudiantes que hay: "))
for i in range(cant):
    codigo = input("Ingrese el codigo del estudiante: ")
    estudiante = input("Ingrese el nombre del estudiante: ")
    listaEstudiantes[codigo] = estudiante #para ingresar un key y un valor se debe hacer de esta manera

print ('='*50)
print("Lista de estudiantes")
print(" ")
for codigo in listaEstudiantes: #en este caso, se debe utilizar el codigo y lista para el for
    print(f"{codigo} --> {estudiante}")
    print(" ")
print('='*50)