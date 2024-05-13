a = [1,2,3,4,5,6,7,8,9,6]

# insere elemento no final da lista
a.append(10)
print(a)

# retorna o indice de um elemento (ex: 5)
print(f"indice de 5: {a.index(5)}")

# retorna a qtnd que um elemento aparece em uma lista.
x = a.count(6)
print(f"vezes que 6 aparece na lista: {x} vezes")

# remove um elemento com base no seu indice
a.pop(9)
print(a)