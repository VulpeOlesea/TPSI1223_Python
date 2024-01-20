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

def percentual(salario_atual: float):
    if salario_atual <= 280:
        percento = salario_atual * 0.2
        print("O percentual de aumento aplicado: 20%")
        print(f"O valor do aumento: {percento:.2f} €")
    elif 280 < salario_atual <= 700:
        percento = salario_atual * 0.15
        print("O percentual de aumento aplicado: 15%")
        print(f"O valor do aumento: {percento:.2f} €")
    elif 700 < salario_atual <= 1500:
        percento = salario_atual * 0.1
        print("O percentual de aumento aplicado: 10%")
        print(f"O valor do aumento: {percento:.2f} €")
    else:
        percento = salario_atual * 0.05
        print("O percentual de aumento aplicado: 5%")
        print(f"O valor do aumento: {percento:.2f} €")
    return percento

salario_atual = float(input("Insira o seu salário: "))

print(f"O salário antes do reajuste: {salario_atual:.2f} €")
print(f"O novo salário, após o aumento: {percentual(salario_atual) + salario_atual:.2f} €")
