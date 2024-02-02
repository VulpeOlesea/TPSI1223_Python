# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero_dia = int(input("Digite um número de dia da semana (de 1 a 7): "))

if numero_dia == 1:
    print(f"O número {numero_dia} é Domingo")
elif numero_dia == 2:
    print(f"O número {numero_dia} é Segunda-feira")
elif numero_dia == 3:
    print(f"O número {numero_dia} é Terça-feira")
elif numero_dia == 4:
    print(f"O número {numero_dia} é Quarta-feira")
elif numero_dia == 5:
    print(f"O número {numero_dia} é Quinta-feira")
elif numero_dia == 6:
    print(f"O número {numero_dia} é Sexta-feira")
elif numero_dia == 7:
    print(f"O número {numero_dia} é Sábado")
else:
    print("Valor inválido")
