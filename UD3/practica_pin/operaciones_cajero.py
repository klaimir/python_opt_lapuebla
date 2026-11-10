def solicitar_pin():
    """Pide el PIN al usuario y asegura que devuelve un entero."""
    while True:
        try:
            return int(input("Introduce tu PIN: "))
        except ValueError:
            print("Error: Por favor, introduce solo números.")

def verificar_pin(pin_introducido, pin_secreto):
    """Devuelve True si los pines coinciden, False en caso contrario."""
    return pin_introducido == pin_secreto

def iniciar_cajero(pin_secreto, intentos_maximos):
    """
    Controla el bucle de intentos. 
    Devuelve True si el usuario hace login correcto, False si se bloquea.
    """
    intentos = intentos_maximos
    
    while intentos > 0:
        pin = solicitar_pin()
        
        if verificar_pin(pin, pin_secreto):
            return True  # Rompe la función y devuelve éxito al main
        else:
            intentos -= 1
            if intentos > 0:
                print(f"PIN incorrecto. Te quedan {intentos} intentos.")
                
    return False  # Si el bucle termina porque intentos llega a 0