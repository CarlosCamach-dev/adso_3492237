num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("""Seleccione una opción:
1. Sumar
2. Restar
3. MUltiplicar
4. Dividir""")
opcion = int(input("Ingrese su opción: "))
if opcion == 1:
    resultado = num1 + num2
elif opcion == 2:
    resultado = num1 - num2
elif opcion == 3:
    resultado = num1 * num2
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: No se puede dividir entre cero.")
        resultado = None
if resultado is not None:
    print("El resultado es:", resultado)

#None sirve para dar un valor nulo a una variable, en vez de colocar 0.