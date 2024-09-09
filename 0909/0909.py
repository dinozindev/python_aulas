# obtem o numero de linhas
with open('exemplo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(f'O arquivo contém {len(linhas)} linhas.')

# obtem o conteudo do arquivo
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)