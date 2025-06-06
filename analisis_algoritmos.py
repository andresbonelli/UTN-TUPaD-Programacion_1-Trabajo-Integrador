import time

def fibo_recursivo(n):
    """
    Genera numeros de Fibonacci usando recursión.
    La complejidad de tiempo es exponencial O(2^n) debido a la recursión repetida.
    La complejidad espacial aumenta tambien exponencialmente por la pila de llamadas.
    :param n:
    :return:
    """
    try:
        if n == 0: return 0
        if n == 1: return 1
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)
    except RecursionError:
        print(f'[recursiveFib ERROR] - Recursion depth exceeded')


def fibo_memoizacion(n):
    """
    Esta funcion usa memoizacion (una forma de cacheo) para optimizar la recursión.
    Almacena los numeros que ya fueron computados en un diccionario para evitar cálculos redundantes.
    La complejidad temporal es 0(n), ya que cada numero de Fibonacci es calculado solo una vez, reduciendo
    significativamente el tiempo de ejecución. Sin embargo, tambien usa recursion,
    con lo cual se puede llegar a alcanzar el limite de pila de llamadas en numeros muy altos.
    :param n:
    :return:
    """
    try:
        memo = {0: 0, 1: 1}

        def f(n):
            if n in memo:
                return memo[n]
            memo[n] = f(n - 1) + f(n - 2)
            return memo[n]

        return f(n)
    except RecursionError:
        print(f'[memoizationFib ERROR] - Recursion depth exceeded')
        return None


def fibo_tabulacion(n):
    """
    Esta version utiliza programacion dinamica para calcular numeros de Fibonacci.
    Construye la secuencia de forma iterativa en lugar de recursiva, desde el primer numero hasta
    el numero pasado como parametro, almacenando los resultados en una lista.
    La complejidad temporal es lineal 0(n) ya que no usamos recursion, y la compliejidad espacial
    tambien es 0(n) ya que vamos almacenando la lista completa.
    :param n:
    :return:
    """
    if n < 2: return n
    tab = [0, 1]
    for i in range(2, n + 1):
        new = tab[i - 2] + tab[i - 1]
        tab.append(new)
    return tab[n]


def fibo_optimizado(n):
    """
    Esta version es una optimizacion de la version anterior, que calcula el numero de Fibonacci
    sin necesidad de cacheo. Tiene complejidad temporal 0(n) al igual que el uso de memo,
    pero complejidad espacial constante 0(1) ya que solo se almacenan los ultimos 2 numeros computados
    en lugar de la secuencia completa.
    :param n:
    :return:
    """
    if n < 2: return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b

def medir_tiempo(funcion, *args):
 inicio = time.time()
 resultado = funcion(*args)
 fin = time.time()
 return resultado, fin - inicio

if __name__ == "__main__":
    # Definimos la posicion en la serie de Fibonacci que queremos calcular
    NUMERO_FIBONACCI = 30
    resultado1, tiempo1 = medir_tiempo(fibo_recursivo, NUMERO_FIBONACCI)
    resultado2, tiempo2 = medir_tiempo(fibo_memoizacion, NUMERO_FIBONACCI)
    resultado3, tiempo3 = medir_tiempo(fibo_tabulacion, NUMERO_FIBONACCI)
    resultado4, tiempo4 = medir_tiempo(fibo_optimizado, NUMERO_FIBONACCI)

    print(f"Fibonacci recursivo: Resultado={resultado1}, Tiempo={tiempo1:.8f} segundos.")
    print(f"Fibonacci con memo: Resultado={resultado2}, Tiempo={tiempo2:.8f} segundos.")
    print(f"Fibonacci con tabulacion: Resultado={resultado3}, Tiempo={tiempo3:.8f} segundos.")
    print(f"Fibonacci optimizado: Resultado={resultado4}, Tiempo={tiempo4:.8f} segundos.")

