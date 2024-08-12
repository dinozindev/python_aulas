fruits = ['apple', 'lemon', 'apple', 'pear', 'banana', 'orange', 'kiwi']
print(type(fruits))

# pega o ultimo valor da lista
print(fruits[-1])

# adiciona um elemento ao final da lista
fruits.append("pineapple")
print(fruits)

# conta quantos elementos x existem na lista
print(fruits.count('apple'))

# remove a primeira instancia do elemento especificado
fruits.remove('apple')
print(fruits)

# remove pelo indice
fruits.pop(2)
print(fruits)

# ordena em ordem alfabetica
fruits.sort()
print(fruits)

# ordena em ordem alfabetica inversa
fruits.sort(reverse=True)
print(fruits)

# retorna os valores de indice 2 ate indice 4 (nao conta o indice 4, apenas 2 e 3)
print(fruits[2:4])

# semelhante ao for padrao, mas resumido
numeros = [1,2,3,4,5]
y = [x**2 for x in numeros]
print(y)

# a tupla nao pode ter seus valores alterados
a = (1,2,3)
# 'tuple' object has no attribute 'remove'
# a.remove(1)

tarifa_dict = {
    "onibus": {
        'RJ': 9,
        'SP': 10,
        'ZZ': 5
    },
    "taxi": {
        'RJ': 15,
        'SP': 20,
        'AL': 50,
        'ZZ': 30
    }
}

# retorna as keys
print(tarifa_dict.keys())
# retorna as keys e values juntos
print(tarifa_dict.items())
# retorna os values
print(tarifa_dict.values())
# retorna os itens dentro de taxi
print(tarifa_dict['taxi'].items())
# deleta um item do dict
del tarifa_dict['onibus']
print(tarifa_dict)

# SET
fruits = {'apple', 'cherry', 'pineapple'}
fruits.add('lemon')
fruits.add('avocado')
print(fruits)

fruits.remove('apple')
print(fruits)

# faz a uniao de dois conjuntos, nao repetindo valores que existem em ambos
# print(conjunto1 | conjunto2)
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
uniao = conjunto1.union(conjunto2)
print(uniao)

# retorna os valores presentes em ambos conjuntos
interseccao = conjunto1.intersection(conjunto2)
print(interseccao)

# retorna os valores que estao presentes em conjunto1, mas que nao estao presentes em conjunto2
diferenca = conjunto1.difference(conjunto2)
print(diferenca)

# retorna os valores que estao presentes em conjunto2, mas que nao estao presentes em conjunto1
diferenca = conjunto2.difference(conjunto1)
print(diferenca)

# verifica se o conjunto eh subconjunto de conjunto1
subconjunto = {1,2}
resultado = subconjunto.issubset(conjunto1)
print(resultado)

diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print(diff_simetrica)
