clave = "Python123"
usuario = "admin"
verificacionUsuario = input("Usuario: ")
verificacionCalve = input("Contraseña: ")
if verificacionUsuario == usuario and verificacionCalve == clave:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")