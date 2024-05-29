import re;

usuarioDados = []
regexCpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
regexTel = r'\d{2} 9\d{4}-\d{4}'
regexNome = r"^[A-Za-zÀ-ÿ'\- ]+$"

#lista de especies

# cadastro do usuario
def cadastro_usuario():
    print("Iniciando cadastro do usuário...\n")
    if len(usuarioDados) > 0:
        print("Você já está cadastrado. Irei te redirecionar para o menu...")
        return
    # cadastro nome
    while True:
        nome = input("Digite o seu nome........................: ")
        if re.match(regexNome, nome) is None:
            print("Digite um nome válido.")
            continue
        else:
            usuarioDados.append(nome)
            break 
    # cadastro idade   
    while True:
        idade = input("Digite sua idade.........................: ")
        if not idade.isdigit() or int(idade) < 18 or int(idade) > 90:
            print("Digite uma idade válida.")
            continue
        else:
            usuarioDados.append(idade)
            break
    # cadastro CPF
    while True:
        cpf = input("Digite o seu CPF (ex: xxx.xxx.xxx-xx)....: ")
        if re.match(regexCpf, cpf) is None:
            print("Digite um CPF válido.")
            continue
        else:
            usuarioDados.append(cpf)
            break
    # cadastro endereço
    while True:
        endereco = input("Digite o seu endereço....................: ")
        if re.match(regexNome, endereco) is None:
            print("Digite um endereço válido.")
            continue
        else:
            usuarioDados.append(endereco)
            break
    # cadastro telefone
    while True:
        telefone = input("Digite o seu telefone (ex: xx xxxxx-xxxx): ")
        if re.match(regexTel, telefone) is None:
            print("Digite um número de telefone válido.")
            continue
        else: 
            usuarioDados.append(telefone)
            break
    print("\nUsuário cadastrado com sucesso!")

#remover usuario 
def deletar_usuario():
    while True:
        if not usuarioDados:
            print("\nVocê não está cadastrado ainda.")
            break
        op_delete = input("\nDeseja realmente deletar o seu cadastro? S ou N: ")
        if op_delete.upper() != "S" and op_delete.upper() != "N":
            print("\nDigite uma opção válida.")
            continue
        elif op_delete.upper() == "S":
            usuarioDados.clear()
            print("\nCadastro removido com sucesso.")
            break
        elif op_delete.upper() == "N":
            print("\nO cadastro não foi removido.")
            break

# visualização das informações do usuário (Nome, Idade, CPF, endereço e telefone)
def gerenciar_usuario(usuarioDados):
        print("\nIniciando menu de gerenciamento do usuário...") 
        while True:
            if usuarioDados == []:
                print("\nVocê ainda não se cadastrou.")
                break
            print("\n==============[ GERENCIAMENTO USUÁRIO ]==============\n")
            print("1 - Remover usuário")
            print("2 - Visualizar informações do usuário")
            print("0 - Sair")
            verif_usuario_op = input("\nSelecione uma opção: ")
            if not verif_usuario_op.isdigit() or int(verif_usuario_op) > 2 or int(verif_usuario_op) < 0:
                print("\nSelecione uma opção válida.")
                continue
            verif_usuario_op = int(verif_usuario_op)
            if verif_usuario_op == 0:
                break
            elif verif_usuario_op == 1:
                deletar_usuario()
                break
            elif verif_usuario_op == 2:
                print("\n==============[ INFORMAÇÕES DO USUÁRIO ]==============\n") 
                print(f"Nome....: {usuarioDados[0]}") 
                print(f"Idade...: {usuarioDados[1]}") 
                print(f"CPF.....: {usuarioDados[2]}") 
                print(f"Endereço: {usuarioDados[3]}") 
                print(f"Telefone: {usuarioDados[4]}\n") 
                input("Pressione ENTER para voltar ao menu: ")
                print("Retornando ao menu do usuário...")
                continue

def relatar_pesca_irregular():
   print("\nRelatório de pesca irregular...")
     

while True:
    print("\n==============[ MENU ]==============\n")
    print("1  - Cadastro Usuário")
    print("2  - Gerenciar Usuário")
    print("3  - Relatar pesca irregular")
    print("0  - Sair\n")
    option = input("Opção: ")
    if not option.isdigit() or (int(option) > 10 or int(option) < 0):
        print("\nSelecione uma opção válida.")
        continue
    option = int(option)   
    match option:
        case 0:
            print("\nSolicitação encerrada.\n")
            break
        case 1:
            cadastro_usuario()
        case 2:
            gerenciar_usuario(usuarioDados)
        case 3:
            relatar_pesca_irregular()