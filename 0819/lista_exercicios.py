#1. Criação de Lista e Acesso a Elementos:
#• Crie uma lista chamada frutas contendo cinco frutas diferentes. Em
#seguida, acesse e imprima a segunda e a última fruta da lista.

frutas = ['apple', 'grape', 'banana', 'pineapple', 'strawberry']

print(frutas[1])
print(frutas[4])

# 2. Adição e Remoção de Elementos:
# • Adicione a fruta “manga” à lista frutas e, em seguida, remova a fruta
# “banana” da lista.

frutas.append('manga')
frutas.remove('banana')

print(frutas)

# 3. Substituição de Elementos:
# • Substitua o terceiro elemento da lista frutas por “abacaxi”.

frutas.pop(2)
frutas.insert(2, 'abacaxi')

print(frutas)
# 4. Tamanho da Lista:
# • Crie uma lista chamada numeros contendo os números de 1 a 10. Escreva
# um programa que conte quantos elementos há na lista.

numeros = [1,2,3,4,5,6,7,8,9,10]

print(f"Tamanho da lista: {len(numeros)}")

# 5. Soma de Elementos:
# • Usando a lista numeros, calcule e imprima a soma de todos os elementos.

print(f"Soma de todos os elementos: {sum(numeros)}")

# 6. Média dos Elementos:
# • Com a mesma lista numeros, calcule e imprima a média dos valores da
# lista.

print(f"Média: {sum(numeros) / len(numeros)}")

# 7. Filtragem de Números Pares:
# • Crie uma nova lista chamada pares contendo apenas os números pares
# da lista numeros.

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

# 8. Ordenação de Listas:
# • Dada uma lista chamada idades com valores desordenados, ordene a lista
# em ordem crescente e depois em ordem decrescente.

idades = [5, 12, 86, 4, 15, 32, 14, 2, 45, 18, 75, 54]

idades.sort()
print(idades)

idades.sort(reverse=True)
print(idades)

# 9. Lista de Listas:
# • Crie uma lista de listas, onde cada sublista representa um aluno e suas
# notas. Por exemplo: [[“Ana”, 7, 8, 9], [“João”, 6, 7, 8]]. Acesse a segunda
# nota do primeiro aluno e a primeira nota do segundo aluno.

alunos = [['Ana', 7, 8, 9], ['João', 6, 7, 8]]

print(alunos[0][2])
print(alunos[1][1])

# 10. Contagem de Elementos:
# • Crie uma lista chamada nomes contendo uma sequência de nomes.
# Escreva um programa que conte quantas vezes um nome específico
# aparece na lista.

nomes = ['Carlos', 'Diogo', 'Marcelo', 'João', 'Eduardo', 'Carlos', 'Marcos', 'Jaime', 'Carlos']

print(f"Quantas vezes Carlos aparece: {nomes.count('Carlos')} vezes")


# 1. Criação de Dicionário e Acesso a Valores:
# • Crie um dicionário chamado dados_pessoais com as chaves “nome”,
# “idade”, e “cidade”, e preencha com suas informações. Acesse e imprima
# o valor associado à chave “nome”.

dados_pessoais = {'nome': 'Carlos', 'idade': 19, 'cidade': 'Bauru'}

print(f"nome: {dados_pessoais['nome']}")

# 2. Adição e Remoção de Chaves e Valores:
# • Adicione uma nova chave “profissão” ao dicionário dados_pessoais e atribua
# um valor a ela. Em seguida, remova a chave “cidade” do dicionário.

dados_pessoais.update({'profissao': 'Médico'})
dados_pessoais.pop('cidade')
print(dados_pessoais)

# 3. Modificação de Valores:
# • Altere o valor da chave “idade” no dicionário dados_pessoais para refletir
# uma nova idade.

dados_pessoais['idade'] = 18
print(dados_pessoais)

# 4. Iteração sobre um Dicionário:
# • Crie um dicionário chamado notas onde as chaves são os nomes dos alunos
# e os valores são suas respectivas notas. Itere sobre o dicionário e imprima
# o nome de cada aluno junto com sua nota.

notas_alunos = {'Carlos': 8.5, 'Marcos': 6.7, 'Márcia': 9, 'Cauan': 7.6}
for aluno in notas_alunos:
    print(f"{aluno} - {notas_alunos[aluno]}")

# 5. Verificação de Chaves:
# • Verifique se a chave “endereço” existe no dicionário dados_pessoais. Se não
# existir, adicione-a com um valor apropriado.

print(dados_pessoais.get('endereco', 'Chave não encontrada'))
dados_pessoais.update({'endereco': 'Rua Doze 12'})
print(dados_pessoais)

# 6. Soma dos Valores de um Dicionário:
# • Crie um dicionário chamado precos onde as chaves são os nomes dos
# produtos e os valores são os preços. Calcule e imprima a soma de todos
# os preços.

produtos = {'Pasta de Dente': 5.99, 'Sabonete Líquido': 12.99, 'Shampoo': 14.99, 'Escova de Dente': 8.99}
print(f"Soma dos produtos: R${sum(produtos.values())}")

# 7. Conversão de Listas para um Dicionário:
# • Dadas duas listas, uma com nomes de alunos e outra com suas respectivas
# notas, crie um dicionário que mapeie cada nome de aluno para sua nota.

alunos = ['José', 'Marcos', 'Carlos', 'Maria', 'Clara']
notas = [6.7, 7.2, 4.5, 8.3, 7.6]
alunos_notas = {}

for i in range(len(alunos)):
    alunos_notas.update({alunos[i]: notas[i]})

print(alunos_notas)

# 8. Dicionário de Dicionários:
# • Crie um dicionário chamado turma onde as chaves são os nomes dos alunos
# e os valores são outros dicionários que contêm as matérias e suas
# respectivas notas. Por exemplo: {"Ana": {"matematica": 7, "portugues": 8}}.
# Acesse a nota de “portugues” da aluna “Ana”.

turma = {'Marcos': {"matematica": 7, "portugues": 8}, 'Carlos': {"matematica": 7, "portugues": 6}, 'Maria': {"matematica": 9, "portugues": 3}, "Ana": {"matematica": 7, "portugues": 8}}
print(turma['Ana']['portugues'])

# 9. Contagem de Ocorrências:
# • Dada uma lista de palavras, crie um dicionário que conta quantas vezes cada
# palavra aparece na lista.

palavras = ['cadeira', 'porta', 'vidro', 'janela', 'porta', 'escada', 'torre', 'cadeira', 'cadeira', 'espada', 'caderno']
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

# 10. Criação de um Dicionário Invertido:
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

print(cor_frutas)
    


