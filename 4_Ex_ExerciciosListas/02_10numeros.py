# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    lista.append(num)
for num in reversed(lista):
    print(f"Ordem inversa: {num}")

