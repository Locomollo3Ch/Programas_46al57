# Problema 54.

ahorradores = []
ahorros = []

print("****Registro de Ahorradores****")
print("Escribe 'salir' en el nombre para finalizar el registro.")

while True:
    nombre = input("Ingresa el nombre del ahorrador:\n").strip()
    
    if nombre.lower() == 'salir':
        break
    
    try:
        monto = float(input(f"¿Cuánto ha ahorrado {nombre}?:\n"))
        
        ahorradores.append(nombre)
        ahorros.append(monto)
        print(f"{nombre} registrado con ${monto:,.2f}")
        
    except ValueError:
        print("¡Error! Por favor ingresa un número válido para el ahorro (sin letras ni comas).")

print("\n" + "="*40)
print("REPORTE DE ESTATUS FINANCIERO")
print("-"*40)

for i in range(len(ahorradores)):
    nombre = ahorradores[i]
    monto = ahorros[i]
    
    if monto < 1000:
        print(f"{nombre}: No tendrás para tu futuro")
    
    elif monto > 1000000:
        print(f"{nombre}: Ya merito te retiras")
    
    else:
        print(f"{nombre}: Vas por buen camino (${monto:,.2f})")

print("="*40)