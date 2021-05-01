soma = cont = 0
while True:
    num = int(input())
    if num < 0:
        break
    else:
        soma += num
        cont += 1
print(f'{soma/cont:.2f}')