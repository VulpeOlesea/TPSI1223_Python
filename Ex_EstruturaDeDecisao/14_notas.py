# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média das notas {nota1} e {nota2} é: {media}")

if 9 <= media < 10:
    print(f"Média de Aproveitamento: A")
    print("APROVADO")
elif 7.5 <= media < 9:
    print(f"Média de Aproveitamento: B")
    print("APROVADO")
elif 6 <= media < 7.5:
    print(f"Média de Aproveitamento: C")
    print("APROVADO")
elif 4 <= media < 6:
    print(f"Média de Aproveitamento: D")
    print("REPROVADO")
elif 0 <= media < 4:
    print(f"Média de Aproveitamento: E")
    print("REPROVADO")
else:
    print("Digite as notas de 1 a 10")