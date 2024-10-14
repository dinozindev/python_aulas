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
    cursor.execute("SELECT * FROM IRIS")  # Consulta SQL para buscar produtos
    rows = cursor.fetchall()  # Busca todas as linhas
    cursor.close()
    connection.close()
    # ID, SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH , CLASS_ID, CLASS
    produtos = [{"id": row[0], "nome": row[6]} for row in rows]
    return jsonify(produtos)
 
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
        produto = {"id": row[0], "nome": row[6]}
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado"}), 404
 
# Rota para adicionar um novo produto (POST)
@app.route('/produtos', methods=['POST'])
def add_produto():
    novo_produto = request.json
    nome = novo_produto.get('nome')
    preco = novo_produto.get('preco')
    connection = get_db_connection()
    cursor = connection.cursor()
    # Consulta SQL para inserir um novo produto
    cursor.execute("""
        INSERT INTO produtos (nome, preco)
        VALUES (:nome, :preco)
    """, [nome, preco])
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    return jsonify({"message": "Produto adicionado"}), 201
 
# Rota para atualizar um produto existente (PUT)
#@app.route('/produtos/<int:id>', methods=['PUT'])
#def update_produto(id):
#    produto_atualizado = request.json
#    nome = produto_atualizado.get('nome')
#    preco = produto_atualizado.get('preco')
#    connection = get_db_connection()
#    cursor = connection.cursor()
    # Consulta SQL para atualizar um produto
#    cursor.execute("""
#        UPDATE produtos
#        SET nome = :nome, preco = :preco
#        WHERE id = :id
#    """, [nome, preco, id])
#    connection.commit()  # Confirma a transação
#    cursor.close()
#    connection.close()
#    return jsonify({"message": "Produto atualizado"}), 200
 
# Rota para deletar um produto (DELETE)
#@app.route('/produtos/<int:id>', methods=['DELETE'])
#def delete_produto(id):
#    connection = get_db_connection()
#    cursor = connection.cursor()
    # Consulta SQL para deletar um produto por ID
#    cursor.execute("DELETE FROM produtos WHERE id = :id", [id])
#    connection.commit()  # Confirma a transação
#    cursor.close()
#    connection.close()
#    return jsonify({"message": "Produto deletado"}), 200
 
if __name__ == '__main__':
    app.run(debug=False)