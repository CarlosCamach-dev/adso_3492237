contador = int(input("Ingrese la cantidad de segundos: "))
hora = contador / 3600
minutos = (contador / 60) % 60
segundos = contador % 60
print(contador, "segundos equivalen a: ")
print(" ")
print(f"{hora:.0f} Hora(s)")
print(f"{minutos:.0f} Minuto(s)")
print(f"{segundos:.0f} Segundo(s)")