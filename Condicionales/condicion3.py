nota = float(input("Ingrese el promedio del estudiante: "))
asistencia = int(input("Ingrese el porcentaje de asistencia del estudiante: "))

if nota >= 3 and asistencia >= 80:
          print(f"El estudiante paso la materia con promedio de {nota:.1f} ","y con asistencia de", asistencia)
else:
          print(f"El estudiante no paso la materia con promedio de {nota:.1f} ","y con asistencia de", asistencia)