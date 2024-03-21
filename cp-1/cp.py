# Lucas Kenji Kikuchi - 554424

valorVenda = input("Venda........................: ")
valorVenda = float(valorVenda)
cupom = input(f"Tem cupom, [s]im ou [n]ão?..: ")

umPorcento = valorVenda / 100

if valorVenda <= 1000:
    desconto = umPorcento * 5
    valorDesconto = valorVenda - desconto
elif valorVenda > 1000:
    desconto = umPorcento * 10
    valorDesconto = valorVenda - desconto

if cupom == "s":
    cupomValor = 50
    valorDesconto = valorDesconto - 50
elif cupom == "n": 
    cupomValor = 0

print("RELATÓRIO: ")
print(f"Venda........: {valorVenda:.2f}")
print(f"Desconto.....: {desconto:.2f}")
print(f"Cupom........: {cupomValor:.2f}")
print(f"Venda Final..: {valorDesconto:.2f}")

    



