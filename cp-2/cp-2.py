# Computational Thinking Using Python - Turma: 1TDSB-2024
# CP2 – Prof. MSc. Luiz W Tavares – 03 Abril 2024
# RM554424 – Nome: Lucas Kenji Kikuchi

eleitores = ['111', '222', '333', '444', '555']
votouOuNao = [0, 0, 0, 0, 0]
candidatos = []
# ultimo voto é nulo (len(votosCandidatos) - 1)
votosCandidatos = [0]
fimCadastro = ''
fimVotacao = ''

# cadastro dos candidatos
while True:
    candidatoAtual = input("Número do Candidato ou <fim>:  ")
    if candidatoAtual.lower() == 'fim':
        print("\n")
        break
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
    if eleitores.count(eleitorAtual) == 1:
        print("\nInício do Voto: \n")
        for i in range(len(candidatos)):
            print(f"{candidatos[i]} - Candidato {candidatos[i]}")
        voto = input("\nVoto - Número do Candidato:  ")
        for i in range(len(candidatos)):
            if candidatos[i] == voto:
                votosCandidatos[i]+=1
            elif candidatos.count(voto) == 0:
                votosCandidatos[len(votosCandidatos) - 1]+=1
                break
        # atualiza a lista votouOuNao, indicando se o eleitor votou (1) ou não (0)
        votouOuNao[eleitores.index(eleitorAtual)]+=1


print(votouOuNao)
print(votosCandidatos)
