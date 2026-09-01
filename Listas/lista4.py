listaGanadores = []
for i in range(5):
    numero = input("Ingrese el numero ganador de la lotería La Primitiva: ")
    listaGanadores.append(numero)

listaGanadores.sort(key=int) 
print("Los números ganadores son:" , listaGanadores)
#Este comando lo que hace es ordenar la lista de menor a mayor, y el "key=int" lo que hace es que el programa interprete que los valores son enteros. tambien se puede colocarse de mayor a menor colocando dentro de () "reverse=True".
