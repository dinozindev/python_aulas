
# valores iniciais
quantia = 1
ced100 = 3
ced50 = 0
ced20 = 5
ced10 = 0
problema = False

# Valor total de todas as cédulas disponíveis.
vlrt = (ced100 * 100) + (ced50 * 50) + (ced20 * 20) + (ced10 * 10)
print(f"Valor disponível no caixa eletrônico: R${vlrt:.2f}")

# Chamada inicial da quantia.
quantia = input("Digite uma quantia para saque: ")
quantia = float(quantia)

# Se uma das três condições for atendida, a variável problema é dada como true.
if quantia > vlrt or quantia % 10 or (ced50 == 0 and ced10 == 0 and quantia % 20):
    problema = True

# condicionais enquanto o problema persistir
while problema == True:
    # quantia para saque maior que o valor do caixa.
    if quantia > vlrt:
        print("Valor inválido. Insira uma quantia que esteja disponível no caixa eletrônico.")
        quantia = input("Digite uma quantia para saque: ")
        quantia = float(quantia)
    # quantia não é múltiplo de 10.
    elif quantia % 10:
        print("Valor inválido. Insira um valor múltiplo de 10.")
        quantia = input("Digite uma quantia para saque: ")
        quantia = float(quantia)
    # sem notas de 50 e 10, quantia não é múltiplo de 20.
    elif ced50 == 0 and ced10 == 0 and quantia % 20:
        print("Valor inválido. Caixa sem notas de 50 e 10. Insira um valor múltiplo de 20.")
        quantia = input("Digite uma quantia para saque: ")
        quantia = float(quantia)
    # problema = false caso não haja mais erros. 
    else:
        problema = False   


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

print("Valor sacado: ")
print(f"R$100,00: {ced100} cédulas (R${(ced100 * 100):.2f})")
print(f"R$50,00: {ced50} cédulas (R${(ced50 * 50):.2f})")
print(f"R$20,00: {ced20} cédulas (R${(ced20 * 20):.2f})")
print(f"R$10,00: {ced10} cédulas (R${(ced10 * 10):.2f})")