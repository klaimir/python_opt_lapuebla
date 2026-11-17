# Archivo: main_fibonacci.py
import timeit
from algoritmos_fibonacci import fibonacci_recursivo, fibonacci_iterativo

n = 32
repeticiones = 10  # Ejecutaremos cada algoritmo 10 veces

print(f"Calculando Fibonacci({n}) ejecutado {repeticiones} veces seguidas...\n")

# 1. Medición del enfoque recursivo O(2^n)
# Usamos lambda para pasar argumentos a la función dentro de timeit
tiempo_rec = timeit.timeit(lambda: fibonacci_recursivo(n), number=repeticiones)

# 2. Medición del enfoque iterativo O(n)
tiempo_ite = timeit.timeit(lambda: fibonacci_iterativo(n), number=repeticiones)

print(f"[O(2^n)] Recursivo : {tiempo_rec:.6f} segundos (total {repeticiones} ejecuciones)")
print(f"[O(n)]   Iterativo : {tiempo_ite:.6f} segundos (total {repeticiones} ejecuciones)")
print(f"\nDiferencia: El método iterativo es {int(tiempo_rec / tiempo_ite):,} veces más rápido.")