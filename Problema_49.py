# Problema 49.

inventario = {
    0: {"nombre": "Manzanas", "clave": "75012345", "existencia": 50},
    1: {"nombre": "Leche", "clave": "75098765", "existencia": 24},
    2: {"nombre": "Pan Integral", "clave": "75045678", "existencia": 15},
    3: {"nombre": "Huevos", "clave": "75032109", "existencia": 30},
    4: {"nombre": "Café", "clave": "75065432", "existencia": 10}
}

print("--- Buscador de Inventario (Modo Diccionario) ---")

print("Productos disponibles en el sistema:\n")
for id_producto, datos in inventario.items():
    print(f"[{id_producto}] {datos['nombre']}")

print(f"\nActualmente hay {len(inventario)} productos registrados.")

try:
    seleccion = int(input("Ingresa el número del producto que deseas consultar:\n"))

    if seleccion in inventario:
        producto = inventario[seleccion] 

        print("\n" + "="*30)
        print("INFORMACIÓN DEL PRODUCTO")
        print("-"*30)
        print(f"Nombre:      {producto['nombre']}")
        print(f"Clave (BC):  {producto['clave']}")
        print(f"Existencia:  {producto['existencia']} piezas")
        print("="*30)
    else:
        print("\nError: El ID ingresado no existe en el inventario.")

except ValueError:
    print("\nError: Por favor, ingresa un número entero válido.")