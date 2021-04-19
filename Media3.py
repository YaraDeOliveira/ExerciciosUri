N1, N2, N3, N4 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
media = (N1*2+N2*3+N3*4+N4*1)/10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    novamedia = (media + exame) / 2
    if novamedia >= 5.0:
        print("Aluno aprovado.")
    else:
        print(("Aluno reprovado."))
    print(f"Media final: {novamedia:.1f}")
