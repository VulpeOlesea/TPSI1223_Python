# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Insira o peso de peixe (em quilos): "))

if peso_peixe > 50:
    peso_excesso = peso_peixe - 50
    multa = peso_excesso * 4
    print(f"Você excedeu o peso permitido em {peso_excesso} quilos.")
    print(f"O valor de sua multa é de {multa} R$.")
else:
    print("Você não excedeu o peso permitido.")


