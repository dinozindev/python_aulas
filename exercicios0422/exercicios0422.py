# Exercicio 1 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar

while True:
    n1 = input("Número 1: ")
    if not n1.isdigit():
        print("Insira um valor válido.")
        continue
    n2 = input("Número 2: ")
    if not n2.isdigit():
        print("Insira um valor válido.")
        continue
    n1 = int(n1)
    n2 = int(n2)
    break

while True:
    operacao = input("Qual operação a ser realizada? (+ para soma, - para subtração, * para multiplicação e / para divisão): ")
    if operacao == '+':
        print(f"\nOperação de soma: {n1} + {n2} = {n1 + n2}\n")
        break
    elif operacao == '-':
        print(f"\nOperação de subtração: {n1} - {n2} = {n1 - n2}\n")
        break
    elif operacao == '*':
        print(f"\nOperação de multiplicação: {n1} * {n2} = {(n1 * n2)}\n")
        break
    elif operacao == '/':
        print(f"\nOperação de divisão: {n1} / {n2} = {(n1 / n2):.2f}\n")
        break
    else:
        print("Insira uma opção válida.")
        continue


# Exercício 2 - Divisão por subtrações sucessivas 

while True:
    n1 = input("Número 1: ")
    if not n1.isdigit():
        print("Insira um valor válido.")
        continue
    n2 = input("Número 2: ")
    if not n2.isdigit():
        print("Insira um valor válido.")
        continue
    n1 = int(n1)
    n2 = int(n2)
    break

quociente = 0
resto = n1
while resto >= n2:
    resto-=n2
    quociente+=1
if resto == 0:
    print(f"{n1} / {n2} = {quociente}")
else:
    print(f"{n1} / {n2} = {quociente}, resto = {resto}")   


# Exercício 3 - Verifique se um número é primo

while True:
    n1 = input("\nNúmero primo ou não: ")
    if not n1.isdigit():
        print("Insira um valor válido.")
        continue
    n1 = int(n1)
    break

divisores = 0
for i in range(n1+1): 
    if i == 0: # evita o valor 0 na divisão
        continue
    if i != 2 and i % 2 == 0 and i != n1: #evita valores múltiplos de 2 na divisão (somente se não for o 2 ou o mesmo número que n1)
        continue
    if n1 % i == 0: # se n1 dividido por i não tem resto, quer dizer que é divisível. 
        divisores+=1

if n1 == 0 or n1 == 1: # 0 e 1 não são primos.
    print(f"{n1} não é um número primo.")
elif divisores > 2: # se o número for primo, ele terá apenas 2 divisores (ele mesmo e 1). Caso ele tenha mais de 2, ele não é primo.
    print(f"{n1} não é um número primo.")
else: 
    print(f"{n1} é um número primo.")

# Exercício 4 - Contando caracteres 
dicionario = {} 
frase = input("\nEscreva uma frase: ")
# remove os espaços em branco da frase
fraseSemEspacos = frase.replace(' ', '')
# transforma a string em uma lista
caracteresFrase = list(fraseSemEspacos)

# para cada caractere na lista, se ele já estiver no dicionário, adiciona um em sua contagem. Caso contrário, adiciona ele.
for caractere in caracteresFrase:
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1

print(dicionario)

