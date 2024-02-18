# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []

for i in range(10):
    caracter = str(input(f"Digite o {i+1}º caracter: ")).strip()
    lista.append(caracter)

consoante = 0
vogais = 'AEIOU'
for caracter in lista:
    if caracter.isalpha() and caracter.upper() not in vogais:
        consoante += 1
        print(caracter)

print(f"A lista tem {consoante} consoante(s).")