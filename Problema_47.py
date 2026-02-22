# Problema 47.

def calificaciones():
    try:
        n = int(input("Ingrese la cantidad de materias que registrara:\n"))
    except ValueError:
        print("Ingrese una cantidad válida.")
        return
    
    resultados = []

    for i in range(n):
        print(f"\n****Materia {i+1}****")
        nombre_materia = input("Nombre de la materia:\n")
        
        notas = input(f"Introduce las notas de {nombre_materia} separadas por espacio (o una sola nota):\n")
        
        lista_notas = [float(nota) for nota in notas.split()]
        
        if len(lista_notas) > 0:
            promedio = sum(lista_notas) / len(lista_notas)
        else:
            promedio = 0.0
        
        resultados.append((nombre_materia, promedio))
    print("\n" + "="*30)
    print(f"{'Materia':<20} | {'Promedio':<10}")
    print("-" * 30)
    for materia, promedio in resultados:
        print(f"{materia:<20} | {promedio:.2f}")
    print("="*30)

if __name__ == "__main__":
    calificaciones()