# 1. Dado um número pelo usuário, calcular o dobro.

num = input("Digite um número: ")
num = float(num)
dobro = num * 2
print(f"O dobro de {num} é {dobro}")

# 2. Dado um número pelo usuário, calcular o quadrado.

num = input("Digite um número: ")
num = float(num)
quad = num ** 2
print(f"O quadrado de {num} é {quad}")

# 3. Dado um número pelo usuário, exibir o anterior e posterior.

num = input("Digite um número: ")
num = int(num)
prev = num - 1
next = num + 1
print(f"{prev} é o anterior, {num} é o atual e {next} é o próximo.")

# 4. Dados dois números pelo usuário, calcular a potência.

base = input("Digite a Base: ")
base = int(base)
exp = input("Digite o Expoente: ")
exp = int(exp)
resultado = base ** exp
print(f"{base} elevado a {exp} é igual a {resultado}")

# 5. Dado um número pelo usuário, exibir o próximo múltiplo de 5

num = input("Digite um número: ")
num = int(num)
prox_mult_5 = num // 5 * 5 + 5
print(f"O próximo múltiplo de 5 de {num} é {prox_mult_5}")

