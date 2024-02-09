# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

import ExerciciosClasses

comprimento = float(input("Digite o comprimento do local: "))
largura = float(input("Digite a largura do local: "))

retangulo = ExerciciosClasses.Retangulo(comprimento, largura)
print("Área do local é:", retangulo.calcularArea())
print("Perímetro do local é:", retangulo.calcularPerimetro())