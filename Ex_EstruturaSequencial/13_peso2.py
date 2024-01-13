# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

genero = input("Insira seu gênero (M para masculino, F para feminino): ")

if genero == "M":
    altura = float(input("Insira sua altura: "))
    peso_ideal = (72.7 * altura) - 58

    print(f"Seu peso ideal é: {peso_ideal}")
elif genero == "F":
    altura = float(input("Insira sua altura: "))
    peso_ideal = (62.1 * altura) - 44.7

    print(f"Seu peso ideal é: {peso_ideal}")