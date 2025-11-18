# codigo_original.py
# Búsqueda de números primos en el rango 1..100000 (versión sin optimizar)
# Autor: Gaby Ocampo
# Fecha: 18/11/2025

import time

def es_primo(n):
    """Comprobación simple: prueba divisores desde 2 hasta n-1 (ineficiente)."""
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def main():
    inicio = time.perf_counter()
    primos = []
    for num in range(1, 100_001):
        if es_primo(num):
            primos.append(num)
    fin = time.perf_counter()
    print(f"Número de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución (segundos): {fin - inicio:.6f}")

if __name__ == "__main__":
    main()
