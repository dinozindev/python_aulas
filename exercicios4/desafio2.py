x = (input("Lados: ")).split()
l, t = [], True
for i in x: l.append(int(i))
l.sort(reverse = True)
if l[1] + l[2] <= l[0]: t = False 
print(f'Não forma um triângulo' if t == False else 'Forma um triângulo') 
if t == True: 
    if (l[0] ** 2) == ((l[1] ** 2) + (l[2] ** 2)): print("Triângulo Retângulo")
    if l[0] == l[1] == l[2]: print('Triângulo Equilátero') 
    elif ((l[0] == l[1]) or (l[1] == l[2])): print('Triângulo Isósceles')
    else: print("Triângulo Escaleno")


# explicação
# l = lados, t = triangulo
# 1. recebe os lados e splita
# 2. define as variáveis lado e triangulo
# 3. para cada lado, transforma-o em int e insere-o no array lado
# 4. faz sort no array, os lados ficam do maior (lado[0]) para o menor (lado[2])
# 5. caso a soma dos dois menores lados seja menor ou igual que o lado maior, não é um triângulo (triangulo = False)
# 6. print da verificação da linha 5
# 7. verificação do tipo (somente se realmente for triangulo)
# 8. verificação do triângulo retângulo
# 9. verificação do triângulo equilátero (todos os lados iguais)
# 10. verificação do triângulo isósceles (somente quando não é equilátero, dois lados iguais)
# 11. verificação do triângulo escaleno (ultimo triangulo possivel, todos os lados diferentes)

