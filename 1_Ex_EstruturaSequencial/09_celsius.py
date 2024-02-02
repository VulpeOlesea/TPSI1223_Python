# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

grausF = float(input("Digite a temperatura em graus Fahrenheit: "))
grausC = 5 * ((grausF - 32) / 9)

print(f"{grausF} graus Fahrenheit em graus Celsius é: {grausC}")