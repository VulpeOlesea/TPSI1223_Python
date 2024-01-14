# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input("Digite o tamanho de um arquivo para download em MB: "))
velocidade = int(input("Digite a velocidade de um link de Internet em Mbps: "))

tempo = (tamanho * 8) / velocidade
minutos = int(tempo // 60)
segundos = int(tempo % 60)

print(f"O tempo de download de {tamanho} MB com a velocidade de {velocidade} Mbps é: {minutos} min e {segundos} seg")