# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import math

lista = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    lista.append(num)

soma = sum(lista)
prod = math.prod(lista)

print(f"Os números digitados: {lista}")
print(f"A soma dos números é: {soma}")
print(f"A multiplicação dos números é: {prod}")