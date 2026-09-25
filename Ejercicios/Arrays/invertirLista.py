listaPalabras = []
cant = int(input("Ingrese la cantidad de palabras: "))
for i in range(cant):
    palabras = input("Ingrese la palabra: ")
    listaPalabras.append(palabras)

listaPalabras.reverse()

print("Palabras en orden inverso:")
for palabra in listaPalabras:
    print(palabra)