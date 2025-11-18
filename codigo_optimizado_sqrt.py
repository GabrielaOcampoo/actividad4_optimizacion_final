# codigo_optimizado_sqrt.py
# Optimización: probar divisores solo hasta sqrt(n) y usar list comprehensions donde aplica.
import time
import math

def es_primo_sqrt(n):
    """Comprueba primalidad probando divisores hasta sqrt(n)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.isqrt(n))
    for d in range(3, limite + 1, 2):  # solo impares
        if n % d == 0:
            return False
    return True

def main():
    inicio = time.perf_counter()
    primos = [num for num in range(1, 100_001) if es_primo_sqrt(num)]
    fin = time.perf_counter()
    print(f"Número de primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución (segundos): {fin - inicio:.6f}")

if __name__ == "__main__":
    main()
