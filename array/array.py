# soma
print("* SUM *")
x = [1, 2, 3, 4, 5]
print(f"Soma: {sum(x)}")

# largura
print("* LEN *")
x = [1, 2, 3, 4, 5]
print(f"Largura: {len(x)}")

#remover primeira ocorrencia de um elemento
print("* REMOVE *")
x = [1, 2, 3, 4, 5]
x.remove(1)
print(x)

#remove e retorna elemento com indice especificado. Se o indice nao for especificado, remove o ultimo elemento da lista. 
print("* POP *")
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
print(f"Elemento removido: {x.pop(1)}")
print(f"Elemento removido: {y.pop()}")

#conta quantas vezes um elemento aparece em uma lista
print("* COUNT *")
x = [1, 2, 3, 4, 5, 1, 4, 5, 7, 1]
print(f"Elemento se repete {x.count(1)} vezes")

#encontra o indice da primeira ocorrencia de um elemento
print("* INDEX *")
x = [2, 3, 4, 2, 3, 5, 4, 2]
print(f"Primeira ocorrencia ocorre no indice {x.index(2)}")
print(f"Primeira ocorrencia apos o indice 1: {x.index(2, 1)}")

#insere um elemento em um indice especifico.
print("* INSERT *")
x = [1, 2, 4, 5, 6]
x.insert(2, 3)
print(x)

#organiza em ordem crescente ou decrescente
print("* SORT *")
x = [9, 3, 4, 2, 1, 7, 5, 8, 6]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

#adiciona item ao final da lista
print("* APPEND *")
x = [1, 2, 3]
x.append(4)
print(x)


