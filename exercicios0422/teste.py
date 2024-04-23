# Exercício 4 - Contando caracteres 
dicionario = {} 
frase = input("Escreva uma frase: ")
fraseSemEspacos = frase.replace(' ', '')
caracteresFrase = list(fraseSemEspacos)
print(caracteresFrase.index('o'))

for i in range(len(caracteresFrase)):
    dicionario[caracteresFrase[i]] = 1

print(dicionario)
