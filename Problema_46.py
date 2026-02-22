# Problema 46

numeros = []

print("Ingrese 10 números:")
for i in range(10):
    num = float(input(f"Número {i + 1}:\n"))
    numeros.append(num)


cuadrados = [n*n for n in numeros]
print("Los números originales son: \n", numeros,)
print("Los cuadrados de los números son: \n", cuadrados)