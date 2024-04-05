# Computational Thinking Using Python - Turma: 1TDSB-2024
# CP2 – Prof. MSc. Luiz W Tavares – 03 Abril 2024
# RM554424 – Nome: Lucas Kenji Kikuchi

# lista de eleitores
eleitores = ['111', '222', '333', '444', '555']
# lista se votou (1) ou não (0)
votouOuNao = [0, 0, 0, 0, 0]
# lista vazia de candidatos
candidatos = []
# ultimo voto é nulo (len(votosCandidatos) - 1)
votosCandidatos = [0]


# cadastro dos candidatos
while True:
    candidatoAtual = input("\nNúmero do Candidato ou <fim>:  ")
    # se digitar fim, quebra o while
    if candidatoAtual.lower() == 'fim':
        break
    # se o valor não for int, continua o while
    elif not candidatoAtual.isdigit(): 
        continue
    # se o candidato já foi registrado, continua o while
    elif candidatos.count(candidatoAtual) == 1:
        continue
    # somente admite valores entre 10 e 99
    elif int(candidatoAtual) >= 10 and int(candidatoAtual) <= 99:
        candidatos.append(candidatoAtual)
        votosCandidatos.append(0)
        print(f"Nome do Candidato...........:  Candidato {candidatoAtual}")

# votação    
while True:
    eleitorAtual = input("\nDigite o Título do Eleitor ou <fim> para terminar:  ")
    # se digitar fim, quebra o while
    if eleitorAtual.lower() == 'fim':
        break
    # verifica se o eleitor está presente na lista de eleitores
    if eleitores.count(eleitorAtual) == 0:
        print("\nEleitor não autorizado para votar")
    elif eleitores.count(eleitorAtual) == 1:
        # verifica se o eleitor já votou
        if votouOuNao[eleitores.index(eleitorAtual)] == 1:
            print("\nEleitor já votou!!!")
        else:
            print("\nInício do Voto: \n")
            print("Candidatos:")
            # percorre a lista de candidatos, imprimindo cada um
            for i in range(len(candidatos)):
                print(f"{candidatos[i]} - Candidato {candidatos[i]}")
            voto = input("\nVoto - Número do Candidato:  ")
            # adiciona o voto ao candidato correspondente
            for i in range(len(candidatos)):
                if candidatos[i] == voto:
                    votosCandidatos[i]+=1
                # se o candidato não existe, adiciona 1 ao voto nulo
                elif candidatos.count(voto) == 0:
                    votosCandidatos[len(votosCandidatos) - 1]+=1
                    break
            # atualiza a lista votouOuNao, indicando se o eleitor votou (1) ou não (0)
            votouOuNao[eleitores.index(eleitorAtual)]+=1
    # verificação para caso todos os eleitores já tiverem votado 
    if votouOuNao.count(1) == 5:
        print(f"\nTodos os eleitores já votaram.\nFIM")
        break

# relatório
print("\n=========================================")
print(f"Total de eleitores: {len(eleitores)}")
print(f"Total de votos ...: {votouOuNao.count(1)}")
# votos dos candidatos
print(f"\nCandidatos ........:")
print(f"Votos:{(votosCandidatos[len(votosCandidatos) - 1]):>4} - 000 - Votos Nulo")
for i in range(len(votosCandidatos) - 1):
        print(f"Votos:{votosCandidatos[i]:>4} -  {candidatos[i]} - Candidato {candidatos[i]}")
print("\nEleitor:")
# votou ou não
for i in range(len(eleitores)):
    if votouOuNao[i] == 0:
        print(f"{eleitores[i]} - NÃO votou")
    else:
        print(f"{eleitores[i]} - votou")

