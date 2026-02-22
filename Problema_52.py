# Problema 52.

productos = ["Monitor G-Sync", "Teclado Mecánico", "Mouse Gamer", "Audífonos Pro", "Tapete XL"]
precios = [4500.50, 1200.00, 850.00, 2100.00, 450.00]
ventas = [12, 45, 78, 23, 60]

print("-" * 75)
print(f"{'PRODUCTO':<20} | {'PRECIO':>12} | {'VENTAS':>10} | {'INGRESO':>15}")
print("-" * 75)

total_ingresos = 0

for i in range(len(productos)):
    ingreso_producto = precios[i] * ventas[i]
    total_ingresos += ingreso_producto
    
    print(f"{productos[i]:<20} | {precios[i]:>12.2f} | {ventas[i]:>10} | ${ingreso_producto:>14.2f}")

print("-" * 75)
print(f"{'TOTAL GENERAL':<48} | ${total_ingresos:>14.2f}")