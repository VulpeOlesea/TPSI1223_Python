# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

lista = []
aluno_media = 0

for aluno in range(10):
    soma = 0
    for nota in range(4):
        notas = float(input(f"Digite a {nota+1}º nota do {aluno+1}º aluno: "))
        soma += notas
    media = soma / 4
    lista.append(media)
    if media >= 7:
        aluno_media += 1

print(f"Tem {aluno_media} aluno(s) com média maior ou igual a 7.0.")
