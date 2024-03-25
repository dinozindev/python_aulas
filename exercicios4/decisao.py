# 8. Dado um número pelo usuário, verifique se ele é “Positivo”, “Negativo” ou “Nulo”(igual a zero).

num = input("numero: ")
num = int(num)

if num > 0:
    print("positivo")
elif num < 0:
    print("negativo")
else:
    print("nulo")


# 9. Dadas três notas (AV1, AV2 e AV3), fazer um algoritmo que calcule a media. A média consiste em descartar a menor nota entre as 3 médias calculando a média simples das outras duas. Exibir se o aluno está “Aprovado” ou “Reprovado” (média menor do que 6).

x = input("Digite as notas: ")
notas = []
soma = 0
status = ''

# insere as notas em uma lista
for i in x.split():
    notas.append(float(i))

# soma as notas da lista
for i in range(len(notas)):
    soma+=notas[i]

# obtem a media dividindo a soma total pela quantidade de itens da lista notas
media = soma / len(notas)

# verificacao de aprovacao e reprovacao
if media >= 6.0:
    status = "Aprovado"
else:
    status = "Reprovado"

print(f"{media:.1f} - {status}")

# 11. Fazer um algoritmo que leia o salário do contribuinte e calcule quanto ele irá pagar de INSS.

salario = float(input("salario: "))
inss = 0

# verificacao em que opcao salario se encaixa (8, 9, 11, teto)
if salario <= 1247.70:
    inss = salario * 0.08
elif salario >= 1247.71 and salario <= 2079.50:
    inss = salario * 0.09
elif salario >= 2079.51 and salario <= 4159.00:
    inss = salario * 0.11
elif salario > 4159.00:
    inss = 468.00

print(f"{inss:.2f}")


# 20. Dados 3 valores numéricos correspondentes a eventuais lados de triângulo, verificar se esses valores formam um triângulo (para cada lado, a soma dos outros dois lados deve ser maior do que ele). Em caso afirmativo, informar ao usuário se o triângulo é equilátero (três lados iguais),isósceles (dois lados iguais) ou escaleno (três lados diferentes). Em caso negativo, exibir “Não forma um triângulo”.

# valor dos três lados.
lados = input("digite os tres lados de um triangulo: ")
lado = []
triangulo = True

for i in lados.split():
    lado.append(int(i))

# verificar se a soma de 2 lados é maior que o terceiro lado. Caso seja, é triângulo. Caso contrário, não é triângulo. 

if lado[0] + lado[1] <= lado[2]:
    triangulo = False
    print('Não forma um triângulo')
elif lado[1] + lado[2] <= lado[0]:
    triangulo = False
    print('Não forma um triângulo')
elif lado[2] + lado[0] <= lado[1]:
    triangulo = False
    print('Não forma um triângulo')
else:
    print('Forma um triângulo')

# verificar o tipo de triângulo retangulo (o quadrado do maior lado é igual a soma dos quadrados dos outros dois lados)
lado.sort(reverse = True)
if (lado[0] ** 2) == ((lado[1] ** 2) + (lado[2] ** 2)):
    print("Triângulo Retângulo")

# verifica triangulo equilatero (todos os lados iguais)
# verifica triangulo isosceles (dois lados iguais)    
if (2 * lado[0]) == (lado[1] + lado[2]):
    print('Triângulo Equilátero')
elif lado[0] == lado[2]:
    print('Triângulo Isósceles')
elif lado[1] == lado[2]:
    print('Triângulo Isósceles')
elif lado[0] == lado[1]:
    print("Triângulo Isósceles")

# verifica triangulo escaleno (tres lados diferentes)
if (lado[0] != lado[1]) and (lado[1] != lado[2]) and (lado[2] != lado[0]) and triangulo == True:
    print("Triângulo Escaleno")


