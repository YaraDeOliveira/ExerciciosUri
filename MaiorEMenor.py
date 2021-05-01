maior = pos = 0
for c in range(0, 5):
    x = int(input())
    while x < 0:
        x = int(input())
    if c == 0:
        maior = x
    elif x > maior:
        maior = x
        pos = c + 1
print(maior)
print(pos)