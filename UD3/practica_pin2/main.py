from operaciones_cajero import iniciar_cajero

PIN_CORRECTO = 1234
MAX_INTENTOS = 3

# Llamamos a la función y guardamos el booleano que nos devuelve
try:
    login_exitoso = iniciar_cajero(PIN_CORRECTO, MAX_INTENTOS)

    # El main toma el control de los mensajes finales
    if login_exitoso:
        print("Acceso permitido. Bienvenido al sistema.")
    else:
        print("Cuenta bloqueada. Ha agotado sus intentos.")
except ValueError as e:
    print(e)