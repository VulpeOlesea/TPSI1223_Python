#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

import math

a = float(input("Insira o comprimento do lado do quadrado: "))
def area_quadrado(a: float):
    return a*a

print(f"A área do quadrado é: {area_quadrado(a)}")
print(f"O dobro da área do quadrado é: {area_quadrado(a)*2}")