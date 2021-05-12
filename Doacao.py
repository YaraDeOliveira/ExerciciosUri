totalviccoin = 0
while True:
    viccoin = float(input())
    if viccoin == -1.0:
        break
    else:
        totalviccoin += viccoin
totreais = totalviccoin * 2.5
print(f'VC$ {totalviccoin:.2f}')
print(f'R$ {totreais:.2f}')
