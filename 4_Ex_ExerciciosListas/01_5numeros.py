# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(num)

print(f"Números digitados: {lista}")