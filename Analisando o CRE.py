menor = 999
matrb = "x"
creTotal = 0
totalAlunos = 0
while True:
    matr = str(input())
    if matr == "999":
        break
    cre = float(input())
    if cre < menor:
        matrb = matr
        menor = cre

    creTotal = creTotal + cre
    totalAlunos += 1

print(matrb)
print(f"{creTotal/totalAlunos:.2f}")
