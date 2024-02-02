# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o número real: "))

prod = (num1 * 2) * (num2 / 2)
soma = (3 * num1) + num3
cubo = num3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {prod}")
print(f"A soma do triplo do primeiro com o terceiro: {soma}")
print(f"O terceiro elevado ao cubo: {cubo}")