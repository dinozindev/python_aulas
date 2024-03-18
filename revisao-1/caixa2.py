
valor = input("saque: ")
valor = float(valor) 

# notas disponíveis
qi50 = 3
qi20 = 5
qi10 = 10

# notas dadas no saque
q50 = 0
q20 = 0
q10 = 0

# total notas de 50 que podem ser utilizadas dado valor. 
q50 = int(valor // 50)

# se a quantidade de notas for maior que a disponível no caixa, a quantidade de notas de 50 que utilizaremos será igual ao total no caixa. 
# reduzimos o valor das notas de 50 do valor total, e passamos para o próximo. 
# caso tenhamos notas suficientes, o valor será o resto da divisão por 50, ou seja, o valor que restou da subtração das notas de 50. 
if q50 > qi50:
    print("entrei 50: ", q50, qi50)
    q50 = qi50
    valor = valor - (q50 * 50)
    print(valor)
else:
    valor = valor % 50
 

# obtém o total de notas de 20 que podem ser usadas dado valor. 
q20 = int(valor // 20)

if q20 > qi20:
    print("entrei 20: ", q20, qi20)
    q20 = qi20
    valor = valor - (q20 * 20)
    print(valor)
else:
    valor = valor % 20

# obtém o total de notas de 10 que podem ser usadas dado valor. 
q10 = int(valor // 10)

# caso tenhamos menos notas de 10 do que as necessárias, isso significa que não temos valor suficiente para cobrir o valor que foi nos dado. 
if q10 > qi10:

    print("valor não possível")

else:

    print(f"Nota 50: {q50} \nNota 20: {q20} \nNota 10: {q10}")