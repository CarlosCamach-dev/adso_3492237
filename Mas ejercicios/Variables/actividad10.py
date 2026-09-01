cop = int(input("Ingrese la cantidad de Pesos Colombianos: "))

usd = cop / 4000
eur = cop / 4600

print(f"Pesos Colommbianos: ${cop:.0f}")
print(f"Dolares: {usd:.2f}$")
print(f"Euros: {eur:.2f}Є")