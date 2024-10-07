#Nome: Lucas Kenji Kikuchi - RM554424
#Data 25/09/2024
#Luiz Wanderley Tavares
#Computational Thinking Using Python
import json
import re

# nome do arquivo: pessoas.json

regexEmail = r"^(?=[^@]*@[^@]*$)(?=.*\.).+$"

# Função para escrever no arquivo JSON com tratamento de erro
def escrever_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

# Função para ler o arquivo JSON com tratamento de erro
def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o arquivo '{nome_arquivo}'. O arquivo pode estar corrompido.")
        return []

# Função para adicionar um novo usuário
def adicionar_usuario(nome_arquivo, novo_usuario):
    try:
        dados = ler_json(nome_arquivo)
        dados.append(novo_usuario)
        escrever_json(dados, nome_arquivo)
        print(f"Usuário {novo_usuario['nome']} adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar o usuário: {e}")

# Função para excluir um usuário
def excluir_usuario(nome_arquivo, id_usuario):
    try:
        dados = ler_json(nome_arquivo)
        dados_atualizados = [usuario for usuario in dados if usuario['id'] != id_usuario]
        if len(dados) == len(dados_atualizados):
            print(f"Nenhum usuário encontrado com o ID {id_usuario}.")
        else:
            escrever_json(dados_atualizados, nome_arquivo)
            print(f"Usuário com ID {id_usuario} removido com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir o usuário: {e}")

# pré-cadastro inicial
pessoas = [
    {
        "id": 1,
        "nome": "Ana Silva",
        "email": "ana.silva@email.com",
        "cidade": "São Paulo",
        "estado": "SP"
    },
    {
        "id": 2,
        "nome": "João Pereira",
        "email": "joao.pereira@email.com",
        "cidade": "Rio de Janeiro",
        "estado": "RJ"
    },
    {
        "id": 3,
        "nome": "Maria Oliveira",
        "email": "maria.oliveira@email.com",
        "cidade": "Belo Horizonte",
        "estado": "MG"
    }
]
escrever_json(pessoas, 'pessoas.json')

siglas_estados = (
    "AC", "AL", "AP", "AM", "BA",
    "CE", "DF", "ES", "GO", "MA",
    "MT", "MS", "MG", "PA", "PB",
    "PR", "PE", "PI", "RJ", "RN",
    "RS", "RO", "RR", "SC", "SP",
    "SE", "TO")

def criar_usuario():
    print("Iniciando cadastro do usuário...\n")
    usuario_novo = {}
    # cadastro id
    while True:
        try:
            id = int(input("Qual o ID do usuário?.....: ")) 
            dados = ler_json('pessoas.json')
            for usuario in dados:
                if usuario['id'] == id:
                    raise Exception("ID já cadastrado.")             
        except Exception as e:
            print(f"Ocorreu um erro ao cadastrar ID: {e}")
        else:
            print("ID registrado com sucesso.")
            usuario_novo['id'] = id
            break
    # cadastro nome
    while True:
        try:
            nome = input("Digite o nome..................................: ")        
        except Exception as e:
            print(f"Ocorreu um erro ao cadastrar Nome: {e}")  
        else:
            usuario_novo['nome'] = nome
            print('Nome registrado com sucesso.')
            break
    # cadastro email
    while True:
        try:
            email = input("Digite o email.................................: ")
            verificar_email(email)
        except ValueError as e:
            print(f"Ocorreu um erro ao cadastrar e-mail: {e}") 
        else:
            usuario_novo['email'] = email
            print('Email registrado com sucesso.')
            break
    while True:
        try:
            cidade = input("Digite a cidade..................................: ")        
        except Exception as e:
            print(f"Ocorreu um erro ao cadastrar cidade: {e}")  
        else:
            usuario_novo['cidade'] = cidade
            print('Cidade registrada com sucesso.')
            break
    while True:
        try:
            estado = input("Digite o estado..................................: ")
            verificar_estado(estado)      
        except ValueError as e:
            print(f"Ocorreu um erro ao cadastrar estado: {e}")  
        else:
            usuario_novo['estado'] = estado
            print('Estado registrado com sucesso.')
            break
    adicionar_usuario('pessoas.json', usuario_novo)

def verificar_estado(estado_digitado):
    if estado_digitado in siglas_estados:
        return True
    else: 
        raise ValueError("Estado inválido.")

def verificar_email(email_digitado):
    if re.match(regexEmail, email_digitado) is None:
        raise ValueError("E-mail inválido.")


def visualizar_usuario(valor):
    try:
        usuario_atual = {}
        dados = ler_json('pessoas.json')
        if valor.isdigit():
            valor = int(valor)
        for usuario in dados:
            if usuario['nome'] == valor or usuario['estado'] == valor:
                usuario_atual = usuario
                break
            elif usuario['id'] == valor: 
                usuario_atual = usuario
                break
        if usuario_atual == {}:
            raise Exception("Usuário não encontrado.")

        else:
            print("\n==============[ INFORMAÇÕES DO USUÁRIO ]==============\n") 
            print(f"ID.........: {usuario_atual['id']}") 
            print(f"Nome.......: {usuario_atual['nome']}") 
            print(f"Email......: {usuario_atual['email']}") 
            print(f"Cidade.....: {usuario_atual['cidade']}") 
            print(f"Estado.......: {usuario_atual['estado']}\n") 
            input("Pressione ENTER para voltar ao menu: ")
    except Exception as e:
        print(f"Erro ao visualizar usuário: {e}")

def atualizar_usuario(nome_arquivo, id):
    try:
            existe = False
            usuario_atualizado = {}
            dados = ler_json(nome_arquivo)
            for usuario in dados:
                if usuario['id'] == id:
                    usuario_atualizado = usuario
                    existe = True  
            if existe == False:
                raise ValueError("ID não existe.")
    except ValueError as e:
        print(e)
    else:
        while True:
            print("\n==============[ ATUALIZAÇÃO DOS DADOS DO USUÁRIO ]==============\n")
            print("1 - Atualizar Nome")
            print("2 - Atualizar Email")
            print("3 - Atualizar Cidade")
            print("4 - Atualizar Estado")
            print("0 - Sair")
            op_atualizar = input("\nSelecione uma opção: ")
            if not op_atualizar.isdigit() or int(op_atualizar) > 4 or int(op_atualizar) < 0:
                print("\nSelecione uma opção válida.")
                continue
            op_atualizar = int(op_atualizar)
            if op_atualizar == 0:
                break
            match op_atualizar:
                case 1:
                    while True:
                        try:
                            nome = input("Digite o nome..................................: ")        
                        except Exception as e:
                            print(f"Ocorreu um erro ao atualizar Nome: {e}")  
                        else:
                            usuario_atualizado['nome'] = nome
                            escrever_json(dados, 'pessoas.json')
                            print('Nome atualizado com sucesso.')
                            break
                case 2:
                   while True:
                        try:
                            email = input("Digite o email.................................: ")
                            verificar_email(email)
                        except ValueError as e:
                            print(f"Ocorreu um erro ao atualizar e-mail: {e}") 
                        else:
                            usuario_atualizado['email'] = email
                            escrever_json(dados, 'pessoas.json')
                            print('Email atualizado com sucesso.')
                            break
                case 3:
                    while True:
                        try:
                            cidade = input("Digite a cidade..................................: ")        
                        except Exception as e:
                            print(f"Ocorreu um erro ao atualizar cidade: {e}")  
                        else:
                            usuario_atualizado['cidade'] = cidade
                            escrever_json(dados, 'pessoas.json')
                            print('Cidade atualizada com sucesso.')
                            break
                case 4:
                     while True:
                        try:
                            estado = input("Digite o estado..................................: ")
                            verificar_estado(estado)      
                        except ValueError as e:
                            print(f"Ocorreu um erro ao atualizar estado: {e}")  
                        else:
                            usuario_atualizado['estado'] = estado
                            escrever_json(dados, 'pessoas.json')
                            print('Estado atualizado com sucesso.')
                            break

def main():
    while True:
        print("\n==============[ MENU DO USUÁRIO ]==============\n")
        print("1  - Criar usuário")
        print("2  - Visualizar usuário")
        print("3  - Atualizar usuário")
        print("4  - Deletar usuário")
        print("0  - Sair\n")
        option = input("Opção: ")
        if not option.isdigit() or (int(option) > 4 or int(option) < 0):
            print("\nSelecione uma opção válida.")
            continue
        option = int(option)
        if option == 0:
            print("\nSolicitação encerrada.\n")
            break
        elif option == 1:
            criar_usuario()
        elif option == 2:
            valor = input("Digite um ID, Nome ou Estado para visualizar usuário: ")
            visualizar_usuario(valor)      
        elif option == 3:
            id = input("Digite o ID do usuário que deseja atualizar: ")
            if not id.isdigit() or (int(id) < 0):
                print("\nDigite um id válido.")
            else:
                id = int(id)
                atualizar_usuario('pessoas.json', id)
        elif option == 4:
            valor = input("Digite o ID do usuário que deseja remover: ")
            if not valor.isdigit() or (int(valor) < 0):
                print("\nDigite um valor válido.")
            else:
                valor = int(valor)
                excluir_usuario('pessoas.json', valor)

if __name__ == '__main__':
    main()


