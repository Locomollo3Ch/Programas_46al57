# Problema 57.

palabra = input("Ingrese la palabra a buscar:\n")

palabras = ["Príncipe Andrés", "Bill Clinton", "Donald Trump", \
            "Bill Gates", "Stephen Hawking", "Kevin Spacey"]

x = palabras.count(palabra)
if x != 0:
    print("Si esta en la lista.")
else:
    print("No esta en la lista.")