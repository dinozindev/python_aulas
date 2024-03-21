# Lucas Kenji Kikuchi - 554424

valorVenda = input("Venda........................: ")
valorVenda = float(valorVenda)

# verifica valores negativos
# while valorVenda < 0:
#     valorVenda = input("Venda........................: ")
#     valorVenda = float(valorVenda)

# verifica se o valor digitado é 's' ou 'n'. Se não, perguntar novamente
cupom = input(f"Tem cupom, [s]im ou [n]ão?..: ")
while cupom != "s" and cupom != "n":
   cupom = input(f"Tem cupom, [s]im ou [n]ão?..: ") 

# 1% do valor da venda
umPorcento = valorVenda / 100

# verificação e aplicação do desconto
if valorVenda <= 1000:
    desconto = umPorcento * 5
    valorDesconto = valorVenda - desconto
elif valorVenda > 1000:
    desconto = umPorcento * 10
    valorDesconto = valorVenda - desconto

# verificação e aplicação do desconto do cupom
if cupom == "s":
    cupomValor = 50
    valorDesconto = valorDesconto - 50
elif cupom == "n": 
    cupomValor = 0

# evitar valores negativos após desconto
# if valorDesconto < 0:
#     valorDesconto = 0

print("RELATÓRIO: ")
print(f"Venda........: {valorVenda:.2f}")
print(f"Desconto.....: {desconto:.2f}")
print(f"Cupom........: {cupomValor:.2f}")
print(f"Venda Final..: {valorDesconto:.2f}")

    



