valor = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o salario?: "))
juros = float(input("Qual o valor do juros mensal?: "))
prestacao = salario * 0.3
juros = 1 + (juros / 100)



if prestacao > valor * (juros - 1):
    valor_residual = valor - prestacao
    meses = 1
    print(valor_residual)

    while valor_residual > 0:
        valor_residual = valor_residual * juros
        print(valor_residual, 'juros')
        valor_residual = valor_residual - prestacao
        print(valor_residual, 'prestacao')
        meses+=1
    
    print(meses, meses / 12)
else:
    print("Salario insuficiente")