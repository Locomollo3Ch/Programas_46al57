# Problema 53.

datos = []

print("****Registro de Datos Dinámico****")
print("Escribe tus datos uno por uno. Para finalizar, escribe 'no' o 'salir'")

while True:
    entrada = input("Ingresa un dato (o 'no' para terminar):\n").strip()
    
    if entrada.lower() in ['no', 'n', 'salir', 'exit']:
        break
    
    if entrada:
        datos.append(entrada)
    else:
        print("Entrada vacía omitida.")

datos.sort()

print("\n" + "="*30)
print("LISTA FINAL ORDENADA")
print("-"*30)

if datos:
    for i, item in enumerate(datos, 1):
        print(f"{i}. {item}")
else:
    print("La lista está vacía.")

print("="*30)