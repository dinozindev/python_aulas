#Nome: Lucas Kenji Kikuchi - RM554424
#Data 26/10/2024
#Luiz Wanderley Tavares
#Computational Thinking Using Python

from flask import Flask, jsonify, request
import oracledb
import json

app = Flask(__name__)

# create table FILMES (
#     id_filme NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
#     nome_filme varchar(255) not null,
#     ano_filme number(4) not null,
#     genero_filme varchar(155) not null,
#     ator_principal varchar(155) not null,
#     atriz_principal varchar(155) not null
# )

# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Inception', 2010, 'Ação/Ficção Científica', 'Leonardo DiCaprio', 'Ellen Page');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Titanic', 1997, 'Romance/Drama', 'Leonardo DiCaprio', 'Kate Winslet');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Matrix', 1999, 'Ação/Ficção Científica', 'Keanu Reeves', 'Carrie-Anne Moss');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Devil Wears Prada', 2006, 'Comédia/Drama', 'Meryl Streep', 'Anne Hathaway');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Gladiator', 2000, 'Ação/Drama', 'Russell Crowe', 'Connie Nielsen');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Forrest Gump', 1994, 'Drama', 'Tom Hanks', 'Robin Wright');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Pretty Woman', 1990, 'Romance/Comédia', 'Richard Gere', 'Julia Roberts');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Avatar', 2009, 'Ação/Ficção Científica', 'Sam Worthington', 'Zoe Saldana');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Shawshank Redemption', 1994, 'Drama', 'Tim Robbins', 'Renee Blaine');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Dark Knight', 2008, 'Ação', 'Christian Bale', 'Maggie Gyllenhaal');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('La La Land', 2016, 'Romance/Musical', 'Ryan Gosling', 'Emma Stone');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Godfather', 1972, 'Crime/Drama', 'Marlon Brando', 'Diane Keaton');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Pulp Fiction', 1994, 'Crime/Drama', 'John Travolta', 'Uma Thurman');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Wonder Woman', 2017, 'Ação/Fantasia', 'Chris Pine', 'Gal Gadot');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('A Star is Born', 2018, 'Romance/Drama', 'Bradley Cooper', 'Lady Gaga');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Jurassic Park', 1993, 'Ação/Ficção Científica', 'Sam Neill', 'Laura Dern');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('The Silence of the Lambs', 1991, 'Suspense/Crime', 'Anthony Hopkins', 'Jodie Foster');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Black Panther', 2018, 'Ação/Ficção Científica', 'Chadwick Boseman', 'Lupita Nyong\o');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Braveheart', 1995, 'Ação/Drama', 'Mel Gibson', 'Sophie Marceau');
# INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal) VALUES ('Gone with the Wind', 1939, 'Romance/Drama', 'Clark Gable', 'Vivien Leigh');

# Função para conectar ao banco de dados Oracle
def get_db_connection():
    DATA_FILE = "oracle_conn.json"
    file = open(DATA_FILE, 'r')
    xfile = json.load(file)

    connection = oracledb.connect(
        user=xfile[0]["user"],
        password=xfile[0]["password"],
        dsn=xfile[0]["dsn"] 
    )
    return connection

# Rota para retornar todos os filmes (GET)
@app.route('/filmes', methods=['GET'])
def get_filmes():
    connection = get_db_connection()
    cursor = connection.cursor()

    id = request.args.get('id_filme')
    nome_filme = request.args.get('nome_filme')
    ano_filme = request.args.get('ano_filme')
    genero_filme = request.args.get('genero_filme')
    ator_principal = request.args.get('ator_principal')
    atriz_principal = request.args.get('atriz_principal')
    
    query = "SELECT * FROM FILMES WHERE 1=1"
    params = []
    
    if id:
        query += " AND ID = :id"
        params.append(id)
    if nome_filme:
        query += " AND nome_filme = :nome_filme"
        params.append(nome_filme)
    if ano_filme:
        query += " AND ano_filme = :ano_filme"
        params.append(ano_filme)
    if genero_filme:
        query += " AND genero_filme = :genero_filme"
        params.append(genero_filme)
    if ator_principal:
        query += " AND ator_principal = :ator_principal"
        params.append(ator_principal)
    if atriz_principal:
        query += " AND atriz_principal = :atriz_principal"
        params.append(atriz_principal)

    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_principal":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404
    
# Rota para buscar um filme específico por ID (GET)
@app.route('/filmes/id_filme/<int:id_filme>', methods=['GET'])
def get_filme_id(id_filme):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por ID
    cursor.execute("SELECT * FROM FILMES WHERE id_filme = :id_filme", [id_filme])
    row = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if row:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_principal":  row[4], "atriz_principal": row[5]}] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404
    
# Rota para buscar filmes por Nome (GET)
@app.route('/filmes/nome_filme/<nome_filme>', methods=['GET'])
def get_filme_nome(nome_filme):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por nome
    cursor.execute("SELECT * FROM FILMES WHERE nome_filme = :nome_filme", [nome_filme])
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_filme":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404
    
# Rota para buscar filmes por Gênero (GET)
@app.route('/filmes/genero_filme/<genero_filme>', methods=['GET'])
def get_filme_genero(genero_filme):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por gênero
    cursor.execute("SELECT * FROM FILMES WHERE genero_filme = :genero_filme", [genero_filme])
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_filme":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404
    
# Rota para buscar filmes por Ano (GET)
@app.route('/filmes/ano_filme/<int:ano_filme>', methods=['GET'])
def get_filme_ano(ano_filme):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por ano
    cursor.execute("SELECT * FROM FILMES WHERE ano_filme = :ano_filme", [ano_filme])
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_filme":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404

# Rota para buscar filmes por ator principal (GET)
@app.route('/filmes/ator_principal/<ator_principal>', methods=['GET'])
def get_filme_ator(ator_principal):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por ator principal
    cursor.execute("SELECT * FROM FILMES WHERE ator_principal = :ator_principal", [ator_principal])
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_filme":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404

# Rota para buscar filmes por atriz principal (GET)
@app.route('/filmes/atriz_principal/<atriz_principal>', methods=['GET'])
def get_filme_atriz(atriz_principal):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para buscar um filme por atriz principal
    cursor.execute("SELECT * FROM FILMES WHERE atriz_principal = :atriz_principal", [atriz_principal])
    rows = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    if rows:
        filme = [{"id_filme": row[0], "nome_filme": row[1], "ano_filme":  row[2], "genero_filme":  row[3], "ator_filme":  row[4], "atriz_principal": row[5]} for row in rows] 
        return jsonify(filme)
    else:
        return jsonify({"message": "Filme não encontrado"}), 404

# Rota para adicionar um novo filme (POST)
@app.route('/filmes', methods=['POST'])
def add_filme():
    novo_filme = request.json
    nome_filme = novo_filme.get('nome_filme')
    ano_filme = novo_filme.get('ano_filme')
    genero_filme = novo_filme.get('genero_filme')
    ator_principal = novo_filme.get('ator_principal')
    atriz_principal = novo_filme.get('atriz_principal')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para inserir um novo filme
    cursor.execute("""
        INSERT INTO FILMES (nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal)
        VALUES (:nome_filme, :ano_filme, :genero_filme, :ator_principal, :atriz_principal)
    """, [nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Filme adicionado"}), 201

# Rota para atualizar um filme existente (PUT)
@app.route('/filmes/<int:id_filme>', methods=['PUT'])
def update_filme(id_filme):
    filme_atualizado = request.json
    nome_filme = filme_atualizado.get('nome_filme')
    ano_filme = filme_atualizado.get('ano_filme')
    genero_filme = filme_atualizado.get('genero_filme')
    ator_principal = filme_atualizado.get('ator_principal')
    atriz_principal = filme_atualizado.get('atriz_principal')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para atualizar um filme
    cursor.execute("""
        UPDATE FILMES
        SET nome_filme = :nome_filme, ano_filme = :ano_filme, genero_filme = :genero_filme, ator_principal = :ator_principal, atriz_principal = :atriz_principal
        WHERE id_filme = :id_filme
    """, [nome_filme, ano_filme, genero_filme, ator_principal, atriz_principal, id_filme])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Filme atualizado"}), 200

# Rota para deletar um filme (DELETE)
@app.route('/filmes/<int:id_filme>', methods=['DELETE'])
def delete_filme(id_filme):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Consulta SQL para deletar um produto por ID
    cursor.execute("DELETE FROM FILMES WHERE id_filme = :id_filme", [id_filme])
    
    connection.commit()  # Confirma a transação
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Filme removido"}), 200

if __name__ == '__main__':
    app.run(debug=False)