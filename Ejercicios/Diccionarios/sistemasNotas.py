notasEstudiantes = {}
cant = int(input("Ingrese la cantidad de estudiantes: "))
for i in range(cant):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    notasEstudiantes[nombre] = nota

print("El estudiante con la mejor nota es:")
for nombre, nota in notasEstudiantes.items():
    if nota == max(notasEstudiantes.values()):
        print(f"{nombre} -> {nota}")
#Value sirve para obtener el valor de un diccionario e items sirve para obtener tanto la clave como el valor de un diccionario.