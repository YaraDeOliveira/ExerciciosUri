inicio = int(input())
fim = int(input())
contprimos = contadivisor = 0
for c in range(inicio, fim+1):
    for d in range(1, fim+1):
        if c % d == 0:
            contadivisor += 1
        if contadivisor > 2:
            break
    if contadivisor == 2:
        print(c)
        contprimos += 1
    contadivisor = 0
print(f'primos: {contprimos}')
