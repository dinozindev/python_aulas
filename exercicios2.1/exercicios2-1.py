
# soma duas variaveis inteiras, armazenando o valor em outra variavel.
a = 3
b = 4
soma = a + b

print(f"a soma de {a} + {b} é igual a {soma}")
print("a soma de", a, "+", b, "é igual a", soma)

# armazena o input na variavel.
nome = input("Qual o seu nome?: ")
print(f"O seu nome é {nome}.")

# imprime o tipo.
print(type("Oi"))
print(type(43))
print(type(False))
print(type(4.3))

# recebe dois números, que, a princípio, são strings.
a_str = input("Digite o primeiro número: ")
b_str = input("Digite o segundo número: ")

# transforma os números em string para inteiros.
a_int = int(a_str)
b_int = int(b_str)

# soma dos números
soma = a_int + b_int

print(f"{a_int} + {b_int} = {soma}")

#ao encapsularmos o input com o int, poupamos uma linha, já que logo após o input ser preenchido o valor será convertido em inteiro.
a_str = int(input("Digite um número: "))



