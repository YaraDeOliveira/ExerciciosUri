X = int(input())
Y = int(input())
if X > Y:
    aux = X
    X = Y
    Y = aux
soma = 0
for c in range(X+1, Y):
    if c % 2 != 0:
        soma += c
print(soma)