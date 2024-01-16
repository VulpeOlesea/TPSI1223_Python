# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior_numero = max(num1, num2, num3)
menor_numero = min(num1, num2, num3)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
