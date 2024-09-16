# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado

a = int(input("coloque sua média"))
if a>=7:
    print("aprovado")
elif a<5:
    print("reprovado")
else:
    print("recuperação")