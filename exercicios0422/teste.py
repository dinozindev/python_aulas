# Exercício 4 - Contando caracteres 
dicionario = {} 
frase = input("Escreva uma frase: ")
# remove os espaços em branco da frase
fraseSemEspacos = frase.replace(' ', '')
# transforma a string em uma lista
caracteresFrase = list(fraseSemEspacos)

# para cada caractere na lista, se ela já estiver na lista, adiciona um em sua contagem. Caso contrário, adiciona ele na lista.
for caractere in caracteresFrase:
    if caractere in dicionario:
        dicionario[caractere] += 1
    else:
        dicionario[caractere] = 1

print(dicionario)

