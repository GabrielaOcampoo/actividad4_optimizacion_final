# codigo_optimizado_numpy_sieve.py
# Criba de Eratóstenes con NumPy para encontrar primos hasta 100000
import time
import numpy as np

def sieve_numpy(n):
    """Criba de Eratóstenes vectorizada con NumPy."""
    if n < 2:
        return np.array([], dtype=np.int64)
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[:2] = False  # 0 y 1 no son primos
    limite = int(np.sqrt(n))
    for p in range(2, limite + 1):
        if is_prime[p]:
            is_prime[p*p:n+1:p] = False
    return np.nonzero(is_prime)[0]  # devuelve arreglo de primos

def main():
    inicio = time.perf_counter()
    primos = sieve_numpy(100_000)
    fin = time.perf_counter()
    print(f"Número de primos encontrados: {primos.size}")
    print(f"Tiempo de ejecución (segundos): {fin - inicio:.6f}")

if __name__ == "__main__":
    main()
