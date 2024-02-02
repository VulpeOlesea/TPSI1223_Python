# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def valor(n: int):
    for x in range (1, n+1):
        linha =" ".join(str(x) * x)
        print(f"{linha} ")

n = int(input("Digite um número inteiro: "))

valor(n)
