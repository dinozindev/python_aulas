#!/usr/bin/env python
# coding: utf-8

# In[1]:


import oracledb

# Estabelecendo conexão
connection = oracledb.connect(
    user="",
    password="",
    dsn="oracle.fiap.com.br:1521/orcl" 
)

print("Conexão estabelecida com sucesso!")


# In[2]:


cursor = connection.cursor()

# Executando a consulta para listar as tabelas do esquema atual
cursor.execute("SELECT table_name FROM user_tables")

# Buscando e imprimindo todas as tabelas
tables = cursor.fetchone()


# In[3]:


tables


# In[ ]:


# ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS


# In[ ]:


# criar arquivo oracle_conn.json  com estas informações

[{
    "user": "",
    "password": "",
    "dsn": "oracle.fiap.com.br:1521/orcl" 
}]


# In[ ]:


DATA_FILE = "oracle_conn.json"
file = open(DATA_FILE, 'r')
xfile = json.load(file)

connection = oracledb.connect(
    user=xfile[0]["user"],
    password=xfile[0]["password"],
    dsn=xfile[0]["dsn"] 
)


# In[ ]:





# In[ ]:





# In[4]:


cursor.execute("select * from IRIS")
iris = cursor.fetchall()
iris


# In[ ]:





# In[ ]:





# In[22]:


from flask import Flask, jsonify, request
import oracledb

app = Flask(__name__)

# Função para conectar ao banco de dados Oracle
def get_db_connection():
    connection = oracledb.connect(
        user="PF1803",
        password="fiap24",
        dsn="oracle.fiap.com.br:1521/orcl" 
    )
    return connection

# Rota para retornar todos os produtos (GET)
@app.route('/produtos', methods=['GET'])
def get_produtos():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Captura os parâmetros da URL (ID, SEPAL_LENGTH, etc.)
    id = request.args.get('ID')
    class_id = request.args.get('CLASS_ID')
    
    print(id, class_id)
    
    # Montar a consulta SQL dinamicamente de acordo com os parâmetros fornecidos
    query = "SELECT * FROM IRIS WHERE 1=1"
    params = []
    
    if id:
        query += " AND ID = :id"
        params.append(id)
    if class_id:
        query += " AND CLASS_ID = :class_id"
        params.append(class_id)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        produto = [{"id": row[0], "SEPAL_LENGTH": row[1],"SEPAL_WIDTH":  row[2],"PETAL_LENGTH":  row[3],"PETAL_WIDTH":  row[4],"CLASS_ID":  row[5], "CLASS": row[6]} for row in rows] 
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado"}), 404
    
# Rota para buscar um produto específico por ID (GET)
@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um produto por ID
    cursor.execute("SELECT * FROM IRIS WHERE ID = :id", [id])
    row = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if row:
        produto = {"id": row[0], "SEPAL_LENGTH": row[1],"SEPAL_WIDTH":  row[2],"PETAL_LENGTH":  row[3],"PETAL_WIDTH":  row[4],"CLASS_ID":  row[5], "CLASS": row[6]}
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado"}), 404

# Rota para adicionar um novo produto (POST)
@app.route('/produtos', methods=['POST'])
def add_produto():
    novo_produto = request.json
    #print(novo_produto)
    # ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS
    SEPAL_LENGTH = novo_produto.get('SEPAL_LENGTH')
    SEPAL_WIDTH = novo_produto.get('SEPAL_WIDTH')
    PETAL_LENGTH = novo_produto.get('PETAL_LENGTH')
    PETAL_WIDTH = novo_produto.get('PETAL_WIDTH')
    CLASS_ID = novo_produto.get('CLASS_ID')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT MAX(ID) FROM IRIS")
    row = cursor.fetchone()
    
    ID = row[0] + 1
    
    seleciona = "SELECT DISTINCT(CLASS) FROM IRIS WHERE CLASS_ID = " + str(CLASS_ID)
    cursor.execute(seleciona)
    row = cursor.fetchone()
    
    CLASS = row[0]
    
    # print(ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS)
    
    # Consulta SQL para inserir um novo produto
    cursor.execute("""
        INSERT INTO IRIS (ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS)
        VALUES (:ID, :SEPAL_LENGTH, :SEPAL_WIDTH, :PETAL_LENGTH, :PETAL_WIDTH , :CLASS_ID, :CLASS)
    """, [ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Produto adicionado"}), 201

# Rota para atualizar um produto existente (PUT)
@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    produto_atualizado = request.json
    SEPAL_LENGTH = novo_produto.get('SEPAL_LENGTH')
    SEPAL_WIDTH = novo_produto.get('SEPAL_WIDTH')
    PETAL_LENGTH = novo_produto.get('PETAL_LENGTH')
    PETAL_WIDTH = novo_produto.get('PETAL_WIDTH')
    CLASS_ID = novo_produto.get('CLASS_ID')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para atualizar um produto
    cursor.execute("""
        UPDATE IRIS
        SET nome = :nome, preco = :preco
        WHERE id = :id
    """, [nome, preco, id])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Produto atualizado"}), 200

# Rota para deletar um produto (DELETE)
@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para deletar um produto por ID
    cursor.execute("DELETE FROM IRIS WHERE id = :id", [id])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Produto deletado"}), 200

if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:





# In[ ]:


import requests

# GET request
response = requests.get('http://127.0.0.1:5000/produtos')
print(response.json())


# In[ ]:


busca = {"CLASS_ID": 0}
response = requests.get('http://127.0.0.1:5000/produtos', params=busca)
for i in response.json():
    print(i)


# In[ ]:


# POST request para adicionar novo produto

# ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS

novo_produto = {"SEPAL_LENGTH": 8,"SEPAL_WIDTH": 8,"PETAL_LENGTH": 8,"PETAL_WIDTH": 8,"CLASS_ID": 2}
response = requests.post('http://127.0.0.1:5000/produtos', json=novo_produto)
print(response.json())


# In[ ]:


# GET request produto
response = requests.delete('http://127.0.0.1:5000/produtos/153')
print(response.json())


# In[ ]:


# COMO URL


# In[ ]:


http://127.0.0.1:5000/produtos # lista total


# In[ ]:


http://127.0.0.1:5000/produtos/3 #id


# In[ ]:


http://127.0.0.1:5000/produtos?CLASS_ID=1 # passando parametros


# In[ ]:




