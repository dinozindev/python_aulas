# Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

# Observando os termos no plural a colocação do "e", da vírgula entre outros.

# Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades

# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

cent = 0
dez = 0
uni = 0

num = input("Número maior que 0 e menor que 1000: ")
num = int(num)

while num < 0 and num > 1000:
    num = input("Número maior que 0 e menor que 1000: ")
    num = int(num)

initialNum = num
cent = num // 100
num = num - cent * 100

dez = num // 10
num = num - dez * 10

uni = num

print(f"{initialNum} = {cent} centenas, {dez} dezenas e {uni} unidades")

