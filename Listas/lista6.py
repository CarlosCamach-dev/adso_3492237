listaMaterias = []
notas = []
max = int(input("Ingrese la cantidad de materias: "))
for i in range(max):
     materia = input("Ingrese el nombre de la materia: ") 
     listaMaterias.append(materia) 
     print(' ')

for materia in listaMaterias: 
   nota = float(input("Ingrese la nota de la materia " + materia + ": "))
   notas.append(nota)
   print(' ')

for i in range(len(notas)- 1, -1, -1): #En esta parte me confundo bastante por hacerlo a la inversa el conteo de la lista, (inicio, final, paso) es asi el range, el "final" quiere decir que debe terminar ANTES de x numero y el "inicio" debe restarse para que sea un indice en vez de un numero normal. 
     if notas[i] > 3:
         listaMaterias.pop(i) #El pop solo sirve para eliminar un elemento de una lista utilizando su posicion. a diferencia que remove que elimina un valor.
     else: 
         print("Tiene que repetir la materia", listaMaterias[i])
     print(' ')