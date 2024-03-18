# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

int1 = input("Número inteiro 1: ")
int1 = int(int1)
int2 = input("Número inteiro 2: ")
int2 = int(int2)
real = input("Número real: ")
real = float(real)

produto = (int1 * 2) * (int2 / 2)
soma = (int1 * 3) + real
elevado = real ** 3

print(f"{produto}, {soma}, {elevado}")


# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = input("Insira sua altura: ")
altura = float(altura)

formula = (72.7 * altura) - 58

print(f"Seu peso ideal é: {formula:.2f}kg")


# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = input("Insira sua altura: ")
h = float(h)
genero = input("M ou H?: ")

if genero == "H":
    formulaH = (72.7 * h) - 58
    print(f"Seu peso ideal é: {formulaH:.2f}kg")
else:
    formulaM = (62.1 * h) - 44.7
    print(f"Seu peso ideal é: {formulaM:.2f}kg")

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
    
peso = input("Peso dos peixes: ")
peso = float(peso)
excesso = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"Excesso de peso: {excesso:.2f}kg | Multa: {multa:.2f} reais")
else:
    print("Peso dentro do regulamento.")


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganhoHora = input("Quanto você ganha por hora?: ")
ganhoHora = float(ganhoHora)
horasTrabalhadas = input("Quantas horas trabalhou no mês?: ")
horasTrabalhadas = float(horasTrabalhadas)

salarioBruto = ganhoHora * horasTrabalhadas

umPorcento = salarioBruto / 100

ir = umPorcento * 11
inss = umPorcento * 8
sindicato = umPorcento * 5

salarioLiquido = salarioBruto - ir - inss - sindicato

print(f"Salário líquido: {salarioLiquido:.2f} reais")


# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = input("Área a ser pintada (em metros quadrados): ")
area = float(area)

areaLitros = area / 3
litrosTotais = areaLitros / 18
litrosTotaisInt = int(litrosTotais)

# 1 lata = 54 metros quadrados = 18 litros
if areaLitros % 18:
    totalLatas = litrosTotaisInt + 1
    print(f"Total latas: {totalLatas} | Preço total: {totalLatas * 80} reais")
else:
    print(f"Total latas: {litrosTotaisInt} | Preço total: {litrosTotaisInt * 80} reais")



# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = input(f"Qual o tamanho do arquivo?: ")
tamanho = float(tamanho)
velocidade = input(f"Qual a velocidade em mbps?: ")
velocidade = float(velocidade)

mbPorSec = velocidade / 8

tempo = tamanho / mbPorSec
tempoMin = tempo / 60

print(f"tempo demorado: {tempo:.2f} segundos / {tempoMin:.2f} minutos")

