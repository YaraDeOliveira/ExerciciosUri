diaSemana = str(input()).lower()
while True:
    qtdeDiasEntrega = int(input())
    if 0 <= qtdeDiasEntrega <= 6:
        break
if diaSemana == 'domingo':
    x = 1
elif diaSemana == "segunda":
    x = 2
elif diaSemana == "terca":
    x = 3
elif diaSemana == "quarta":
    x = 4
elif diaSemana == "quinta":
    x = 5
elif diaSemana == "sexta":
    x = 6
else:
    x = 7
diaEntrega = x + qtdeDiasEntrega
if diaEntrega > 7:
    diaEntrega = diaEntrega - 7
if qtdeDiasEntrega == 0:
    print('chega hoje!')
elif diaEntrega == 1:
    print('sera entregue domingo')
elif diaEntrega == 2:
    print('sera entregue segunda')
elif diaEntrega == 3:
    print('sera entregue terca')
elif diaEntrega == 4:
    print("sera entregue quarta")
elif diaEntrega == 5:
    print("sera entregue quinta")
elif diaEntrega == 6:
    print("sera entregue sexta")
else:
    print("sera entregue sabado")