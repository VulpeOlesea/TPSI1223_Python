# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : €
# - IR (11%) : €
# - INSS (8%) : €
# - Sindicato ( 5%) : €
# = Salário Liquido : €
# Obs.: Salário Bruto - Descontos = Salário Líquido.

din_hora = float(input("Insira quanto ganha por hora: "))
hora = float(input("Insira quantos horas trabalha por mês: "))

salario_bruto = din_hora * hora
ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato

print(f"+ Salário Bruto: {salario_bruto} €")
print(f"- IR (11%): {ir} €")
print(f"- INSS (8%): {inss} €")
print(f"- Sindicato (5%): {sindicato} €")
print(f"= Salário Liquido: {salario_liquido} €")