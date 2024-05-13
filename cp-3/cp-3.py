import re

filmes = [{'titulo': "Carros", 'nome': "Carros", 'ano': 2006, 'sinopse': "Carros muito loucos em varios lugares loucos"}, {'titulo': "Avengers", 'nome': "Avengers", 'ano': 2010, 'sinopse': "Heróis muito loucos"}]
usuarios = [{'nome': 'Lucas', 'idade': 19, 'telefone': '11 98923-3948', 'email': 'lucas@gmail.com', 'senha': 'Lucas0013'}]
regexTel = r'\d{2} 9\d{4}-\d{4}'
regexEmail = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# função para cadastro e remoção de filmes
def cadastro_filmes():
    while True:
        print("\n==============[ MENU FILMES ]==============\n")
        print("0 - Voltar (voltar para o Menu Inicial)")
        print("1 - Cadastrar Filmes")
        print("2 - Remover Filmes")
        op_filmes = input("\nSelecione uma opção: ")
        if not op_filmes.isdigit() or (int(op_filmes) > 2 or int(op_filmes) < 0):
            print("\nSelecione uma opção válida.")
            continue
        op_filmes = int(op_filmes)
        if op_filmes == 0:
            print("Retornando ao menu inicial...")
            break
        elif op_filmes == 1:
            titulo = input("\nQual o título do filme?...........: ")
            nome = input("Qual o nome do filme?.............: ")
            while True:
                ano = input("Qual o ano de lançamento do filme?: ")
                if not ano.isdigit() or int(ano) > 2024 or int(ano) < 1895:
                    print("Insira um ano válido.")
                    continue
                else:
                    ano = int(ano)
                    break
            sinopse = input("Qual a sinopse do filme?..........: ")
            filmes.append({'titulo': titulo, 'nome': nome, 'ano': ano, 'sinopse': sinopse})
            print("\nFilme cadastrado com sucesso!")
        elif op_filmes == 2:
            while True: 
                if filmes == []:
                    print("\nNenhum filme foi cadastrado.")
                    break
                print("\n=============[ REMOVER FILME ]=============\n")
                for i in range(len(filmes)):
                    print(f"{i} - {filmes[i]['titulo']}")
                op_remove = input("\nQual filme deseja remover?: ")
                if not op_remove.isdigit() or int(op_remove) > (len(filmes) - 1) or int(op_remove) < 0:
                    print("\nSelecione uma opção válida.")
                    continue
                op_remove = int(op_remove)
                filmes.pop(op_remove)
                print("\nFilme removido com sucesso.")
                break

# função para cadastro e remoção de usuários
def cadastro_usuarios():
    while True:
        print("\n==============[ MENU USUÁRIOS ]==============\n")
        print("0 - Voltar (voltar para o Menu Inicial)")
        print("1 - Cadastrar Usuários")
        print("2 - Remover Usuários")
        op_usuarios = input("\nSelecione uma opção: ")
        if not op_usuarios.isdigit() or (int(op_usuarios) > 2 or int(op_usuarios) < 0):
            print("\nSelecione uma opção válida.")
            continue
        op_usuarios = int(op_usuarios)
        if op_usuarios == 0:
            print("Retornando ao menu inicial...")
            break
        elif op_usuarios == 1:
            nome_usuario = input("\nQual o seu nome?...........: ")
            while True:
                idade = input("Qual a sua idade?.............: ")
                if not idade.isdigit() or int(idade) < 18:
                    print("Insira uma idade válida.")
                    continue
                else:
                    idade = int(idade)
                    break
            while True:
                tel = input("Qual o seu telefone? (ex: DD 9XXXX-XXXX): ")
                if re.match(regexTel, tel) is None:
                    print("Insira um telefone válido.")
                    continue
                else:
                    break
            while True:
                email = input("Qual o seu e-mail?: ")
                if re.match(regexEmail, email) is None:
                    print("Insira um e-mail válido.")
                    continue
                else:
                    email.lower()
                    break
            senha = input("Qual a senha a ser utilizada no Login?: ")
            usuarios.append({'nome': nome_usuario, 'idade': idade, 'telefone': tel, 'email': email, 'senha': senha})
            print("\nUsuário cadastrado com sucesso!")
        elif op_usuarios == 2:
            while True: 
                if usuarios == []:
                    print("\nNenhum usuário foi cadastrado.")
                    break
                print("\n=============[ REMOVER USUÁRIO ]=============\n")
                for i in range(len(usuarios)):
                    print(f"{i} - {usuarios[i]['nome']} - {usuarios[i]['email']}")
                op_remove = input("\nQual usuário deseja remover?: ")
                if not op_remove.isdigit() or int(op_remove) > (len(usuarios) - 1) or int(op_remove) < 0:
                    print("\nSelecione uma opção válida.")
                    continue
                op_remove = int(op_remove)
                usuarios.pop(op_remove)
                print("\nUsuário removido com sucesso.")
                break

# função para validar e logar o usuário.
def login_usuario(): 
    while True:
        email_login = input("\nInsira seu e-mail: ").lower()
        senha_login = input("Insira sua senha.: ")
        if usuarios == []:
            print("\nNenhum usuário cadastrado no sistema.")
            break
        for i in range(len(usuarios)):
            confirm = False
            if usuarios[i]['email'] == email_login or usuarios[i]['senha'] == senha_login:
                confirm = True
                break
        if confirm == False:
            print("\nUsuário ou senha inválido.")
            continue
        menu_filmes()
        break

# função para abrir o menu com a lista de filmes.
def menu_filmes():
    while True:
        print("\n=============[ LISTA FILMES ]=============\n")
        print("0 - Sair do sistema (voltar ao Menu Inicial)")
        for j in range(len(filmes)):
            print(f"{j+1} - {filmes[j]['nome']} - {filmes[j]['ano']}")
        op_filme = input("\nSelecione um filme para assistir: ")
        if not op_filme.isdigit() or int(op_filme) > (len(filmes)) or int(op_filme) < 0:
            print("\nSelecione uma opção válida.")
            continue
        op_filme = int(op_filme)
        if op_filme == 0:
            print("\nRetornando ao menu inicial...")
            break
        else:
            while True:
                print(f"\nSinopse: {filmes[op_filme-1]['sinopse']}")
                print("\n0 - Assistir")
                print("1 - Voltar")
                op_filme_escolhido = input("\nEscolha uma das opções: ")
                if op_filme_escolhido != '0' and op_filme_escolhido != '1':
                    print("\nEscolha uma opção válida.")
                    continue
                elif op_filme_escolhido == '0':
                    print("\nBom Filme")
                    break
                elif op_filme_escolhido == '1':
                    break 


# menu principal
while True:
    print("\n==============[ MENU INICIAL ]==============\n")
    print("0 - Saída (sai do sistema)")
    print("1 - Cadastro de Filmes")
    print("2 - Cadastro de Usuários")
    print("3 - Login do Usuário\n")
    op = input("Selecione uma opção: ")
    if not op.isdigit() or (int(op) > 3 or int(op) < 0):
        print("\nSelecione uma opção válida.")
        continue
    op = int(op)
    if op == 0:
        print("\nSaindo do menu...")
        break
    elif op == 1:
        cadastro_filmes()
    elif op == 2:
        cadastro_usuarios()
    elif op == 3:
        login_usuario()
