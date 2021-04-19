L, R = input().split(" ")
R = int(R)
L = int(L)
while not 1 <= L <= 5 and 1 <= R <= 5:
    L, R = input().split(" ")
    R = int(R)
    L = int(L)
soma = L + R
print(soma)


