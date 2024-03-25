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



