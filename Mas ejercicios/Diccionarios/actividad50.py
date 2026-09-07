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
for valor in gestionEstudiantes.values():
        promedios.append(valor[3])
maxPromedio = max(promedios)
for codigo, valor in gestionEstudiantes.items():
      if valor[3] == maxPromedio:
            print(f"""
            Codigo: {codigo}
            Nombre: {valor[0]}
            Edad: {valor[1]}
            Carrera: {valor[2]}
            Promedio: {valor[3]}""")
