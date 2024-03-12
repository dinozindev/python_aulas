segundos = input("segundos: ")
segundos = int(segundos)

minutos = 0
convertidoHoras = 0
convertidoSegundos = 0

minutosInteiro = segundos // 60
minutos = segundos / 60
# primeiro, obtemos a casa decimal dos minutos (equivalem aos segundos), arredondamos para duas casas decimais e multiplicamos por 60, obtendo o valor em segundos. Depois, arredondamos novamente, obtendo o valor inteiro.
convertidoSegundos = round(round((minutos - minutosInteiro), 2) * 60)

# obtenção das horas inteiras e horas com valor dos minutos nos decimais
horasInteiro = int(minutos // 60)
horas = round(minutos / 60, 2)

# obtemos os minutos em decimais
decimalMinutos = (horas - horasInteiro)
# transformamos os decimais em minutos
convertidoMinutos = int(decimalMinutos * 60)

print(f"{horasInteiro}h{convertidoMinutos}min{convertidoSegundos}s")
