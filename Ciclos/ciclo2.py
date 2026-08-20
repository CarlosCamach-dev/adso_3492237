listaMaterias = []

max = int(input("Ingrese la cantidad de materias: "))

for i in range(max):
    materia = input("Ingrese el nombre de la materia: ")
    listaMaterias.append(materia)

for materia in listaMaterias: #No necesariamente hay que colocar range, con colocar la variable es suficiente. Solo si el usuario coloca un número o desde el programa, se debe colocar range. Ademas, se debe colocar la variable "materia" en el "for" para que el programa sepa que se va a trabajar con esa variable.
    print("Yo estudio", materia)
