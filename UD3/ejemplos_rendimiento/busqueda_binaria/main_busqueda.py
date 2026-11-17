# Archivo: main_busqueda.py
import timeit
from algoritmos_busqueda import busqueda_lineal, busqueda_binaria

tamanio = 10_000_000  # 10 millones de registros ordenados
datos = list(range(tamanio))
objetivo = 9_999_999  # Peor caso: el último elemento
repeticiones = 100

print(f"Buscando el elemento {objetivo:,} en una lista de {tamanio:,} elementos...")
print(f"Realizando {repeticiones} búsquedas por cada algoritmo...\n")

# Medición Lineal O(n)
t_lineal = timeit.timeit(lambda: busqueda_lineal(datos, objetivo), number=repeticiones)

# Medición Binaria O(log n)
t_binaria = timeit.timeit(lambda: busqueda_binaria(datos, objetivo), number=repeticiones)

print(f"[O(n)]     Búsqueda Lineal  : {t_lineal:.6f} segundos")
print(f"[O(log n)] Búsqueda Binaria : {t_binaria:.6f} segundos")
print(f"\nLa búsqueda binaria fue {int(t_lineal / t_binaria):,} veces más rápida.")