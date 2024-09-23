#!/usr/bin/env python
# coding: utf-8

# In[1]:

import json

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

# Função para escrever no arquivo JSON com tratamento de erro
def escrever_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

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

# Função principal
def main():
    nome_arquivo = 'usuarios.json'
    
    # Exemplo de usuários
    usuarios = [
        {"id": 1, "nome": "João", "email": "joao@email.com", "idade": 25},
        {"id": 2, "nome": "Maria", "email": "maria@email.com", "idade": 32}
    ]

    # Criar arquivo com dados iniciais
    escrever_json(usuarios, nome_arquivo)

    # Adicionar um novo usuário
    adicionar_usuario(nome_arquivo, {"id": 3, "nome": "Carlos", "email": "carlos@email.com", "idade": 40})

    # Excluir um usuário pelo ID
    excluir_usuario(nome_arquivo, 2)

if __name__ == "__main__":
    main()


# In[ ]:




