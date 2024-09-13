x = int(input())

soma = 0.0
y = 2.0
z = 4.0


if not x>0:
    print("Temq ser maior q zero z�")
else:
    while x >= 1:
        soma = soma + (x/(y*z))
        x = x-1
        y = y + 4
        z = z + 4
    print(f"{soma:.4f}")
