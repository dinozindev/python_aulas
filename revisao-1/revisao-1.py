idade = 30
print(type(idade))

preco_arroz = 11.38
print(type(preco_arroz))

nome = "Carlos"
print(type(nome))

problema = False 
print(type(problema))

kg_arroz = 3.5
preco_arroz = 12.50

valor = kg_arroz * preco_arroz
print(f"O preço total de {kg_arroz:.2f} kg de arroz é de {valor:.2f} reais, porque o preço por kg é de {preco_arroz:.2f}.")

x = 13.43
y = 2.32
z = x * y
print(f"{z:.2f}")
print(format(z, '.2f'))

dividendo = 124
divisor = 5

resto = dividendo % divisor
quociente = dividendo // divisor
resultado = dividendo / divisor

print(resto, quociente, resultado)

# exemplos formatacao 
# <valor>:<caractere><direção><qntd_caracteres-totais>
nome = "Carlos"
# completar com $, para a esquerda, totalizando 10 caracteres.
print(f"{nome:$>10}")
# completar com *, centralizando a variável, totalizando 20 caracteres.
print(f"{nome:*^20}")
# completar com %, para a direita, totalizando 10 caracteres.
print(f"{nome:%<10}")
# completar com espaço em branco, para a esquerda, totalizando 10 caracteres.
print(f"{nome:>10}")
