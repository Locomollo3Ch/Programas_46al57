# Problema 55.

def mostrar_menu():
    print("****MENÚ DE OPERACIONES****")
    print("1. Agregar valor")
    print("2. Eliminar valor (por dato o índice)")
    print("3. Ordenar lista (modificar original)")
    print("4. Ver copia ordenada (sin modificar original)")
    print("5. Buscar elemento e índices")
    print("6. Estadísticas (Solo números)")
    print("7. Ver lista actual")
    print("8. Salir")
    return input("Selecciona una opción:\n")

tipo_lista = input("¿Deseas crear una lista de (N)úmeros o de (T)exto?:\n").strip().lower()
lista = []

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        valor = input("Ingresa el valor a agregar:\n")
        if tipo_lista == 'n':
            try:
                lista.append(float(valor))
            except ValueError:
                print("Error: Debes ingresar un número.")
        else:
            lista.append(valor)

    elif opcion == "2":
        sub_opc = input("Eliminar por (V)alor o (I)ndice?:\n").lower()
        try:
            if sub_opc == 'v':
                val = float(input("Valor:\n")) if tipo_lista == 'n' else input("Valor:\n")
                lista.remove(val)
            else:
                idx = int(input("Índice:\n"))
                lista.pop(idx)
            print("Eliminado con éxito.")
        except (ValueError, IndexError):
            print("Error: Valor o índice no válido.")

    elif opcion == "3":
        lista.sort()
        print("Lista original ordenada.")

    elif opcion == "4":
        print(f"Copia ordenada: {sorted(lista)}")
        print(f"Original sigue igual: {lista}")

    elif opcion == "5":
        busqueda = input("Elemento a buscar:\n")
        if tipo_lista == 'n': busqueda = float(busqueda)
        
        if busqueda in lista:
            indices = [i for i, x in enumerate(lista) if x == busqueda]
            print(f"El elemento '{busqueda}' está en los índices: {indices}")
        else:
            print("No se encontró el elemento.")

    elif opcion == "6":
        if tipo_lista == 'n' and lista:
            maximo = max(lista)
            minimo = min(lista)
            suma = sum(lista)
            promedio = suma / len(lista)
            print(f"\nEstadísticas:\n- Máximo: {maximo}\n- Mínimo: {minimo}\n- Suma: {suma}\n- Promedio: {promedio:.2f}")
        else:
            print("Operación no disponible para texto o lista vacía.")

    elif opcion == "7":
        print(f"Lista actual: {lista}")

    elif opcion == "8":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")