modalidade = input("Informe a modalidade: ")
nome_atleta = input("Nome do atleta: ").title()

notas = []
while True: 
    qtd_notas = int(input(f'Quantidade de tentativas a {modalidade} tem: '))
    # qtd de notas a serem contabilizadas para a media
    qtd_notas_validas = int(input(f"Quantidade de tentativas validas: "))
    media = 0

    if qtd_notas_validas <= qtd_notas:
        for i in range(qtd_notas):
            notas.append(float(input(f"Salto {i+1}: ")))

        # com o [:], deixamos de espelhar o vetor, portanto os valores atualizados de notas nao serao refletidos ao vetor notas_orig
        notas_orig = notas[:]
        notas.sort(reverse=True)

        media = sum(notas[:qtd_notas_validas]) / qtd_notas_validas

        print(f"O atleta {nome_atleta} obteve a média de {media:.2f}")
        for i in range(qtd_notas):
            print(f"Tentativa {i+1}: {notas_orig[i]}")
            break
    else: 
        print("Quantidade de notas validas deve ser menor ou igual a quantidade de tentativas.")
