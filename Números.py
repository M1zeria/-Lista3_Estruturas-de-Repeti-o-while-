pares = 0
impares = 0
positivos = 0
negativos = 0

N = int(input())

while N != 0:
    if N % 2 == 0:
        pares = pares+1
    if N % 2 != 0:
        impares = impares+1
    if N > 0:
        positivos = positivos+1
    if N < 0:
        negativos = negativos+1
    N = int(input())
if pares == 1:
    print(f"{pares} valor par")
if pares != 1:
    print(f"{pares} valores pares")
if impares == 1:
    print(f"{impares} valor impar")
if impares != 1:
    print(f"{impares} valores impares")
if positivos == 1:
    print(f"{positivos} valor positivo")
if positivos != 1:
    print(f"{positivos} valores positivos")
if negativos == 1:
    print(f"{negativos} valor negativo")
if negativos != 1:
    print(f"{negativos} valores negativos")

