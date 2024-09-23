# vale mais a pena carregar o json em memoria, zerar o arquivo, e escrever novamente o arquivo atualizado, ao invés de fazer insert.
# criar uma tabela sem indices é melhor do que inserir registros em uma tabela com indices já estabelecidos.

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

#1. Criar um Arquivo JSON Simples
#• Objetivo: Criar um arquivo JSON que contenha uma lista de objetos (ex: usuários) com informações como nome, idade, e-mail, etc.
#• Exemplo de Saída: usuarios.json 

import json

# Lista de usuários
usuarios = [
    {"id": 1, "nome": "João Silva", "idade": 30, "email": "joao.silva@example.com"},
    {"id": 2, "nome": "Maria Souza", "idade": 25, "email": "maria.souza@example.com"},
    {"id": 3, "nome": "Pedro Oliveira", "idade": 40, "email": "pedro.oliveira@example.com"},
    {"id": 4, "nome": "Ana Costa", "idade": 22, "email": "ana.costa@example.com"},
    {"id": 5, "nome": "Carlos Pereira", "idade": 35, "email": "carlos.pereira@example.com"},
    {"id": 6, "nome": "Fernanda Santos", "idade": 28, "email": "fernanda.santos@example.com"},
    {"id": 7, "nome": "Lucas Andrade", "idade": 33, "email": "lucas.andrade@example.com"},
    {"id": 8, "nome": "Juliana Carvalho", "idade": 29, "email": "juliana.carvalho@example.com"},
    {"id": 9, "nome": "Ricardo Lima", "idade": 45, "email": "ricardo.lima@example.com"},
    {"id": 10, "nome": "Bianca Mendes", "idade": 27, "email": "bianca.mendes@example.com"}
]

escrever_json(usuarios, "usuarios.json")

#2. Ler e Exibir Dados de um Arquivo JSON
#• Objetivo: Ler um arquivo JSON e exibir o conteúdo no console.
#• Exemplo: Carregar e mostrar os dados de um arquivo usuarios.json.

arquivo_json = ler_json("usuarios.json")
print(f"Dados do JSON: {arquivo_json}")

#3. Adicionar um Novo Objeto ao Arquivo JSON
#• Objetivo: Adicionar um novo usuário a uma lista de usuários existente em um arquivo JSON, sem sobrescrever os dados existentes.
#• Exemplo: Adicionar um novo usuário ao arquivo usuarios.json.

novo_usuario = {"id": 11, "nome": "Marcos dos Santos", "idade": 19, "email": "marcos.santos@gmail.com"}
adicionar_usuario("usuarios.json", novo_usuario)

#4. Atualizar um Campo Específico em um Objeto JSON
#• Objetivo: Atualizar o e-mail de um usuário específico com base no seu nome ou ID no arquivo JSON.
#• Exemplo: Alterar o e-mail de um usuário chamado “João” em usuarios.json.

def atualizar_email(nome_arquivo, id_usuario, novo_email):
    try:
        dados = ler_json(nome_arquivo)
        for usuario in dados:
            if usuario['id'] == id_usuario:
                usuario['email'] = novo_email
                print(f"Email do usuário com ID {id_usuario} atualizado com sucesso.")
        escrever_json(dados, nome_arquivo)
    except Exception as e:
        print(f"Erro ao atualizar o usuário: {e}")

atualizar_email("usuarios.json", 1, "joao123@gmail.com")

#5. Excluir um Objeto Específico do Arquivo JSON
#• Objetivo: Remover um usuário específico do arquivo JSON com base em um identificador (por exemplo, um ID).
#• Exemplo: Excluir o usuário com id: 3 de usuarios.json.

excluir_usuario("usuarios.json", 3)

#6. Buscar um Objeto Específico no JSON
#• Objetivo: Ler o arquivo JSON e buscar um usuário específico pelo nome ou ID.
#• Exemplo: Encontrar o usuário com o nome “Maria” em usuarios.json.

def buscar_usuario(nome_arquivo, id_usuario):
    try:
        dados = ler_json(nome_arquivo)
        for usuario in dados:
            if usuario["id"] == id_usuario:
                return usuario
    except Exception as e:
        print(f"Erro ao buscar o usuário: {e}")

usuario_buscado = buscar_usuario('usuarios.json', 2)
print(f"Usuário buscado: {usuario_buscado}")

#7. Filtrar Dados com Base em Condições Específicas
#• Objetivo: Filtrar e exibir os usuários que têm idade superior a 30 no arquivo JSON.
#• Exemplo: Mostrar todos os usuários com idade acima de 30 em usuarios.json.

def filtrar_usuarios_maior_30(nome_arquivo):
    try:
        dados = ler_json(nome_arquivo)
        dados_filtrados = [usuario for usuario in dados if usuario['idade'] > 30]
        if len(dados_filtrados) == 0:
            print(f"Nenhum usuário encontrado com a idade maior que 30.")
        else:
            return dados_filtrados
    except Exception as e:
        print(f"Erro ao filtrar usuários: {e}")

dados_filtrados = filtrar_usuarios_maior_30('usuarios.json')
print(f"Usuários com idade maior que 30 anos: {dados_filtrados}")

#8. Contar o Número de Objetos em um Arquivo JSON
#• Objetivo: Contar quantos usuários estão cadastrados no arquivo JSON.
#• Exemplo: Exibir o número total de usuários em usuarios.json.

dados = ler_json("usuarios.json")
print(f'Quantidade de Usuários cadastrados: {len(dados)} usuários.')

#9. Ordenar Objetos no Arquivo JSON
#• Objetivo: Ordenar os usuários por idade ou nome e salvar o resultado no arquivo JSON.
#• Exemplo: Ordenar os usuários por idade em ordem crescente.

def ordenar_por_idade(nome_arquivo):
    try:
        dados = ler_json(nome_arquivo)
        dados_ordenados = sorted(dados, key=lambda d: d['idade'])
        escrever_json(dados_ordenados, nome_arquivo)
    except Exception as e:
        print(f"Erro ao ordenar usuários: {e}")


ordenar_por_idade('usuarios.json')
dados = ler_json("usuarios.json")
print(f"Dados ordenados: {dados}")

#10. Mesclar Dois Arquivos JSON
#• Objetivo: Ler dois arquivos JSON diferentes contendo listas de objetos e mesclar os dados em um único arquivo JSON.
#• Exemplo: Mesclar usuarios.json com clientes.json e salvar o resultado em resultado.json.

clientes = [
    {"nome": "Leonardo Farias", "idade": 37, "email": "leonardo.farias@empresa1.com", "empresa": "Empresa Alfa"},
    {"nome": "Patrícia Nunes", "idade": 29, "email": "patricia.nunes@empresa2.com", "empresa": "Empresa Beta"},
    {"nome": "Eduardo Martins", "idade": 43, "email": "eduardo.martins@empresa3.com", "empresa": "Empresa Gama"},
    {"nome": "Renata Lima", "idade": 26, "email": "renata.lima@empresa4.com", "empresa": "Empresa Delta"},
    {"nome": "Thiago Rodrigues", "idade": 34, "email": "thiago.rodrigues@empresa5.com", "empresa": "Empresa Épsilon"}
]

escrever_json(clientes, 'clientes.json')
dados_usuarios = ler_json("usuarios.json")
dados_clientes = ler_json("clientes.json")

dados_usuarios.extend(dados_clientes)
resultado = dados_usuarios

escrever_json(resultado, 'resultado.json')



