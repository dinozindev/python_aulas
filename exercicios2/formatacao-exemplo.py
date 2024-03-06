# Formatação com modificadores.

nome = "Edson"
print(f"{nome:>10s}")
print(f"{nome:0>10s}")
print(f"{nome:<10s}")
print(f"{nome:0<10s}")
print(f"{nome:^10s}")
print(f"{nome:0^10s}")

num = 23
print(f"{num:>5d}")
print(f"{num:0>5d}")
print(f"{num:0<5d}")
print(f"{num:0^5d}")

nome = "Carlos Dionisio"
nome_formatado = '{:@>40}'.format(nome)
print(nome_formatado)
nome_formatado = '{:$<40}'.format(nome)
print(nome_formatado)
nome_formatado = '{:*^40}'.format(nome)
print(nome_formatado)

nome = "Michael Jackson"
tamanho = len(nome)
maiusculas = nome.upper()
minusculas = nome.lower()
iniciais = nome.title()
