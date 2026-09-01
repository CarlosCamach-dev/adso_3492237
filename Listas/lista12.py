matrices = [[[1,2,3],[4,5,6]],[[-1,0],[0,1],[1,1]]]
suma = 0
for matris in range (2):
    for fila in range (len(matrices[matris])):
        for columna in range (len(matrices[matris][fila])):
            for numero in range (len(matrices[matris][fila])):
                 suma += matrices[0][fila][numero] * matrices[1][numero][columna]
                #print(suma)
                       
                #print(f"matris {matris + 1} fila {fila + 1} columna {columna + 1} {matrices[matris][fila][numero]}")
             