
# valores iniciais
quantia = 1
ced100 = 3
ced50 = 3
ced20 = 5
ced10 = 10

# Valor total de todas as cédulas disponíveis.
vlrt = (ced100 * 100) + (ced50 * 50) + (ced20 * 20) + (ced10 * 10)
print((ced100 * 100) + (ced50 * 50) + (ced20 * 20) + (ced10 * 10))

# Chamada inicial da quantia.
quantia = input("Digite uma quantia para saque: ")
quantia = float(quantia)

# Caso a quantia informada para saque seja maior que o valor disponível em cédulas, um novo valor será pedido. 
if quantia > vlrt:
        print("Valor inválido. Insira um valor que esteja disponível no caixa eletrônico.")
        quantia = input("quantia: ")
        quantia = float(quantia)

# Caso não haja cédulas de 50 e 10, apenas quantias de múltiplo 20 serão admitidas. 
if ced50 == 0 and ced10 == 0:
    while quantia % 20:
        print("Valor inválido. Insira um valor múltiplo de 20.")
        quantia = input("Digite uma quantia para saque: ")
        quantia = float(quantia)
# Apenas valores múltiplos de 10 serão aceitos como valores válidos caso haja cédulas de 50 e 10
else: 
    while quantia % 10:
        print("Valor inválido. Insira um valor múltiplo de 10.")
        quantia = input("Digite uma quantia para saque: ")
        quantia = float(quantia)

# Verificação cédulas de 100

# Se ced100 for maior ou igual a quantia // 100, o valor de ced100 se torna a quantidade de cedulas que podem ser entregue e a quantia tem o valor das cedulas reduzida. 
# Caso ced100 seja menor que a quantia // 100, será usado apenas as cédulas disponíveis.  
# Caso ced100 seja igual a zero, retorna zero.
if ced100 >= quantia // 100:
    ced100 = quantia // 100
    quantia = quantia - (ced100 * 100)  
elif ced100 < quantia // 100:
    quantia = quantia - (ced100 * 100)  
else:
    ced100 = 0


# verifica quantidade de cedulas de 50, removendo o valor total das cédulas de 50.
if ced50 >= quantia // 50:
    ced50 = quantia // 50
    quantia = quantia - (ced50 * 50)
elif ced50 < quantia // 50:
    quantia = quantia - (ced50 * 50)  
else:
    ced50 = 0


# verifica quantidade de cedulas de 20, removendo o valor total das cédulas de 20.
if ced20 >= quantia // 20:
    ced20 = quantia // 20
    quantia = quantia - (ced20 * 20)
elif ced20 < quantia // 20:
    quantia = quantia - (ced20 * 20)  
else:
    ced20 = 0 


# verifica quantidade de cedulas de 10, removendo o valor total das cédulas de 10.
if ced10 >= quantia // 10:
    ced10 = quantia // 10
    quantia = quantia - (ced10 * 10)
elif ced10 < quantia // 10:
    quantia = quantia - (ced10 * 10)  
else:
    ced10 = 0

# transformando em ints
ced100 = int(ced100)
ced50 = int(ced50)
ced20 = int(ced20)
ced10 = int(ced10)

print(f"R$100,00 - {ced100} cédulas (R${ced100 * 100},00)")
print(f"R$50,00 - {ced50} cédulas (R${ced50 * 50},00)")
print(f"R$20,00 - {ced20} cédulas (R${ced20 * 20},00)")
print(f"R$10,00 - {ced10} cédulas (R${ced10 * 10},00)")