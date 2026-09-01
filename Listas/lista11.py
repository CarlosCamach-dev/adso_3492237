vector1 = (1,2,3)
vector2 = (-1,0,2)
productoEscalar = 0
mult = 0
for i in range(3):
    mult = vector1[i] * vector2[i]
    productoEscalar = productoEscalar + mult
print("El producto escalar es:", productoEscalar)