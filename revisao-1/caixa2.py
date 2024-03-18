
valor = input("saque: ")

valor = float(valor)
 
qi50 = 3

qi20 = 5

qi10 = 10
 
q50 = 0

q20 = 0

q10 = 0
 
q50 = int(valor // 50)
 
if q50 > qi50:

    print("entrei 50: ", q50, qi50)

    q50 = qi50

    valor = valor - (q50 * 50)

    print(valor)

else:

    valor = valor % 50
 
q20 = int(valor // 20)

if q20 > qi20:

    print("entrei 20: ", q20, qi20)

    q20 = qi20

    valor = valor - (q20 * 20)

    print(valor)

else:

    valor = valor % 20
 
q10 = int(valor // 10)
 
if q10 > qi10:

    print("valor não possível")

else:

    print(f"Nota 50: {q50} \nNota 20: {q20} \nNota 10: {q10}")