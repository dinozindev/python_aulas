x = (input("notas: ")).split()
n, s = [], 0 
for i in x: n.append(float(i)) 
for i in range(len(n)): s += n[i]
print(f"média aritmética: {(s / len(n)):.1f}")

# explicação 
# n = notas, s = soma
# 1. recebe notas e splita
# 2. define variáveis notas e soma
# 3. para cada nota, inserir no array notas e transformar em float.
# 4. iterar sobre o array 'notas' com base no total de notas no array, somando em cada iteração a nota ao valor total 'soma'
# 5. dividir a soma total pela quantidade de notas no array, obtendo a média aritmética. 
