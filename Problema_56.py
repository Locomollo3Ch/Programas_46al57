# Problema 56.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

ultimo = numeros[-1]

for i in range(1, 11):
    numeros.append(ultimo + i)

print("Lista extendida:")
print(numeros)