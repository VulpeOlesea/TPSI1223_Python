# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(num1, num2, num3):
    return num1 + num2 + num3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terseiro número: "))

print("Soma de três argumentos é: ", soma(num1, num2, num3))