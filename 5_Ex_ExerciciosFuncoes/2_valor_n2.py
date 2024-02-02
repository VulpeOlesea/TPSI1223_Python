# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def valor(n: int):
    for x in range(1, n+1):
        for linha in range(1, x+1):
            print(linha, end=" ")
        print("")

n = int(input("Digite um número inteiro: "))

valor(n)