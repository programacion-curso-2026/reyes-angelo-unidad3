import random

def es_primo(num):
    """Función auxiliar para verificar si un número es primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# --- Ejercicio A ---
print("--- EJERCICIO A: Número primo aleatorio entre 1 y 100 ---")
while True:
    numero_aleatorio = random.randint(1, 100)
    if es_primo(numero_aleatorio):
        print(f"El número primo aleatorio generado es: {numero_aleatorio}")
        break

print("\n" + "="*50 + "\n")

# --- Ejercicio B ---
print("--- EJERCICIO B: Números primos hasta N ---")
try:
    N = int(input("Ingrese un valor para N: "))
    print(f"Números primos desde el 1 hasta el {N}:")
    primos = [n for n in range(2, N + 1) if es_primo(n)]
    print(primos)
except ValueError:
    print("Por favor, ingrese un número entero válido.")