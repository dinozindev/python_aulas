# obtem o numero de linhas
with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'O arquivo contém {len(linhas)} linhas.')

# obtem o conteudo do arquivo
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Novo conteúdo")

with open('arquivo.txt', 'a') as arquivo:
    arquivo.write("Adicionando conteúdo")

with open('arquivo.txt', 'x') as arquivo:
    arquivo.write("Criando novo arquivo")

# binarios
with open('imagem.png', 'rb') as arquivo:
    dados = arquivo.read()

with open('imagem.png', 'wb') as arquivo:
    arquivo.write(novos_dados_binarios)

with open('imagem.png', 'ab') as arquivo:
    arquivo.write(mais_dados_binarios)

# atualizacao
with open('arquivo.txt', 'r+') as arquivo:
    conteudo = arquivo.read()
    arquivo.write("Novo conteúdo no final")

with open('arquivo.txt', 'w+') as arquivo:
    arquivo.write("Novo conteúdo")
    arquivo.seek(0)
    conteudo = arquivo.read()

with open('arquivo.txt', 'a+') as arquivo:
    arquivo.write("Conteúdo adicional")
    arquivo.seek(0)
    conteudo = arquivo.read()
