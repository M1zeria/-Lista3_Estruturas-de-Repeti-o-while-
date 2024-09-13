x = int(input())
y = x

while True:
    if y == 0:
        break
    if x % y == 0:
        print(y)
    y = y-1
