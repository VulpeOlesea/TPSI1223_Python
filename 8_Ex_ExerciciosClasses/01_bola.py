# Classe Bola: Crie uma classe que modele uma bola:
#
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

import ExerciciosClasses

cor = input("Digite a cor: ")
circ = input("Digite a circunferência: ")
material = input("Qual o material: ")

bola = ExerciciosClasses.Bola(cor,circ,material)

print("---" * 10)
bola.mostraCor()

print("---" * 10)
nova_cor = input("Digite a nova cor: ")
bola.trocaCor(nova_cor)
bola.mostraCor()