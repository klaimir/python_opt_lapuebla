import pytest
from operaciones_cajero import verificar_pin, iniciar_cajero

# ==========================================
# TESTS DE LÓGICA PURA (Solo assert simples)
# ==========================================

def test_pin_correcto_devuelve_true():
    # Comprobamos que si le pasamos el PIN correcto, devuelve True
    resultado = verificar_pin(1234, 1234)
    assert resultado == True

def test_pin_incorrecto_devuelve_false():
    # Comprobamos un PIN equivocado
    resultado = verificar_pin(1111, 1234)
    assert resultado == False

def test_pin_negativo_devuelve_false():
    # Comprobamos qué pasa si introducen números negativos
    resultado = verificar_pin(-1234, 1234)
    assert resultado == False


# ==========================================
# TEST SIMULANDO EL TECLADO (Avanzado)
# ==========================================

def test_cajero_bloquea_cuenta_al_agotar_intentos(monkeypatch):
    """
    Explicación para el alumno: 
    'monkeypatch' es una herramienta de pytest. Sirve para engañar a Python.
    Le decimos: 'Cuando el código pida un input(), no esperes a que yo teclee,
    haz de cuenta que el usuario ha escrito "0000" automáticamente'.
    """
    # 1. Engañamos al teclado para que escriba "0000"
    monkeypatch.setattr('builtins.input', lambda _: "0000")
    
    # 2. Ejecutamos la función del cajero (fallará 3 veces seguidas)
    resultado = iniciar_cajero(pin_secreto=1234, intentos_maximos=3)
    
    # 3. Comprobamos que la función devuelve False (Cuenta bloqueada)
    assert resultado == False