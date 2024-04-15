familia = {'sobrenome': {'Silva':   {'pai':'Joao',  
                                     'mae': 'Maria', 
                                     'crianca 1': 'Pedro',
                                     'tio': 'Rick'},
                         'Machado': {'pai':'Pedro', 
                                     'mae': 'Lidia', 
                                     'criancas': {'Maria': '15', 
                                                  'Vitor': '7'}}}}

for sbnm in list(familia['sobrenome']):
    print('Familia: ', sbnm, '\n')
    for familiar in list(familia['sobrenome'][sbnm]):
        xty = (type(familia['sobrenome'][sbnm][familiar]) == dict)
        if xty:
            for lisxint in list(familia['sobrenome'][sbnm][familiar]):
                print('sobrenome', sbnm, familiar, lisxint)
                print('Membro: ', lisxint, ': ', familia['sobrenome'][sbnm][familiar][lisxint])
        else:
            print('Membro: ', familiar, ': ', familia['sobrenome'][sbnm][familiar])
    print('\n')