year = int(input("Ingrese el año que desees: "))

if year % 4 or year % 400 :
    print("El año", year ," es bisiesto")

    print("El año", year," no es bisiesto")