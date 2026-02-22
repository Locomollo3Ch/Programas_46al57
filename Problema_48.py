# Problema 48.

nombres = ["Manzanas", "Leche", "Pan Integral", "Huevos", "Café"]
claves = ["75012345", "75098765", "75045678", "75032109", "75065432"]
existencias = [50, 24, 15, 30, 10]

print("--- Buscador de Inventario ---")

print("\nProductos disponibles:")
for i in range(len(nombres)):
    print(f"[{i}] {nombres[i]}")

print(f"\nActualmente hay {len(nombres)} productos registrados.")

try:
    indice = int(input("Ingresa el número del producto que deseas consultar:\n"))

    if 0 <= indice < len(nombres):
        print("\n" + "="*30)
        print("INFORMACIÓN DEL PRODUCTO")
        print("-"*30)
        print(f"Nombre:      {nombres[indice]}")
        print(f"Clave (BC):  {claves[indice]}")
        print(f"Existencia:  {existencias[indice]} piezas")
        print("="*30)
    else:
        print("\nError: El índice está fuera de rango. Intenta con un número de la lista.")

except ValueError:
    print("\nError: Por favor, ingresa un número entero válido.")