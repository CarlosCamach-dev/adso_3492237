lado1 = int(input("Ingrese el primer lado: "))
lado2 = int(input("Ingrese el segundo lado: "))
lado3 = int(input("Ingrese el tercer lado: "))
if lado1 + lado2 > lado3:
    if lado1 == lado2 == lado3:
        print("Si forma un triangulo, sale un equilatero")
    if lado1 == lado2 != lado3:
        print("Si forma un triangulo, sale un isosceles")
    if lado1 != lado2 != lado3:
        print("Si forma un triangulo, sale un escaleno")
else:
    print("No forma un triangulo")