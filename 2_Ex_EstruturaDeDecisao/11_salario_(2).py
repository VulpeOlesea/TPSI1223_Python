# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até € 280,00 (incluindo) : aumento de 20%
# salários entre € 280,00 e € 700,00 : aumento de 15%
# salários entre € 700,00 e € 1500,00 : aumento de 10%
# salários de € 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario_atual = float(input("Insira o seu salário: "))

if salario_atual <= 280:
    percento = 20
elif 280 < salario_atual <= 700:
    percento = 15
elif 700 < salario_atual <= 1500:
    percento = 10
else:
    percento = 5

salario_aumento = (percento / 100) * salario_atual
novo_salario = salario_atual + salario_aumento

print(f"O salário antes do reajuste: {salario_atual:.2f} €")
print(f"O percentual de aumento aplicado: {percento}%")
print(f"O valor do aumento: {salario_aumento:.2f} €")
print(f"O novo salário, após o aumento: {novo_salario:.2f} €")
