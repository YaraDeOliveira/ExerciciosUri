nomeVendedor = str(input())
salfixo = float(input())
vendas = float(input())
comissao = vendas*0.15
total = salfixo + comissao
print(f"TOTAL = R$ {total:.2f}")
