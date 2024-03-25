# 1. Dado um número, exibir os seus 10 primeiros múltiplos
num = int(input("numero: "))
for i in range(1, 11):
    print(num * i)

# V2. Exibir em formato de tabuada
num = int(input("número: "))
# multiplica o numero de 1 a 10
print(f"Tabuada do {num}")
for i in range(1, 11):
    # imprimir o resultado
    print(f"{i:2.0f} x {num:2.0f} = {(i * num):2.0f}")

# V3. Pedir o multiplicando e exibir no formato de tabuada
x = input("numero e multiplicando: ")

numeros = []

for i in x.split():
    numeros.append(int(i))

for i in range(1, numeros[1]):
    print(f"{numeros[0]:2.0f} X {i:2.0f} = {(numeros[0] * i):2.0f}")


# 2. Somar números até que seja digitado zero
numeros = input("numeros: ")
lista = []
soma = 0

# insere os numeros na lista como int
for numero in numeros.split():
    lista.append(int(numero))

# quando encontra um 0 na lista, quebra o loop (para que o restante dos números não seja somado). Caso contrario, soma. 
for i in range(len(lista)):
    if lista[i] == 0:
        break
    else:
        soma+=lista[i]
    
print(soma)

# V2. Somar números até que seja digitado um numero negativo

numeros = input("numeros: ")
lista = []
soma = 0

# insere os numeros na lista como int
for numero in numeros.split():
    lista.append(int(numero))

# quando um número negativo é encontrado no loop, soma primeiro, e depois quebra.  
for i in range(len(lista)):
    if lista[i] < 0:
        soma+=lista[i]
        break
    else:
        soma+=lista[i]
    
print(soma)


# V3. Somar números até que seja digitado um numero negativo. O numero negativo não fará parte da somatória.
numeros = input("numeros: ")
lista = []
soma = 0

# insere os numeros na lista como int
for numero in numeros.split():
    lista.append(int(numero))

# quando um número negativo é encontrado no loop, quebra, fazendo com que ele não seja somado. 
for i in range(len(lista)):
    if lista[i] < 0:
        break
    else:
        soma+=lista[i]
    
print(soma)


# 1. Em uma votação, existem 3 candidatos: 1 – Huguinho, 2 – Zezinho e 3 – Luizinho. Pedir e acumular votos até que em votos seja digitado o numero 0 (zero). Ao final, exibir a quantidade de votos de cada usuário.

print("1 - HUGUINHO \n2 - ZEZINHO \n3 - LUIZINHO\n0 - SAIR")
x = input("votos: ")

votos = []
votosHuguinho = 0
votosZezinho = 0
votosLuizinho = 0
palavraH = "VOTO" 
palavraZ = "VOTO" 
palavraL = "VOTO"

# adiciona os votos para uma lista
for i in x.split():
    votos.append(int(i))

# contabiliza os votos e quebra caso encontre o numero 0
for i in range(len(votos)):
    if votos[i] == 0:
        break
    elif votos[i] == 1:
        votosHuguinho+=1
    elif votos[i] == 2:
        votosZezinho+=1
    elif votos[i] == 3:
        votosLuizinho+=1

# verificação plural
if votosHuguinho == 1:
    palavraH = "VOTO"
else:
    palavraH = "VOTOS"

if votosZezinho == 1:
    palavraZ = "VOTO"
else:
    palavraZ = "VOTOS"

if votosLuizinho == 1:
    palavraL = "VOTO"
else:
    palavraL = "VOTOS"

print(f"1 - HUGUINHO: {votosHuguinho:>10} {palavraH}")
print(f"2 - ZEZINHO: {votosZezinho:>11} {palavraZ}")
print(f"3 - LUIZINHO: {votosLuizinho:10} {palavraZ}")

# V2. A condição de saída será digitar [S]im ou [N]ão (seja maiúsculo ou minúsculo).

print("1 - HUGUINHO \n2 - ZEZINHO \n3 - LUIZINHO\n0 - SAIR")
x = input("votos: ")

votos = []
votosHuguinho = 0
votosZezinho = 0
votosLuizinho = 0
palavraH = "VOTO" 
palavraZ = "VOTO" 
palavraL = "VOTO"

# caso o item seja 1, 2 ou 3, transforma em int e insere na lista. Caso contrario, transforme em letra maiuscula.
for i in x.split():
    if i == '1' or i == '2' or i == '3':
        votos.append(int(i))
    else: 
        votos.append(i.upper())

# caso encontre 'S', continua o loop. Caso encontre 'N', quebra o loop. 
for i in range(len(votos)):
    if votos[i] == "S":
        continue
    elif votos[i] == "N":
        break
    elif votos[i] == 1:
        votosHuguinho+=1
    elif votos[i] == 2:
        votosZezinho+=1
    elif votos[i] == 3:
        votosLuizinho+=1

if votosHuguinho == 1:
    palavraH = "VOTO"
else:
    palavraH = "VOTOS"

if votosZezinho == 1:
    palavraZ = "VOTO"
else:
    palavraZ = "VOTOS"

if votosLuizinho == 1:
    palavraL = "VOTO"
else:
    palavraL = "VOTOS"

print(f"1 - HUGUINHO: {votosHuguinho:>10} {palavraH}")
print(f"2 - ZEZINHO: {votosZezinho:>11} {palavraZ}")
print(f"3 - LUIZINHO: {votosLuizinho:10} {palavraL}")

# V3. Caso digite uma letra diferente de S ou N, dar uma mensagem de erro e forças a digitação de S ou N.

# lacos todos os exs 
