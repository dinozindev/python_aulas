# Computational Thinking Using Python - Turma: 1TDSB-2024
# CP2 – Prof. MSc. Luiz W Tavares – 03 Abril 2024
# RM554424 – Nome: Lucas Kenji Kikuchi

# oq falta: verificar se o eleitor ja votou, verificar eleitor nao autorizado, finalizar votação quando todos os eleitores ja tiverem votado, imprimir relatorio

eleitores = ['111', '222', '333', '444', '555']
votouOuNao = [0, 0, 0, 0, 0]
candidatos = []
# ultimo voto é nulo (len(votosCandidatos) - 1)
votosCandidatos = [0]


# cadastro dos candidatos
while True:
    candidatoAtual = input("Número do Candidato ou <fim>:  ")
    if candidatoAtual.lower() == 'fim':
        print("\n")
        break
    # somente admite valores entre 10 e 99
    if int(candidatoAtual) >= 10 and int(candidatoAtual) <= 99:
        candidatos.append(candidatoAtual)
        votosCandidatos.append(0)
        print(f"Nome do Candidato...........:  Candidato {candidatoAtual} \n")
        print(candidatos)

# votação    
while True:
    eleitorAtual = input("Digite o Título do Eleitor ou <fim> para terminar:  ")
    if eleitorAtual.lower() == 'fim':
        print("\n")
        break
    if eleitores.count(eleitorAtual) == 0:
        print("\nEleitor não autorizado para votar\n")
    elif eleitores.count(eleitorAtual) == 1:
        # verifica se o eleitor já votou
        if votouOuNao[eleitores.index(eleitorAtual)] == 1:
            print("\nEleitor já votou!!!\n")
        else:
            print("\nInício do Voto: \n")
            # percorre o array de candidatos, imprimindo cada um
            for i in range(len(candidatos)):
                print(f"{candidatos[i]} - Candidato {candidatos[i]}")
            voto = input("\nVoto - Número do Candidato:  ")
            # contabiliza os votos
            for i in range(len(candidatos)):
                if candidatos[i] == voto:
                    votosCandidatos[i]+=1
                # se o candidato não existe, adiciona 1 ao voto nulo
                elif candidatos.count(voto) == 0:
                    votosCandidatos[len(votosCandidatos) - 1]+=1
                    break
            # atualiza a lista votouOuNao, indicando se o eleitor votou (1) ou não (0)
            votouOuNao[eleitores.index(eleitorAtual)]+=1 
    if votouOuNao.count(1) == 5:
        print(f"\nTodos os eleitores já votaram.\nFIM\n")
        break

print("=========================================")
print(f"Total de eleitores: {len(eleitores)}")
print(f"Total de votos ...: {votouOuNao.count(1)}")
print(f"\nCandidatos ........:")
print(f"Votos:{(votosCandidatos[len(votosCandidatos) - 1]):>3} - 000 - Votos Nulo")
for i in range(len(votosCandidatos) - 1):
        print(f"Votos:{votosCandidatos[i]:>3} - {candidatos[i]:>2} - Candidato {candidatos[i]}")
print("\n")
for i in range(len(eleitores)):
    if votouOuNao[i] == 0:
        print(f"{eleitores[i]} - NÃO votou")
    else:
        print(f"{eleitores[i]} - votou")
    
print(votosCandidatos)

