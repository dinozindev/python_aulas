telefone_lista = [('Yan', '1234-5678'), ('Maria', '3322-7755')]

for i in range(len(telefone_lista)):
    for j in range(len(telefone_lista[i])):
        print(i, j, telefone_lista[i][j])

# dict
telefone = {'Leo': '1234-5678', 'Pedro': '9999-9999', 'Carlos': '1234-5432', 'Maria': '1232-5876'}
telefone_novo = {}
print(telefone)
print(telefone['Leo'])
print(telefone.get('Roberto', 'Usuário não encontrado'))
print('9999-9999' in telefone.values())

for nome in telefone:
    print(nome, telefone[nome])

for nome in telefone:
    telefone_novo[nome] = '9' + telefone[nome]  
print(telefone_novo)

familia = {'sobrenome': {'Silva':   {'pai':'Joao',  'mae': 'Maria', 
                                    'crianca 1': 'Pedro'},
                        'Machado': {'pai':'Pedro', 
                                    'mae': 'Lidia', 
                                    'criancas': (('Maria', 15),
                                                ('Vitor', 7))}}}

print(familia['sobrenome']['Silva'])
print(familia['sobrenome'].get('Silva'))

for sobrenome in list(familia['sobrenome']):
    print('Familia ', sobrenome, '\n')

    for familiar in list(familia['sobrenome'][sobrenome]):
        print('Membro: ', familiar, familia['sobrenome'][sobrenome][familiar])
    
    print('\n')