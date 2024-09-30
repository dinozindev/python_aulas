import oracledb

connection = oracledb.connect(
    user='RM554424',
    password='040704',
    dsn='oracle.fiap.com.br:1521/orcl'
)

print('Conexão estabelecida.')