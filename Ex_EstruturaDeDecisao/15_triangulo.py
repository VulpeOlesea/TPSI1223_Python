# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Os valores podem ser um Triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Os valores podem ser um Triângulo Isósceles.")
    elif a != b and a != c and b != c:
        print("Os valores podem ser um Triângulo Escaleno.")
else:
    print("Os valores não formam um triângulo.")
