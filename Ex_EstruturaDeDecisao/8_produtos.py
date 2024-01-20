# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço de primeiro produto: "))
produto2 = float(input("Digite o preço de segundo produto: "))
produto3 = float(input("Digite o preço de terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O mais barato é primeiro produto o que tem valor {produto1} €")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O mais barato é segundo produto o que tem valor {produto2} €")
elif produto3 < produto1 and produto3 < produto2:
    print(f"O mais barato é terceiro produto o que tem valor {produto3} €")
elif produto1 == produto2 and produto1 < produto3:
    print(f"Os primeiro e segundo produtos são os mais baratos com valor {produto1} €")
elif produto1 == produto3 and produto1 < produto2:
    print(f"Os primeiro e terceiro produtos são os mais baratos com valor {produto1} €")
elif produto2 == produto3 and produto2 < produto1:
    print(f"Os segundo e terceiro produtos são os mais baratos com valor {produto2} €")
else:
    print(f"Todos os produtos são iguais com valor {produto1} €")




