# Problema 51.

try:
    n = int(input("Trabajadores a registrar:\n"))
    
    nombres = []
    asistencias = []

    for i in range(n):
        nombre = input(f"Ingrese el nombre del trabajador {i+1}:\n")
        asistencia = input(f"¿Asistió {nombre}? (Escribe 1 para SÍ, 0 para NO):\n")
        
        while asistencia not in ["0", "1"]:
            print("Entrada inválida. Por favor ingresa 0 o 1.")
            asistencia = input(f"¿Asistió {nombre}? (1 para SÍ, 0 para NO): ")
            
        nombres.append(nombre)
        asistencias.append(int(asistencia))

    print("\n****REPORTE DE ASISTENCIA****")
    for i in range(n):
        estado = "asistió" if asistencias[i] == 1 else "no asistió"
        print(f"{nombres[i]} {estado} a trabajar.")

except ValueError:
    print("Error: Debes ingresar un número entero para la cantidad de trabajadores.")