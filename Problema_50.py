# Problema 50.

inventario = {
    0: {"nombre": "Manzanas", "clave": "75012345", "existencia": 50},
    1: {"nombre": "Leche", "clave": "75098765", "existencia": 24},
    2: {"nombre": "Pan Integral", "clave": "75045678", "existencia": 15},
    3: {"nombre": "Huevos", "clave": "75032109", "existencia": 30},
    4: {"nombre": "Café", "clave": "75065432", "existencia": 10}
}

print("****Buscador Global de Inventario****")
print("Productos disponibles:\n")
for id_p, datos in inventario.items():
    print(f"[{id_p}] {datos['nombre']} (Clave: {datos['clave']})")

busqueda = input("\nIngresa el ID, Nombre o Clave del producto:\n").strip()

producto_encontrado = None

if busqueda.isdigit():
    id_num = int(busqueda)
    if id_num in inventario:
        producto_encontrado = inventario[id_num]

if not producto_encontrado:
    for id_p, datos in inventario.items():
        if busqueda.lower() == datos['nombre'].lower() or busqueda == datos['clave']:
            producto_encontrado = datos
            break

if producto_encontrado:
    print("\n" + "="*30)
    print("INFORMACIÓN DEL PRODUCTO")
    print("-"*30)
    print(f"Nombre:      {producto_encontrado['nombre']}")
    print(f"Clave (BC):  {producto_encontrado['clave']}")
    print(f"Existencia:  {producto_encontrado['existencia']} piezas")
    print("="*30)
else:
    print(f"\nNo se encontró ningún producto que coincida con: '{busqueda}'")