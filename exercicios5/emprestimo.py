# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorCasa = float(input("Qual o valor da casa?: "))
salario = float(input("Qual o salario?: "))
anos = int(input("Qual a quantidade de anos a pagar?: ")) 
juros = float(input("Qual o valor do juros mensal?: "))
juros = 1 + (juros / 100)

meses = anos * 12
juros_total = juros ** meses

valor_juros = valorCasa * juros_total

prestacao = valor_juros / meses

print(valorCasa)
print(valor_juros)
print(salario)
print(anos)
print(meses)
print(juros)
print(juros_total)
print(prestacao)
print(salario * 0.3)

if prestacao == salario * 0.3:
    print("N empresta")
else:
    print("empresta")
