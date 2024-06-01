import re;

organizacoes = [{'nome': 'Oceanos Mais Limpos', 'pontuacao': 1200}, {'nome': 'Mares Azuis', 'pontuacao': 1000}, {'nome': 'WaterEco', 'pontuacao': 800}, {'nome': 'OceansBy', 'pontuacao': 600}, {'nome': 'SustainableMarine', 'pontuacao': 400}]

tipos_poluicao = ['Plástico', 'Vazamento de óleo', 'Detritos de embarcações', 'Descarte de esgoto', 'Produtos químicos']
oceanos = ['Oceano Índico', 'Oceano Antártico', 'Oceano Pacífico', 'Oceano Atlântico', 'Oceano Ártico']
qtnd = ['Baixa', 'Média', 'Alta', 'Alarmante']
tipos_pescas_ilegais = ['Pesca em Áreas Protegidas', 'Pesca de Espécies Protegidas', 'Uso de Equipamentos Proibidos', 'Pesca Fora de Temporada', 'Pesca Sem Licença', 'Captura Excedendo Limites de Quantidade', 'Descarte Ilegal', 'Pesca não declarada e não regulamentada']

#lista de especies
especies_marinhas = [
    {'nome': 'Tartaruga-verde','nome_cientifico': 'Chelonia mydas','descricao': 'A tartaruga-verde é uma grande tartaruga marinha encontrada principalmente em mares tropicais e subtropicais. É herbívora e se alimenta principalmente de algas e ervas marinhas.','status_conservacao': 'Em Perigo'}, 
    {'nome': 'Baleia-azul','nome_cientifico': 'Balaenoptera musculus','descricao': 'A baleia-azul é o maior animal conhecido a ter existido, podendo atingir mais de 30 metros de comprimento. Alimenta-se principalmente de krill e outras pequenas criaturas marinhas.','status_conservacao': 'Em Perigo'}, 
    {'nome': 'Golfinho-nariz-de-garrafa','nome_cientifico': 'Tursiops truncatus','descricao': 'O golfinho-nariz-de-garrafa é uma espécie de golfinho amplamente distribuída em mares temperados e tropicais. É conhecido por sua inteligência e comportamento sociável.','status_conservacao': 'Pouco Preocupante'},
    {'nome': 'Tubarão-branco','nome_cientifico': 'Carcharodon carcharias','descricao': 'O tubarão-branco é um dos maiores predadores marinhos, conhecido por seu tamanho e força. Habita águas costeiras temperadas e subtropicais em todo o mundo.','status_conservacao': 'Vulnerável'},
    {'nome': 'Peixe-palhaço','nome_cientifico': 'Amphiprioninae','descricao': 'O peixe-palhaço é conhecido por sua relação simbiótica com anêmonas-do-mar. Possui cores vibrantes e é popular em aquários marinhos.','status_conservacao': 'Pouco Preocupante'},
    {'nome': 'Polvo-gigante-do-pacífico','nome_cientifico': 'Enteroctopus dofleini','descricao': 'O polvo-gigante-do-pacífico é a maior espécie de polvo, encontrada no Oceano Pacífico Norte. É conhecido por sua inteligência e capacidade de camuflagem.','status_conservacao': 'Pouco Preocupante'},
    {'nome': 'Manati','nome_cientifico': 'Trichechus','descricao': 'O manati, também conhecido como peixe-boi, é um grande mamífero marinho herbívoro encontrado em águas costeiras e rios de regiões tropicais e subtropicais.','status_conservacao': 'Vulnerável'},
    {'nome': 'Cavalo-marinho','nome_cientifico': 'Hippocampus','descricao': 'O cavalo-marinho é um pequeno peixe marinho com uma aparência única que lembra um cavalo. É conhecido por suas caudas preênseis e a reprodução onde os machos carregam os ovos.','status_conservacao': 'Vulnerável'},
    {'nome': 'Estrela-do-mar girassol','nome_cientifico': 'Pycnopodia helianthoides','descricao': 'A estrela-do-mar girassol é uma das maiores espécies de estrela-do-mar, encontrada no Pacífico Norte. Tem muitas pernas e é um predador eficiente.','status_conservacao': 'Em Perigo'},
    {'nome': 'Raia-manta','nome_cientifico': 'Manta birostris','descricao': 'A raia-manta é uma das maiores espécies de raia, conhecida por sua grande envergadura e comportamento grácil. Habita águas tropicais e subtropicais.','status_conservacao': 'Vulnerável'}
]

usuarioDados = []
denunciaPesca = []
denunciaPoluicao = []
relatoEspecie = []
regexCpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
regexTel = r'\d{2} 9\d{4}-\d{4}'
regexNome = r"^[A-Za-zÀ-ÿ'\- ]+$"
regexCoordenadas = r'^([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)),\s*([-+]?(180(\.0+)?|(1[0-7]\d|[1-9]?\d)(\.\d+)?))$'
regexHoras = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
regexData = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])$"

# cadastro do usuario
def cadastro_usuario():
    print("Iniciando cadastro do usuário...\n")
    if len(usuarioDados) > 0:
        print("Você já está cadastrado. Irei te redirecionar para o menu...")
        return
    # cadastro nome
    while True:
        nome = input("Digite o seu nome........................: ")
        if re.match(regexNome, nome) is None:
            print("Digite um nome válido.")
            continue
        else:
            usuarioDados.append(nome)
            break 
    # cadastro idade   
    while True:
        idade = input("Digite sua idade.........................: ")
        if not idade.isdigit() or int(idade) < 13 or int(idade) > 90:
            print("Digite uma idade válida.")
            continue
        else:
            usuarioDados.append(idade)
            break
    # cadastro CPF
    while True:
        cpf = input("Digite o seu CPF (ex: xxx.xxx.xxx-xx)....: ")
        if re.match(regexCpf, cpf) is None:
            print("Digite um CPF válido.")
            continue
        else:
            usuarioDados.append(cpf)
            break
    # cadastro endereço
    while True:
        endereco = input("Digite o seu endereço....................: ")
        if re.match(regexNome, endereco) is None:
            print("Digite um endereço válido.")
            continue
        else:
            usuarioDados.append(endereco)
            break
    # cadastro telefone
    while True:
        telefone = input("Digite o seu telefone (ex: xx xxxxx-xxxx): ")
        if re.match(regexTel, telefone) is None:
            print("Digite um número de telefone válido.")
            continue
        else: 
            usuarioDados.append(telefone)
            break
    print("\nUsuário cadastrado com sucesso!")

#remover usuario 
def deletar_usuario():
    while True:
        if not usuarioDados:
            print("\nVocê não está cadastrado ainda.")
            break
        op_delete = input("\nDeseja realmente deletar o seu cadastro? S ou N: ")
        if op_delete.upper() != "S" and op_delete.upper() != "N":
            print("\nDigite uma opção válida.")
            continue
        elif op_delete.upper() == "S":
            usuarioDados.clear()
            print("\nCadastro removido com sucesso.")
            break
        elif op_delete.upper() == "N":
            print("\nO cadastro não foi removido.")
            break

# visualização das informações do usuário (Nome, Idade, CPF, endereço e telefone)
def gerenciar_usuario(usuarioDados):
        print("\nIniciando menu de gerenciamento do usuário...") 
        while True:
            if usuarioDados == []:
                print("\nVocê ainda não se cadastrou.")
                break
            print("\n==============[ GERENCIAMENTO USUÁRIO ]==============\n")
            print("1 - Remover usuário")
            print("2 - Visualizar informações do usuário")
            print("0 - Sair")
            verif_usuario_op = input("\nSelecione uma opção: ")
            if not verif_usuario_op.isdigit() or int(verif_usuario_op) > 2 or int(verif_usuario_op) < 0:
                print("\nSelecione uma opção válida.")
                continue
            verif_usuario_op = int(verif_usuario_op)
            if verif_usuario_op == 0:
                break
            elif verif_usuario_op == 1:
                deletar_usuario()
                break
            elif verif_usuario_op == 2:
                print("\n==============[ INFORMAÇÕES DO USUÁRIO ]==============\n") 
                print(f"Nome....: {usuarioDados[0]}") 
                print(f"Idade...: {usuarioDados[1]}") 
                print(f"CPF.....: {usuarioDados[2]}") 
                print(f"Endereço: {usuarioDados[3]}") 
                print(f"Telefone: {usuarioDados[4]}\n") 
                input("Pressione ENTER para voltar ao menu: ")
                print("Retornando ao menu do usuário...")
                continue

# denunciar pesca ilegal      
def denunciar_pesca_ilegal():
    print("\nIniciando denúncia de pesca ilegal...")
    if usuarioDados == []:
        print("Você não está cadastrado. Irei te redirecionar para o menu...")
        return
    while True:
        print("\n==============[ TIPO DE PESCA ILEGAL ]==============\n")
        for i in range(len(tipos_pescas_ilegais)):
            print(f"{i} - {tipos_pescas_ilegais[i]}")
        opt_pescas_ilegais = input("\nQual o tipo de pesca ilegal identificada?: ")
        if not opt_pescas_ilegais.isdigit() or int(opt_pescas_ilegais) > 7 or int(opt_pescas_ilegais) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_pescas_ilegais = int(opt_pescas_ilegais)
            denunciaPesca.append(tipos_pescas_ilegais[opt_pescas_ilegais])
            break
    while True: 
        horas = input("Que horas a pesca ilegal foi identificada? (ex: 13:30): ")
        if re.match(regexHoras, horas) is None:
            print("Digite um horário válido.")
            continue
        else:
            denunciaPesca.append(horas)
            break 
    while True: 
        data = input("Qual a data em que a pesca ilegal foi identificada? (ex: 07/06): ")
        if re.match(regexData, data) is None:
            print("Digite uma data válida.")
            continue
        else:
            denunciaPesca.append(data)
            break 
    while True:
        coordenadas = input("Quais as coordenadas?7 (Ex: -45.12345, -123.12345): ")
        if re.match(regexCoordenadas, coordenadas) is None:
            print("Digite um nome válido.")
            continue
        else:
            denunciaPesca.append(coordenadas)
            break
    ponto_referencia = input('Qual o ponto de referência?: ')
    denunciaPesca.append(ponto_referencia)
    observacoes = input("Mais alguma observação sobre o ocorrido?: ")
    denunciaPesca.append(observacoes)
    print("\nDenúncia de pesca ilegal registrada com sucesso.")

# denunciar poluição
def denunciar_poluicao():
    print("\nIniciando denúncia de poluição...\n")
    if usuarioDados == []:
        print("Você não está cadastrado. Irei te redirecionar para o menu...")
        return
    while True: 
        print("\n==============[ TIPO DE POLUIÇÃO ]==============\n")
        for i in range(len(tipos_poluicao)):
            print(f"{i} - {tipos_poluicao[i]}")
        opt_poluicao = input("\nQual o tipo de poluição encontrada?: ")
        if not opt_poluicao.isdigit() or (int(opt_poluicao) > 4) or int(opt_poluicao) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_poluicao = int(opt_poluicao)
            denunciaPoluicao.append(tipos_poluicao[opt_poluicao])
            break
    while True:
        print("\n==============[ OCEANO ]==============\n")
        for i in range(len(oceanos)):
            print(f"{i} - {oceanos[i]}")
        opt_oceano = input("\nEm qual oceano a poluição foi encontrada?: ")
        if not opt_oceano.isdigit() or (int(opt_oceano) > 4) or int(opt_oceano) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_oceano = int(opt_oceano)
            denunciaPoluicao.append(oceanos[opt_oceano])
            break
    while True:
        print("\n==============[ QUANTIDADE ]==============\n")
        for i in range(len(qtnd)):
            print(f"{i} - {qtnd[i]}")
        opt_qtnd = input("\nQual o nível da quantidade encontrada?: ")
        if not opt_qtnd.isdigit() or (int(opt_qtnd) > 3) or int(opt_qtnd) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_qtnd = int(opt_qtnd)
            denunciaPoluicao.append(qtnd[opt_qtnd])
            break
    while True:
        coordenadas = input("Digite as coordenadas (Ex: -45.12345, -123.12345): ")
        if re.match(regexCoordenadas, coordenadas) is None:
            print("Digite um nome válido.")
            continue
        else:
            denunciaPoluicao.append(coordenadas)
            break
    ponto_referencia = input('Qual o ponto de referência?: ')
    denunciaPoluicao.append(ponto_referencia)
    print("\nDenúncia de poluição registrada com sucesso.")

# pontuação das organizações    
def pontuacao_organizacoes():
    posicao = 1
    print("\n==============[ TABELA DE ORGANIZAÇÕES ]==============\n") 
    organizacoes_sorted = sorted(organizacoes, key=lambda x: x['pontuacao'], reverse=True)
    for organizacao in organizacoes_sorted:
        print(f"{posicao}ª - {organizacao['nome']}, Pontuação: {organizacao['pontuacao']}")
        posicao+=1
    input("\nPressione ENTER para voltar ao menu principal: ")

# consulta especies
def consultar_especies():
    print("Iniciando consulta de espécie...")
    while True:
        print("\n==============[ ESPÉCIES ]==============\n")
        for i in range(len(especies_marinhas)):
            print(f"{i+1:<2d} - {especies_marinhas[i]['nome']}")
        print("0  - Sair\n")
        option_especies = input("Selecione uma espécie para consultar: ")
        if not option_especies.isdigit() or (int(option_especies) > len(especies_marinhas) or int(option) < 0):
            print("\nSelecione uma opção válida.")
            continue
        option_especies = int(option_especies)
        if option_especies == 0:
            print("\nRetornando ao menu principal...")
            break
        if 1 <= option_especies <= len(especies_marinhas):
            while True:
                i = option_especies - 1
                print(f"\n==============[ {especies_marinhas[i]['nome']} ]==============\n")
                print(f"Nome.................: {especies_marinhas[i]['nome']}")
                print(f"Nome científico......: {especies_marinhas[i]['nome_cientifico']}")
                print(f"Descrição............: {especies_marinhas[i]['descricao']}")
                print(f"Status de Conservação: {especies_marinhas[i]['status_conservacao']}")
                input("\nPressione a tecla ENTER para voltar ao menu de espécies: ")
                break
    
# menu    
while True:
    print("\n==============[ MENU ]==============\n")
    print("1  - Cadastro Usuário")
    print("2  - Gerenciar Usuário")
    print("3  - Denunciar Pesca Ilegal")
    print("4  - Denunciar Poluição")
    print("5  - Relatar Espécie")
    print("6  - Consultar Espécies")
    print("7  - Visualizar pontuação das organizações")
    print("0  - Sair\n")
    option = input("Opção: ")
    if not option.isdigit() or (int(option) > 7 or int(option) < 0):
        print("\nSelecione uma opção válida.")
        continue
    option = int(option)   
    match option:
        case 0:
            print("\nSolicitação encerrada.\n")
            break
        case 1:
            cadastro_usuario()
        case 2:
            gerenciar_usuario(usuarioDados)
        case 3:
            denunciar_pesca_ilegal()
        case 4:
            denunciar_poluicao()
        case 5:
            print()
        case 6:
            consultar_especies()
        case 7:
            pontuacao_organizacoes()