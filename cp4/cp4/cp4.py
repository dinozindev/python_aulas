#Nome: Lucas Kenji Kikuchi - RM554424
#Data 21/08/2024
#Luiz Wanderley Tavares
#Computational Thinking Using Python

#O que é lista? R: lista é uma estrutura de dados mutável, definida por colchetes, que aceita múltiplos tipos de elementos. Usada para dados que se alteram constantemente.
#O que é tupla? R: Em comparação a lista, a tupla é uma estrutura de dados imutável, definida por parênteses, usada para dados que não se alteram, como coordenadas, por exemplo.
#O que é dict? R: dicionário é uma estrutura de dados que mapeia chaves a valores em pares, criado com chaves.
#O que é set? R: set é uma estrutura de dados não ordenada de elementos únicos, mutável e criado com chaves.

#1.1 Criação de Lista e Acesso a Elementos:
#• Crie uma lista chamada frutas contendo cinco frutas diferentes. Em
#seguida, acesse e imprima a segunda e a última fruta da lista.

frutas = ['apple', 'grape', 'banana', 'pineapple', 'strawberry']

print(f"Segunda fruta: {frutas[1]}")
print(f"Última fruta.: {frutas[4]}")

#1.2 Adição e Remoção de Elementos:
# • Adicione a fruta “manga” à lista frutas e, em seguida, remova a fruta
# “banana” da lista.

frutas.append('manga')
frutas.remove('banana')

print(f"'manga' adicionada e 'banana' removida: {frutas}")

#1.3 Substituição de Elementos:
# • Substitua o terceiro elemento da lista frutas por “abacaxi”.

frutas.pop(2)
frutas.insert(2, 'abacaxi')

print(f"Terceiro elemento da lista substituido por 'abacaxi': {frutas}")

#1.4 Tamanho da Lista:
# • Crie uma lista chamada numeros contendo os números de 1 a 10. Escreva
# um programa que conte quantos elementos há na lista.

numeros = [1,2,3,4,5,6,7,8,9,10]

print(f"Quantidade de elementos na lista: {len(numeros)}")

#1.5 Soma de Elementos:
# • Usando a lista numeros, calcule e imprima a soma de todos os elementos.

print(f"Soma de todos os elementos: {sum(numeros)}")

#1.6 Média dos Elementos:
# • Com a mesma lista numeros, calcule e imprima a média dos valores da
# lista.

print(f"Média dos números: {sum(numeros) / len(numeros)}")

#1.7 Filtragem de Números Pares:
# • Crie uma nova lista chamada pares contendo apenas os números pares
# da lista numeros.

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Números pares: {pares}")

#1.8 Ordenação de Listas:
# • Dada uma lista chamada idades com valores desordenados, ordene a lista
# em ordem crescente e depois em ordem decrescente.

idades = [5, 12, 86, 4, 15, 32, 14, 2, 45, 18, 75, 54]

idades.sort()
print(f"Lista em ordem crescente: {idades}")

idades.sort(reverse=True)
print(f"Lista em ordem decrescente: {idades}")

#1.9 Lista de Listas:
# • Crie uma lista de listas, onde cada sublista representa um aluno e suas
# notas. Por exemplo: [[“Ana”, 7, 8, 9], [“João”, 6, 7, 8]]. Acesse a segunda
# nota do primeiro aluno e a primeira nota do segundo aluno.

alunos = [['Ana', 7, 8, 9], ['João', 6, 7, 8]]

print(f"Segunda nota do primeiro aluno: {alunos[0][2]}")
print(f"Primeira nota do segundo aluno: {alunos[1][1]}")

#1.10 Contagem de Elementos:
# • Crie uma lista chamada nomes contendo uma sequência de nomes.
# Escreva um programa que conte quantas vezes um nome específico
# aparece na lista.

nomes = ['Carlos', 'Diogo', 'Marcelo', 'João', 'Eduardo', 'Carlos', 'Marcos', 'Jaime', 'Carlos']

print(f"Quantas vezes Carlos aparece na lista: {nomes.count('Carlos')} vezes")

# 2.1 Criação de Dicionário e Acesso a Valores:
# • Crie um dicionário chamado dados_pessoais com as chaves “nome”,
# “idade”, e “cidade”, e preencha com suas informações. Acesse e imprima
# o valor associado à chave “nome”.

dados_pessoais = {'nome': 'Carlos', 'idade': 19, 'cidade': 'Bauru'}

print(f"Nome: {dados_pessoais['nome']}")

# 2.2 Adição e Remoção de Chaves e Valores:
# • Adicione uma nova chave “profissão” ao dicionário dados_pessoais e atribua
# um valor a ela. Em seguida, remova a chave “cidade” do dicionário.

dados_pessoais.update({'profissao': 'Médico'})
print(f"Chave 'profissao' adicionada, juntamente com seu valor: {dados_pessoais}")
dados_pessoais.pop('cidade')
print(f"Chave 'cidade' removida: {dados_pessoais}")


# 2.3 Modificação de Valores:
# • Altere o valor da chave “idade” no dicionário dados_pessoais para refletir
# uma nova idade.

dados_pessoais['idade'] = 18
print(f"Chave 'idade' atualizada de 19 para 18: {dados_pessoais}")

# 2.4 Iteração sobre um Dicionário:
# • Crie um dicionário chamado notas onde as chaves são os nomes dos alunos
# e os valores são suas respectivas notas. Itere sobre o dicionário e imprima
# o nome de cada aluno junto com sua nota.

notas_alunos = {'Carlos': 8.5, 'Marcos': 6.7, 'Márcia': 9, 'Cauan': 7.6}
for aluno in notas_alunos:
    print(f"{aluno} - {notas_alunos[aluno]}")

# 2.5 Verificação de Chaves:
# • Verifique se a chave “endereço” existe no dicionário dados_pessoais. Se não
# existir, adicione-a com um valor apropriado.

print(dados_pessoais.get('endereco', 'Chave não encontrada'))
dados_pessoais.update({'endereco': 'Rua Doze 12'})
print(f"Adicionada nova chave 'endereco' não existente anteriormente: {dados_pessoais}")

# 2.6 Soma dos Valores de um Dicionário:
# • Crie um dicionário chamado precos onde as chaves são os nomes dos
# produtos e os valores são os preços. Calcule e imprima a soma de todos
# os preços.

produtos = {'Pasta de Dente': 5.99, 'Sabonete Líquido': 12.99, 'Shampoo': 14.99, 'Escova de Dente': 8.99}
print(f"Soma dos produtos: R${sum(produtos.values())}")

# 2.7 Conversão de Listas para um Dicionário:
# • Dadas duas listas, uma com nomes de alunos e outra com suas respectivas
# notas, crie um dicionário que mapeie cada nome de aluno para sua nota.

alunos = ['José', 'Marcos', 'Carlos', 'Maria', 'Clara']
notas = [6.7, 7.2, 4.5, 8.3, 7.6]
alunos_notas = {}

for i in range(len(alunos)):
    alunos_notas.update({alunos[i]: notas[i]})

print(f'Alunos e suas notas em formato de dicionário: {alunos_notas}')

# 2.8 Dicionário de Dicionários:
# • Crie um dicionário chamado turma onde as chaves são os nomes dos alunos
# e os valores são outros dicionários que contêm as matérias e suas
# respectivas notas. Por exemplo: {"Ana": {"matematica": 7, "portugues": 8}}.
# Acesse a nota de “portugues” da aluna “Ana”.

turma = {'Marcos': {"matematica": 7, "portugues": 8}, 'Carlos': {"matematica": 7, "portugues": 6}, 'Maria': {"matematica": 9, "portugues": 3}, "Ana": {"matematica": 7, "portugues": 8}}
print(f"Nota de português da aluna Ana: {turma['Ana']['portugues']}")

# 2.9 Contagem de Ocorrências:
# • Dada uma lista de palavras, crie um dicionário que conta quantas vezes cada
# palavra aparece na lista.

palavras = ['cadeira', 'porta', 'vidro', 'janela', 'porta', 'escada', 'torre', 'cadeira', 'cadeira', 'espada', 'caderno']
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(f"Ocorrências: {contagem}")

# 2.10 Criação de um Dicionário Invertido:
# • Dado um dicionário frutas_cor onde as chaves são nomes de frutas e os
# valores são suas respectivas cores, crie um novo dicionário onde as cores
# são as chaves e os valores são listas de frutas que têm essa cor.

frutas_cor = {'maçã': 'vermelho', 'uva': 'roxo', 'morango': 'vermelho', 'laranja': 'laranja', 'toranja': 'laranja', 'abacaxi': 'amarelo'}
cor_frutas = {}
for cor in frutas_cor.values():
    if cor not in cor_frutas:
        cor_frutas[cor] = []

for fruta in frutas_cor.keys():
    cor_frutas[frutas_cor.get(fruta)].append(fruta)

print(f"Dicionário invertido: {cor_frutas}")

# 3.1 Criação e Acesso a Elementos de uma Tupla:
# • Crie uma tupla chamada coordenadas contendo dois números
# representando uma latitude e uma longitude. Acesse e imprima cada
# elemento da tupla separadamente.

coordenadas = (100,-20)
print(f"Latitude.: {coordenadas[0]}°")
print(f"Longitude: {coordenadas[1]}°")

# 3.2 Imutabilidade da Tupla:
# • Crie uma tupla chamada cores com três cores diferentes. Tente alterar um
# dos elementos da tupla e observe o erro gerado. Em seguida, explique por
# que o erro ocorreu.

cores = ('vermelho', 'laranja', 'azul')
# cores.insert('amarelo')

# R: O erro acontece já que a tupla é um iterável imutável, ou seja, não pode ter novos valores adicionados, nem valores já existentes removidos, portanto não possui métodos como .pop() ou .append().

# 3.3 Conversão de Lista para Tupla:
# • Dada uma lista chamada nomes com alguns nomes, converta essa lista
# em uma tupla e imprima o resultado.

nomes = ['Carlos', 'Marcelo', 'Ana']
nomes = tuple(nomes)
print(f"Lista transformada em tupla: {nomes}")

# 3.4 Descompactação de Tupla:
# • Crie uma tupla chamada pessoa com os valores (“João”, 30, “São Paulo”).
# Use descompactação para atribuir esses valores a três variáveis diferetesn
# chamadas nome, idade, e cidade. Imprima cada variável separadamente.

pessoa = ('João', 30, 'São Paulo')

(nome, idade, cidade) = pessoa

print(f"Nome: {nome} - Idade: {idade} - Cidade: {cidade}")

# 3.5 Tupla como Chave em um Dicionário:
# • Crie um dicionário chamado localizacao onde as chaves são tuplas
# representando coordenadas (latitude, longitude) e os valores são nomes
# de cidades. Adicione pelo menos três entradas ao dicionário e acesse o
# nome de uma cidade usando uma das tuplas como chave.
    
localizacao = {(100, -200): 'São Paulo', (-230, 650): 'Toronto', (430, -201): 'Madrid'}
print(f"Acessando a cidade a partir das coordenadas como chave: {localizacao[(-230, 650)]}")

# 4.1 Criação de Conjunto e Acesso a Elementos:
# • Crie um conjunto chamado frutas contendo as frutas “maçã”, “banana”,
# “laranja” e “uva”. Em seguida, tente acessar diretamente um elemento e
# explique o resultado.

frutas = {'maçã', 'banana', 'laranja', 'uva'}
#print(frutas[0])

# R: como um conjunto é uma lista não ordenada, não podemos acessar seus elementos através do índice.

# 4.2 Adição e Remoção de Elementos:
# • Adicione a fruta “manga” ao conjunto frutas e, em seguida, remova a fruta
# “laranja” do conjunto. Imprima o conjunto antes e depois de cada
# operação.

print(f"Conjunto inicial de frutas: {frutas}")
frutas.add('manga')
print(f"Conjunto de frutas após adição da 'manga': {frutas}")
frutas.remove('laranja')
print(f"Conjunto de frutas após a remoção da 'laranja': {frutas}")

# 4.3 Verificação de Pertinência:
# • Verifique se a fruta “banana” está presente no conjunto frutas. Faça o
# mesmo para a fruta “abacaxi” e imprima os resultados.

print(f"Banana está presente no conjunto frutas?.: {'banana' in frutas}")
print(f"Abacaxi está presente no conjunto frutas?: {'abacaxi' in frutas}")

# 4.4 União de Conjuntos:
# • Crie dois conjuntos, set1 com os elementos {1, 2, 3, 4} e set2 com os
# elementos {3, 4, 5, 6}. Calcule a união dos dois conjuntos e imprima o
# resultado.

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(f"União do conjunto set1 com set2: {set1.union(set2)}")

# 4.5 Interseção de Conjuntos:
# • Usando os mesmos conjuntos set1 e set2, calcule a interseção dos dois
# conjuntos e imprima o resultado.

print(f"Interseção dos conjuntos set1 e set2: {set1.intersection(set2)}")

# 4.6 Diferença de Conjuntos:
# • Calcule a diferença entre set1 e set2 (elementos que estão em set1 mas
# não em set2) e imprima o resultado.

print(f"Diferença entre set1 e set2: {set1.difference(set2)}")

# 4.7 Diferença Simétrica:
# • Calcule a diferença simétrica entre set1 e set2 (elementos que estão em
# set1 ou set2, mas não em ambos) e imprima o resultado.

print(f"Diferença simétrica entre set1 e set2: {set1.symmetric_difference(set2)}")

# 4.8 Conversão de Lista para Conjunto (Remoção de Duplicados):
# • Dada uma lista chamada numeros com os valores [1, 2, 2, 3, 4, 4, 5],
# converta essa lista em um conjunto para remover os elementos
# duplicados. Imprima o conjunto resultante.

numeros = [1,2,2,3,4,4,5]
numeros = set(numeros)
print(f"Conversão da lista para conjunto: {numeros}")

# 4.9 Conjunto Imutável (frozenset):
# • Crie um frozenset com os elementos {1, 2, 3}. Tente adicionar um novo
# elemento a ele e observe o que acontece. Explique o motivo.

numeros = {1,2,3}
numeros = frozenset(numeros)
#numeros.add(4)

# R: o método frozenset retorna um set imutável, ou seja, que não pode ser alterado, portanto não podemos adicionar novos valores a ele.

# 4.10 Subconjuntos e Superconjuntos:
# • Crie dois conjuntos, A com os elementos {1, 2, 3} e B com os elementos
# {1, 2, 3, 4, 5}. Verifique se A é um subconjunto de B e se B é um
# superconjunto de A.

A = {1,2,3}
B = {1,2,3,4,5}

print(f"A é subconjunto de B?..: {A.issubset(B)}")
print(f"B é superconjunto de A?: {B.issuperset(A)}")

# 5.1 Criação de Função Simples:
# • Crie uma função chamada saudacao que receba um nome como
# parâmetro e imprima “Olá, [nome]!”.

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Carlos")

# 5.2 Função com Retorno de Valor:
# • Crie uma função chamada soma que receba dois números como
# parâmetros, calcule a soma deles e retorne o resultado.

def soma(a, b):
    return a + b

print(f"Soma: {soma(4,3)}")

# 5.3 Função para Cálculo de Fatorial:
# • Escreva uma função chamada fatorial que receba um número inteiro e
# retorne seu fatorial. Utilize recursão para resolver o problema.

def fatorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * fatorial(x-1)    
print(f"Fatorial de 8: {fatorial(8)}")

# 5.4 Função com Parâmetros Opcionais:
# • Crie uma função chamada imprimir_lista que receba uma lista e um
# booleano chamado reverso (com valor padrão False). Se reverso for True,
# imprima a lista na ordem inversa; caso contrário, imprima na ordem
# normal.

lista = [1,2,3,4,5,6]
def imprimir_lista(lista, reverso=False):
    if reverso==True:
        lista.sort(reverse=True)
        print(f"Lista com reverso == True: {lista}")
    else:
        print(f"Lista com reverso == False (valor padrão): {lista}")

imprimir_lista(lista)

imprimir_lista(lista, True)


# 5.5 Função para Verificar Número Primo:
# • Escreva uma função chamada eh_primo que receba um número inteiro e
# retorne True se o número for primo, e False caso contrário.

def eh_primo(numero_inteiro):
    divisivel = 0
    for i in range(1, numero_inteiro+1):
        if numero_inteiro == 2:
            return True
        elif numero_inteiro % i == 0:
            divisivel+=1
    if divisivel==2:
        return True
    else:
        return False
        
print(f"O número 29 é primo?: {eh_primo(29)}")
        

# 5.6 Função que Utiliza Outra Função:
# • Crie uma função chamada lista_primos que receba um número inteiro n e
# utilize a função eh_primo para gerar uma lista dos primeiros n números
# primos.

def lista_primos(n):
    primos = []
    for i in range(1, n+1):
        if eh_primo(i) == True:
            primos.append(i)
    return primos

print(f"Números primos de 1 a 100: {lista_primos(100)}")


# 5.7 Função para Calcular Média:
# • Escreva uma função chamada media que receba uma lista de números e
# retorne a média dos valores.

def media(lista_numeros=list):
    media = sum(lista_numeros) / len(lista_numeros)
    return media

print(f"Média dos valores: {media([10, 9, 8, 4])}")

# 5.8 Função com Vários Parâmetros:
# • Crie uma função chamada descricao_pessoa que receba um nome, uma
# idade e uma cidade. A função deve retornar uma string no formato “Nome
# tem Idade anos e mora em Cidade”.

def descricao_pessoa(nome, idade, cidade):
    return f"{nome} tem {idade} anos e mora em {cidade}"

print(descricao_pessoa('Carlos', 19, 'Diadema'))

# 5.9 Função com Número Variável de Parâmetros:
# • Escreva uma função chamada soma_multiplos que receba um número
# variável de parâmetros e retorne a soma de todos eles.

def soma_multiplos(*numeros):
    return sum(numeros)

print(f"Soma dos parâmetros variáveis: {soma_multiplos(1,10,3,4,5,90,30)}")

# 5.10 Função para Converter Temperatura:
# • Crie uma função chamada converter_temperatura que receba uma
# temperatura e a unidade de medida (Celsius ou Fahrenheit). Se a unidade
# for Celsius, converta para Fahrenheit, e vice-versa. Retorne a temperatura
# convertida.

def converter_temperatura(temp, unidade):
    if unidade=="Celsius":
        return round(temp * 1.8 + 32, 2)
    elif unidade=="Fahrenheit":
        return round((temp - 32) / 1.8, 2)
    else: 
        print("Insira uma unidade válida.")
    
print(f"Celsius para Fahrenheit: {converter_temperatura(37, 'Celsius')}°F")

print(f"Fahrenheit para Celsius: {converter_temperatura(70, 'Fahrenheit')}°C")

# loop número primo
while True:
    primo = input("Digite um número para ver se é primo ou E para sair do programa: ")
    if primo == 'E':
        break
    elif not primo.isdigit():
        print("\nInsira um valor válido.\n")
        continue
    else:
        primo = int(primo)
        print(f"{primo} é primo?: {eh_primo(primo)}")

# loop fatorial
while True:
    fact = input("Digite um número para verificar seu fatorial ou E para sair do programa: ")
    if fact == 'E':
        break
    elif not fact.isdigit():
        print("\nInsira um valor válido.\n")
        continue
    else:
        fact = int(fact)
        print(f"Fatorial de {fact}: {fatorial(fact)}")

# loop conversão de temperaturas
while True:
    print("\n======= { Conversor de Temperatura } =======\n")
    print("0 - Sair")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius") 
    opt = input("\nQual conversão deseja fazer?: ")
    if not opt.isdigit() or int(opt) > 2 or int(opt) < 0:
        print("\nInsira um valor válido.")
        continue
    opt = int(opt)
    if opt == 0:
        break
    temp = input("Qual a temperatura?: ")
    temp = float(temp)
    match opt:
        case 1:
            print(f"\nCelsius para Fahrenheit: {converter_temperatura(temp, 'Celsius')}°F")
        case 2:
            print(f"\nFahrenheit para Celsius: {converter_temperatura(temp, 'Fahrenheit')}°C") 

            

    

