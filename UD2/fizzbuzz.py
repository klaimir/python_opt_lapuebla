# fizzbuzz.py
def fizzbuzz(numero):
    # Refactorización de la lógica para que pase el test de 15
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)