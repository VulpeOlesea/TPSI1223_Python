# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : € 1100,00
#         (-) IR (5%)                     : €   55,00
#         (-) INSS ( 10%)                 : €  110,00
#         FGTS (11%)                      : €  121,00
#         Total de descontos              : €  165,00
#         Salário Liquido                 : €  935,00

din_hora = float(input("Insira quanto ganha por hora: "))
hora = float(input("Insira quantos horas trabalha por mês: "))
salario_bruto = din_hora * hora

if salario_bruto <= 900:
    percento = 0
elif salario_bruto <= 1500:
    percento = 5
elif salario_bruto <= 2500:
    percento = 10
else:
    percento = 20

ir = (percento / 100) * salario_bruto
sindicato = 0.03 * salario_bruto
fgts = 0.11 * salario_bruto
descontos_total = ir + sindicato
salario_liquido = salario_bruto - descontos_total

print(f"Salário Bruto: ({din_hora} * {hora}): € {salario_bruto:.2f}")
print(f"(-) IR ({percento}%): € {ir:.2f}")
print(f"(-) Sindicato (3%): € {sindicato:.2f}")
print(f"FGTS (11%): € {fgts:.2f} ")
print(f"Total de descontos: € {descontos_total:.2f}")
print(f"Salário Liquido: € {salario_liquido}")