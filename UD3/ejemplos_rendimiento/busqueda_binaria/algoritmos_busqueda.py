# Archivo: algoritmos_busqueda.py

def busqueda_lineal(lista, objetivo):
    """
    Enfoque A: Búsqueda Lineal - Orden Lineal O(n).
    Recorre la lista elemento por elemento desde el inicio.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista_ordenada, objetivo):
    """
    Enfoque B: Búsqueda Binaria - Orden Logarítmico O(log n).
    Requisito indispensable: La lista debe estar previamente ordenada.
    Descarta la mitad de los elementos en cada iteración.
    """
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista_ordenada[medio]

        if valor_medio == objetivo:
            return medio  # Elemento encontrado
        elif valor_medio < objetivo:
            izquierda = medio + 1  # Descartamos la mitad izquierda
        else:
            derecha = medio - 1  # Descartamos la mitad derecha

    return -1  # Elemento no encontrado
