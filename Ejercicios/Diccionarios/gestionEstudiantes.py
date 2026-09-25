gestionEstudiantes = {}
promedios = []
cant = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(cant):
    codigo = int(input("Codigo del Estudiante: "))
    nombre = input("Nombre del Estudiante: ")
    edad = int(input("Edad del Estudiante: "))
    carrera = input("Carrera del Estudiante: ")
    promedio = float(input("Promedio del Estudiante: "))
    gestionEstudiantes[codigo] = nombre, edad, carrera, promedio

print("Mejor Estudiante: ")
for datos in gestionEstudiantes.values():
    promedios.append(datos[3])
maxPromedio = max(promedios)
for codigo, datos in gestionEstudiantes.items():
    if datos[3] == maxPromedio:
        print(f"""
        Codigo: {codigo}
        Nombre: {datos[0]}
        Edad: {datos[1]}
        Carrera: {datos[2]}
        Promedio: {datos[3]}""")
