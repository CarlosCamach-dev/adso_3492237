libreria = {}
cant = int(input("Ingrese la cantidad de libros: "))
for i in range(cant):
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    libreria[codigo] = titulo

buscador = input("Ingrese el código del libro que quiere buscar: ")
if buscador in libreria:
    print(f"""Libro encontrado:
    {buscador} -> {libreria[buscador]}""")
else:
    print("El libro no se encuentra en la librería.")