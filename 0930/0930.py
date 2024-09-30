import oracledb

connection = oracledb.connect(
    user='RM554424',
    password='040704',
    dsn='oracle.fiap.com.br:1521/orcl'
)

print('Conexão estabelecida.')

cursor = connection.cursor()

# Executando uma consulta para obter todos os registros da tabela "peca"
# READ
cursor.execute("SELECT * FROM peca WHERE ROWNUM <= 10")

result = cursor.fetchall()

for row in result:
    print(row)

#cursor.close()

# CREATE

insert_query = "INSERT INTO peca (id_peca, disponibilidade_peca, nome_peca, preco_peca) VALUES (:1, :2, :3, :4)"
data = [
     ("P00032", 30, "Motor", 90.00),
     ("P00052", 2, "Carburador", 110.00),
     ("P00082", 45, "Refrigerador", 200.00)
 ]

cursor.executemany(insert_query, data)
connection.commit()
print(f"{cursor.rowcount} registros inseridos.")

# cursor.close()
# connection.close()

# UPDATE

update_query = "UPDATE peca SET disponibilidade_peca = :1 WHERE id_peca = :2"
cursor.execute(update_query, (50, "P00032"))

connection.commit()
print(f"{cursor.rowcount} registro(s) atualizado(s).")

# cursor.close()
# connection.close()

# DELETE

delete_query = "DELETE FROM peca WHERE id_peca = :1"
cursor.execute(delete_query, ("P00032",))

connection.commit()
print(f"{cursor.rowcount} registro(s) excluído(s).")
cursor.close()
connection.close()