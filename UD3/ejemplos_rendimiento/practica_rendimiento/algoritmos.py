# Archivo: algoritmos.py

def generar_datos(tamanio):
    """
    Genera una lista de enteros del 0 al tamanio - 1 y añade al final
    el penúltimo elemento para forzar el peor escenario de búsqueda.
    """
    lista = list(range(tamanio))
    if tamanio >= 2:
        lista.append(tamanio - 2)
    return lista

def tiene_duplicados_lento(lista):
    """
    Enfoque A: Implementación mediante bucles anidados.
    """
    n = len(lista)
    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] == lista[j]:
                return True
    return False

def tiene_duplicados_rapido(lista):
    """
    Enfoque B: Implementación mediante conjuntos (Set / Tabla Hash).
    """
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False