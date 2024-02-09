# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

import ExerciciosClasses

tamanho = float(input("Digite o tamanho do lado do quadrado: "))

quadrado = ExerciciosClasses.Quadrado(tamanho)
print("Tamanho do lado do quadrado:", quadrado.retornarTamanho())
print("Área do quadrado:", quadrado.calcularArea())

print("---" * 15)
mudar_tamanho = float(input("Digite o novo tamanho do lado do quadrado: "))

quadrado.mudarTamanho(mudar_tamanho)
print("Novo tamanho do lado do quadrado:", quadrado.retornarTamanho())
print("Nova área do quadrado:", quadrado.calcularArea())