
convertido = 0
convertidoDecimal = 0
casaDecimal = 0
minutosNaHora = 0

minutos = input("minutos: ")
minutos = int(minutos)

conversao = input("Deseja converter para 'segundos' ou 'horas'?: ")

# valor convertido em segundos
if conversao == 'segundos':
    convertido = minutos * 60
    print(f"{minutos} minutos equivalem a {convertido} segundo(s).")
# valor convertido em horas
elif conversao == 'horas':
    # valor inteiro
    convertido = minutos // 60
    # valor em decimal com duas casas
    convertidoDecimal = round(minutos / 60, 2)
    # obtendo o valor da casa
    casaDecimal = convertidoDecimal - convertido
    # obtendo o valor da casa decimal em minutos
    minutosNaHora = round(casaDecimal * 60)
    print(f"{minutos} minutos equivalem a {convertido}h{minutosNaHora}min")