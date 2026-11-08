# Ficha de Actividad: Implementación Modular del Cajero Automático 

**Módulo:** Programación en Python (Optativa 2º DAM)
**Objetivos:** Trabajar la modularidad mediante la importación de archivos, el retorno de valores booleanos para el control de flujo en el bloque principal y la creación de tests unitarios simples.

## 1. Instrucciones para el Alumnado

Vais a estructurar el algoritmo del cajero automático en dos archivos separados para simular un entorno de trabajo real. La lógica de negocio estará en un módulo, y la ejecución del programa en otro.

### Archivo 1: `operaciones_cajero.py` (Módulo de funciones)
Crea las siguientes tres funciones:
1. `solicitar_pin()`: Pide el PIN al usuario, lo convierte a entero y lo devuelve. Usa también manejo de excepciones para comprobar que no se ha convertido correctamente.
2. `verificar_pin(pin_introducido, pin_secreto)`: Simulamos como si fuera una conexión a BD. De momento, compara ambos números y devuelve `True` si coinciden o `False` si no. No debe imprimir nada por pantalla.
3. `iniciar_cajero(pin_secreto, intentos_maximos)`: Contiene el bucle de los intentos. Llama a las dos funciones anteriores. 
    * Si el usuario acierta, la función debe devolver `True`.
    * Si el usuario agota los intentos, la función debe devolver `False`.
    * *Nota:* Esta función sí puede imprimir avisos de "PIN incorrecto" y los intentos restantes, pero **no** los mensajes finales de éxito o bloqueo.

### Archivo 2: `main.py` (Programa principal)
Desde este archivo debes:
1. Importar la función `iniciar_cajero` de tu módulo.
2. Llamar a la función pasándole el PIN secreto y el máximo de intentos (Define ambas con constantes), y guardar su resultado en una variable.
3. Evaluar esa variable con un `if/else` para imprimir el mensaje final: "Acceso permitido" o "Cuenta bloqueada".

---

## 2. Testing Simplificado (`test_cajero.py`)

Al haber sacado los mensajes finales al `main.py` y centrado el módulo en devolver booleanos, el código es extremadamente fácil de testear con simples comprobaciones (`assert`). 

### (Guía docente):

* **¿Qué es un test?** Un test no es más que una función de Python que empieza por la palabra `test_`. Pytest buscará automáticamente cualquier función que se llame así.
* **¿Qué hace el `assert`?** Es como un juez. Evalúa la afirmación que ponemos a su derecha. Si la afirmación es cierta (`True == True`), el test pasa en verde. Si es falsa (`False == True`), el test se rompe en rojo y te avisa del error.
* **Un test por cada caso:** En lugar de hacer parametrizaciones complejas (que es como hacer un bucle de tests), les pedimos que hagan un *copia-pega* de la función de prueba y le cambien el nombre. Un test para el acierto, un test para el fallo y otro test para un caso raro (números negativos). Es repetitivo, pero pedagógicamente asimilan mejor que cada test tiene una única responsabilidad.
* **El concepto de "Mock" (monkeypatch):** ¿Cómo testeamos la función `iniciar_cajero` si se queda esperando a que yo escriba en la consola?". Para ello utilizaremos `monkeypatch` la cual actúa como un "robot invisible" que pulsa las teclas por nosotros para que el test sea automático y no se quede colgado esperando la interacción humana.