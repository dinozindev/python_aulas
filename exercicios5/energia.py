# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

instalacao = {'instalacao': {'R': {'500':0.4,'resto':0.65}, 
                             'I': {'1000':0.55,'resto': 0.60}, 
                             'C': {'5000':0.55,'resto': 0.60}}}

kwh = int(input("Quantidade de kWh consumida: "))
instalacao = input("Tipo de instalacao (R para residencias, I para industrias e C para comercios): ")

campo0 = list(instalacao['instalacao'][instalacao][0])
val_comp = float(campo0)

if kwh == val_comp:
    preco = instalacao['instalacao'][instalacao][campo0]
else:
    preco = instalacao['instalacao'][instalacao]['resto']

custo = preco * kwh
print(f"Valor a pagar: {custo}")

# if instalacao.upper() == "R" and kwh <= 500:
#     valorPagar = kwh * 0.4
#     print(f"Valor a pagar: {valorPagar}")
# if instalacao.upper() == "R" and kwh > 500:
#     valorPagar = kwh * 0.65
#     print(f"Valor a pagar: {valorPagar}")

# if instalacao.upper() == "C" and kwh <= 1000:
#     valorPagar = kwh * 0.55
#     print(f"Valor a pagar: {valorPagar}")
# if instalacao.upper() == "C" and kwh > 1000:
#     valorPagar = kwh * 0.60
#     print(f"Valor a pagar: {valorPagar}")

# if instalacao.upper() == "I" and kwh <= 5000:
#     valorPagar = kwh * 0.55
#     print(f"Valor a pagar: {valorPagar}")
# if instalacao.upper() == "I" and kwh > 5000:
#     valorPagar = kwh * 0.60
#     print(f"Valor a pagar: {valorPagar}")

