# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam € 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_a_pintar = float(input("Insira a área em metros quadrados necessaria para pintar: "))

lata_tinta = (area_a_pintar - 1) // (18 * 3) + 1
preco_tinta = lata_tinta * 80

print(f"Para {area_a_pintar} metros quadrados é necessaria {lata_tinta} de latas de tinta.")
print(f"Preço total: {preco_tinta} €.")