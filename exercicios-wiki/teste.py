# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = input(f"Qual o tamanho do arquivo?: ")
tamanho = float(tamanho)
velocidade = input(f"Qual a velocidade em mbps?: ")
velocidade = float(velocidade)

mbPorSec = velocidade / 8

tempo = tamanho / mbPorSec
tempoMin = tempo / 60

print(f"tempo demorado: {tempo:.2f} segundos / {tempoMin:.2f} minutos")