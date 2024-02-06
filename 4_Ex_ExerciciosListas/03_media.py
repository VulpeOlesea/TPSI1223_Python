# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}º nota: "))
    notas.append(nota)

print(f"Notas digitadas: {notas}")
media = sum(notas) / 4
print(f"Nota média é: {media}")