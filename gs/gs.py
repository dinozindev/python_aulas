#Grupo Ecocean
#Giovanna Revito Roz - RM558981
#Kaian Gustavo de Oliveira Nascimento - RM558986
#Lucas Kenji Kikuchi - RM554424

#link para o video: https://youtu.be/KyvPwDbnGiQ?si=zsFUhr7EWfbzlnlM


#importação do re
import re;

# lista de organizações
organizacoes = [{'nome': 'Oceanos Mais Limpos', 'pontuacao': 1200}, {'nome': 'Mares Azuis', 'pontuacao': 1000}, {'nome': 'WaterEco', 'pontuacao': 800}, {'nome': 'OceansBy', 'pontuacao': 600}, {'nome': 'SustainableMarine', 'pontuacao': 400}]
# tipos de poluição
tipos_poluicao = ['Plástico', 'Vazamento de óleo', 'Detritos de embarcações', 'Descarte de esgoto', 'Produtos químicos']
#oceanos
oceanos = ['Oceano Índico', 'Oceano Antártico', 'Oceano Pacífico', 'Oceano Atlântico', 'Oceano Ártico']
#quantidade de poluição
qtnd = ['Baixa', 'Média', 'Alta', 'Alarmante']
#tipos de pesca 
tipos_pescas_ilegais = ['Pesca em Áreas Protegidas', 'Pesca de Espécies Protegidas', 'Uso de Equipamentos Proibidos', 'Pesca Fora de Temporada', 'Pesca Sem Licença', 'Captura Excedendo Limites de Quantidade', 'Descarte Ilegal de Peixes', 'Pesca não declarada e não regulamentada']
#recompensas
recompensas = [
    {'nome_recompensa': 'Desconto de 10% em serviços empresas parceiras', 'pontos_necessarios': 20},
    {'nome_recompensa': 'Reconhecimento de Espécies por imagem ilimitado por 7 dias', 'pontos_necessarios': 35},
    {'nome_recompensa': 'Desconto de 20% em serviços empresas parceiras', 'pontos_necessarios': 40},
    {'nome_recompensa': 'Desconto de 45% em serviços empresas parceiras', 'pontos_necessarios': 70},
    {'nome_recompensa': 'Reconhecimento de Espécies por imagem ilimitado por 30 dias', 'pontos_necessarios': 120}
]
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
    {'nome': 'Raia-manta','nome_cientifico': 'Manta birostris','descricao': 'A raia-manta é uma das maiores espécies de raia, conhecida por sua grande envergadura e comportamento grácil. Habita águas tropicais e subtropicais.','status_conservacao': 'Vulnerável'},
    {'nome': 'Tartaruga-de-couro','nome_cientifico': 'Dermochelys coriacea','descricao': 'A tartaruga-de-couro é a maior das tartarugas marinhas, conhecida por sua carapaça distinta de couro em vez de placas ósseas. Habita oceanos tropicais e subtropicais.','status_conservacao': 'Vulnerável'},
    {'nome': 'Coral-estaghorn','nome_cientifico': 'Acropora cervicornis','descricao': 'O coral-estaghorn é caracterizado por seus ramos longos e finos que se assemelham a chifres de cervos. Habita recifes de coral no Caribe.','status_conservacao': 'Em perigo crítico'},
    {'nome': 'Vaquita','nome_cientifico': 'Phocoena sinus','descricao': 'A vaquita é a menor espécie de cetáceo e é encontrada apenas no norte do Golfo da Califórnia, no México.','status_conservacao': 'Criticamente em perigo'},
    {'nome': 'Peixe-serra-longo','nome_cientifico': 'Pristis pristis','descricao': 'O peixe-serra-longo é um grande peixe de água salgada com um focinho serrilhado distinto. É encontrado em águas tropicais e subtropicais, mas suas populações têm diminuído drasticamente devido à pesca e à perda de habitat.','status_conservacao': 'Criticamente em perigo'},
    {'nome': 'Boto-da-baía-de-Yangtze','nome_cientifico': 'Lipotes vexillifer','descricao': 'O boto-da-baía-de-Yangtze, também conhecido como baiji, é um golfinho de água doce nativo do rio Yangtze na China. É uma das espécies de cetáceos mais ameaçadas do mundo devido à poluição e à degradação do habitat.','status_conservacao': 'Criticamente em perigo'},   
]

usuarioDados = []
denunciasPesca = []
denunciasPoluicao = []
pontosUsuario = 0
recompensas_reivindicadas = []
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
        op_delete = input("\nDeseja realmente deletar o seu cadastro? S ou N (Todos os dados registrados, incluindo denúncias, recompensas e pontos serão removidos): ")
        if op_delete.upper() != "S" and op_delete.upper() != "N":
            print("\nDigite uma opção válida.")
            continue
        elif op_delete.upper() == "S":
            usuarioDados.clear()
            denunciasPesca.clear()
            denunciasPoluicao.clear()
            global pontosUsuario
            pontosUsuario = 0
            recompensas_reivindicadas.clear()
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
            match verif_usuario_op:
                case 0:
                    break
                case 1:
                    deletar_usuario()
                    break
                case 2:
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
        print("\nVocê não está cadastrado. Irei te redirecionar para o menu...")
        return
    denuncia = []
    while True:
        print("\n==============[ TIPO DE PESCA ILEGAL ]==============\n")
        for i in range(len(tipos_pescas_ilegais)):
            print(f"{i} - {tipos_pescas_ilegais[i]}")
        opt_pescas_ilegais = input("\nQual o tipo de pesca ilegal identificada?......................: ")
        if not opt_pescas_ilegais.isdigit() or int(opt_pescas_ilegais) > 7 or int(opt_pescas_ilegais) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_pescas_ilegais = int(opt_pescas_ilegais)
            denuncia.append(tipos_pescas_ilegais[opt_pescas_ilegais])
            break
    while True: 
        horas = input("Que horas a pesca ilegal foi identificada? (ex: 13:30).........: ")
        if re.match(regexHoras, horas) is None:
            print("Digite um horário válido.")
            continue
        else:
            denuncia.append(horas)
            break 
    while True: 
        data = input("Qual a data em que a pesca ilegal foi identificada? (ex: 07/06): ")
        if re.match(regexData, data) is None:
            print("Digite uma data válida.")
            continue
        else:
            denuncia.append(data)
            break 
    while True:
        coordenadas = input("Quais as coordenadas? (Ex: -45.12345, -123.12345)..............: ")
        if re.match(regexCoordenadas, coordenadas) is None:
            print("Digite um nome válido.")
            continue
        else:
            denuncia.append(coordenadas)
            break
    ponto_referencia = input('Qual o ponto de referência?....................................: ')
    denuncia.append(ponto_referencia)
    observacoes = input("Mais alguma observação sobre o ocorrido?.......................: ")
    denuncia.append(observacoes)
    adicionar_pontos(10)
    denunciasPesca.append(denuncia)
    print("\nDenúncia de pesca ilegal registrada com sucesso.")

# denunciar poluição
def denunciar_poluicao():
    print("\nIniciando denúncia de poluição...\n")
    if usuarioDados == []:
        print("Você não está cadastrado. Irei te redirecionar para o menu...")
        return
    denuncia = []
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
            denuncia.append(tipos_poluicao[opt_poluicao])
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
            denuncia.append(oceanos[opt_oceano])
            break
    while True:
        print("\n==============[ QUANTIDADE ]==============\n")
        for i in range(len(qtnd)):
            print(f"{i} - {qtnd[i]}")
        opt_qtnd = input("\nQual o nível da quantidade encontrada?...........: ")
        if not opt_qtnd.isdigit() or (int(opt_qtnd) > 3) or int(opt_qtnd) < 0:
            print("\nSelecione uma opção válida.")
            continue
        else:
            opt_qtnd = int(opt_qtnd)
            denuncia.append(qtnd[opt_qtnd])
            break
    while True:
        coordenadas = input("Digite as coordenadas (Ex: -45.12345, -123.12345): ")
        if re.match(regexCoordenadas, coordenadas) is None:
            print("Digite um nome válido.")
            continue
        else:
            denuncia.append(coordenadas)
            break
    ponto_referencia = input('Qual o ponto de referência?......................: ')
    denuncia.append(ponto_referencia)
    adicionar_pontos(10)
    denunciasPoluicao.append(denuncia)
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
    print("\nIniciando consulta de espécie...")
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

# gerenciar denuncia de pesca ilegal
def gerenciar_denuncia_pesca(denunciaPesca):
    print("\nIniciando gerenciamento de denúncia de pesca ilegal...")
    while True:
        if denunciaPesca == []:
            print("\nVocê não realizou nenhuma denúncia ainda. Retornando ao menu...")
            break
        print("\n==============[ GERENCIAMENTO DENÚNCIA(S) DE PESCA ILEGAL ]==============\n")
        print("1 - Remover denúncia de pesca ilegal")
        print("2 - Visualizar informações da(s) denúncia(s) de pesca ilegal")
        print("0 - Sair")
        opt_gepesca = input("\nSelecione uma opção: ")
        if not opt_gepesca.isdigit() or int(opt_gepesca) > 2 or int(opt_gepesca) < 0:
            print("\nSelecione uma opção válida.")
            continue
        opt_gepesca = int(opt_gepesca)
        match opt_gepesca:
            case 0:
                print("Retornando ao menu principal...")
                break
            case 1:
                deletar_denuncia_pesca()
                break
            case 2:
                print("\n==============[ INFORMAÇÕES DA(S) DENÚNCIA(S) DE PESCA ILEGAL ]==============") 
                for i in range(len(denunciaPesca)):
                    print(f"\nDenúncia {i+1}\n")
                    print(f"Tipo..................: {denunciaPesca[i][0]}") 
                    print(f"Horário...............: {denunciaPesca[i][1]}") 
                    print(f"Data..................: {denunciaPesca[i][2]}")
                    print(f"Coordenadas...........: {denunciaPesca[i][3]}")  
                    print(f"Ponto de referência...: {denunciaPesca[i][4]}")
                    print(f"Observações adicionais: {denunciaPesca[i][5]}") 
                input("\nPressione ENTER para voltar ao menu: ")
                print("\nRetornando ao menu...")
                continue

# deletar denuncia de pesca ilegal
def deletar_denuncia_pesca():
    if not denunciasPesca:
        print("\nVocê não fez nenhuma denúncia ainda.")
        return
    while True:
        print("\n==============[ DELETAR DENÚNCIA DE PESCA ILEGAL ]==============\n")
        for i in range(len(denunciasPesca)):
            print(f"{i} - Denúncia {i+1}")
        op_pesca = input("\nQual denúncia deseja remover?: ") 
        if not op_pesca.isdigit() or (int(op_pesca) > (len(denunciasPesca) - 1) or int(op_pesca) < 0):
            print("\nSelecione uma opção válida.")
            continue
        op_pesca = int(op_pesca)   
        op_delete = input("\nDeseja realmente remover a denúncia feita? S ou N: ")
        if op_delete.upper() != "S" and op_delete.upper() != "N":
            print("\nDigite uma opção válida.")
            continue
        elif op_delete.upper() == "S":
            denunciasPesca.pop(op_pesca)
            print("\nDenúncia removida com sucesso.")
            break
        elif op_delete.upper() == "N":
            print("\nA Denúncia não foi removida.")
            break

# gerenciar denuncia de poluição
def gerenciar_denuncia_poluicao(denunciaPoluicao):
    print("\nIniciando gerenciamento de denúncia de poluição...")
    while True:
        if denunciaPoluicao == []:
            print("\nVocê não realizou nenhuma denúncia ainda. Retornando ao menu...")
            break
        print("\n==============[ GERENCIAMENTO DENÚNCIA DE POLUIÇÃO ]==============\n")
        print("1 - Remover denúncia de poluição")
        print("2 - Visualizar informações da(s) denúncia(s) de poluição")
        print("0 - Sair")
        opt_gerpoluicao = input("\nSelecione uma opção: ")
        if not opt_gerpoluicao.isdigit() or int(opt_gerpoluicao) > 2 or int(opt_gerpoluicao) < 0:
            print("\nSelecione uma opção válida.")
            continue
        opt_gerpoluicao = int(opt_gerpoluicao)
        match opt_gerpoluicao:
            case 0:
                print("Retornando ao menu principal...")
                break
            case 1:
                deletar_denuncia_poluicao()
                break
            case 2:
                print("\n==============[ INFORMAÇÕES DA(S) DENÚNCIA(S) DE POLUIÇÃO ]==============")
                for i in range(len(denunciasPoluicao)): 
                    print(f"\nDenúncia {i+1}\n")
                    print(f"Tipo de poluição...: {denunciaPoluicao[i][0]}") 
                    print(f"Oceano.............: {denunciaPoluicao[i][1]}") 
                    print(f"Quantidade.........: {denunciaPoluicao[i][2]}")
                    print(f"Coordenadas........: {denunciaPoluicao[i][3]}")  
                    print(f"Ponto de referência: {denunciaPoluicao[i][4]}")
                input("\nPressione ENTER para voltar ao menu: ")
                print("\nRetornando ao menu...")
                continue

# deletar denuncia de poluição
def deletar_denuncia_poluicao():
    if not denunciasPoluicao:
        print("\nVocê não fez nenhuma denúncia ainda.")
        return
    while True:
        print("\n==============[ DELETAR DENÚNCIA DE POLUIÇÃO ]==============\n")
        for i in range(len(denunciasPoluicao)):
            print(f"{i} - Denúncia {i+1}")
        op_poluicao = input("\nQual denúncia deseja remover?: ") 
        if not op_poluicao.isdigit() or (int(op_poluicao) > (len(denunciasPoluicao) - 1) or int(op_poluicao) < 0):
            print("\nSelecione uma opção válida.")
            continue
        op_poluicao = int(op_poluicao)   
        op_delete = input("\nDeseja realmente remover a denúncia feita? S ou N: ")
        if op_delete.upper() != "S" and op_delete.upper() != "N":
            print("\nDigite uma opção válida.")
            continue
        elif op_delete.upper() == "S":
            denunciasPoluicao.pop(op_poluicao)
            print("\nDenúncia removida com sucesso.")
            break
        elif op_delete.upper() == "N":
            print("\nA Denúncia não foi removida.")
            break

# adicionar pontos a pontuação do usuário
def adicionar_pontos(pontos):
    global pontosUsuario
    pontosUsuario += pontos

# remover pontos da pontuação do usuário
def remover_pontos(pontos):
    global pontosUsuario
    pontosUsuario -= pontos

# seleção de recompensa
def receber_recompensa():
    while True:
        print("\n==============[ RECOMPENSAS ]==============\n")
        for i in range(len(recompensas)):
            print(f"{i+1} - {recompensas[i]['nome_recompensa']} - {recompensas[i]['pontos_necessarios']} pontos")
        print("0  - Sair")
        opt_recompensa = input("\nQual recompensa deseja resgatar?: ")
        if not opt_recompensa.isdigit() or (int(opt_recompensa) > len(recompensas) or int(opt_recompensa) < 0):
            print("\nSelecione uma opção válida.")
            continue
        opt_recompensa = int(opt_recompensa)
        if opt_recompensa == 0:
            print("\nRetornando ao menu de recompensas...")
            break
        if 1 <= opt_recompensa <= len(recompensas):
            opt_recompensa-=1
        if recompensas[opt_recompensa]['pontos_necessarios'] > pontosUsuario:
            print("\nVocê não possui pontos suficientes para reivindicar a recompensa.")
            continue
        elif recompensas[opt_recompensa] in recompensas_reivindicadas:
            print("\nVocê já reivindicou essa recompensa.")
            continue
        else:
            recompensas_reivindicadas.append(recompensas[opt_recompensa])
            remover_pontos(recompensas[opt_recompensa]['pontos_necessarios'])
            print("\nRecompensa reivindicada com sucesso.")
            break

#visualização das recompensas obtidas
def visualizar_recompensas_recebidas():
    if recompensas_reivindicadas == []:
        print("\nVocê ainda não reivindicou nenhuma recompensa.")
        return
    print("\n==============[ RECOMPENSAS ATIVAS ]==============\n")
    for i in range(len(recompensas_reivindicadas)):
        print(f"- {recompensas_reivindicadas[i]['nome_recompensa']}")
    input('\nPressione a tecla ENTER para retornar ao menu: ')
    return
        
# consultar as recompensas
def consultar_recompensas():
    print("\nIniciando consulta de recompensas de usuário...")
    if usuarioDados == []:
        print("\nVocê ainda não se cadastrou.")
        return
    while True:
        print("\n==============[ MENU RECOMPENSAS ]==============\n")
        print(f"Pontuação atual: {pontosUsuario}\n")
        print("1 - Receber recompensa")
        print("2 - Visualizar recompensas reivindicadas")
        print("0 - Sair")
        opt_rec = input('\nSelecione uma opção para continuar: ')
        if not opt_rec.isdigit() or (int(opt_rec) > 2 or int(opt_rec) < 0):
            print("\nSelecione uma opção válida.")
            continue
        opt_rec = int(opt_rec)
        match opt_rec:
            case 0:
                break
            case 1:
                receber_recompensa()
            case 2:
                visualizar_recompensas_recebidas()
                
# menu    
while True:
    print("\n==============[ MENU ]==============\n")
    print("1  - Cadastro Usuário")
    print("2  - Gerenciar Usuário")
    print("3  - Denunciar Pesca Ilegal")
    print("4  - Gerenciar Denúncia(s) de Pesca Ilegal") 
    print("5  - Denunciar Poluição")
    print("6  - Gerenciar Denúncia(s) de Poluição") 
    print("7  - Consultar Espécies")
    print("8  - Visualizar pontuação das organizações")
    print("9  - Consultar Recompensas de Usuário")
    print("0  - Sair\n")
    option = input("Opção: ")
    if not option.isdigit() or (int(option) > 9 or int(option) < 0):
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
            gerenciar_denuncia_pesca(denunciasPesca)
        case 5:
            denunciar_poluicao()
        case 6:
            gerenciar_denuncia_poluicao(denunciasPoluicao)
        case 7:
            consultar_especies()
        case 8:
            pontuacao_organizacoes()
        case 9:
            consultar_recompensas()