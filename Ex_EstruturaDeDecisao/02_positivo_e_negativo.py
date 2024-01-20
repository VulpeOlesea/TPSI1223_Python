# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Digite um número: "))

if num > 0:
    print("Número é positivo")
elif num < 0:
    print("Número é negativo")
else:
    print("Número é zero")