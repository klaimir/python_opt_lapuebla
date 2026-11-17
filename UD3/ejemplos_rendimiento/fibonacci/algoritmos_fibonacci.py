# Archivo: algoritmos_fibonacci.py

def fibonacci_recursivo(n):
    """
    Enfoque A: Implementación Recursiva Pura - Orden Exponencial O(2^n).
    Cada llamada genera dos nuevas llamadas recursivas.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_iterativo(n):
    """
    Enfoque B: Implementación Iterativa - Orden Lineal O(n).
    Recorre los elementos una única vez mediante un bucle.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
