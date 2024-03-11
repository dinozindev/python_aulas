# informar quantia e quantas cedulas de cada existem, informando por fim se eh possivel retornar ou nao o valor atraves das cedulas disponiveis.

quantia = 0.0
ced100 = 0
ced50 = 0
ced20 = 0
ced10 = 0
problema = 0

# enquanto houver resto na divisão da quantia por dez, isso significa que notas menores que 10 estão sendo utilizadas. Portanto, é necessário repetir a chamada de input. 
while quantia % 10:
    quantia = input("quantia: ")
    quantia = float(quantia)

    ced100 = quantia // 100
    quantia = quantia (ced100 * 100)

# verifica quantidade de cedulas de 50, removendo o valor total das cedulas de 50. 
    ced50 = quantia // 50
    quantia = quantia (ced50 * 50)

# verifica quantidade de cedulas de 20, removendo o valor total das cedulas de 20. 
    ced20 = quantia // 20
    quantia = quantia (ced20 * 20)

# verifica quantidade de cedulas de 10.
    ced10 = quantia // 10

    print(f"50 - {ced50}  20 - {ced20}  10 - {ced10}")