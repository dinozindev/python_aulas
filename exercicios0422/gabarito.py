# exercicio 1

n1 = float(input("Valor 1: "))
n2 = float(input("Valor 2: "))
operacao = input("Qual a operação? (+ - * /): ")

if operacao == '+':
    print(n1 + n2)
elif operacao == '-':
    print(n1 - n2)
elif operacao == '*':
    print(n1 * n2)
elif operacao == '/':
    print(n1 / n2)


# exercicio 2 
x = int(input("Valor x: "))
y = int(input("Valor y: "))

xo = x
n = 0
if xo > y:
    while xo >= y:
        xo-=y
        n+=1

print(f"{x} / {y} = {n} com resto {xo}")

# exercicio 3 

x = int(input("Número primo ou não: "))

n = 3
if x >= 3:
    while x % n != 0:
        n+=2

if n == x:
    print("primo")
else:
    print("não é primo")

# imprime todos os primos entre 0 e 1000
for x in range(1000):
    n = 3
    if (x > 3) and (x % 2 != 0):
        while(x % n != 0):
            n+=2
    if n == x or x == 2 or x == 1:
        print(x)

# exercicio 4

x = input("Escreva uma frase: ")
y = {}
for i in x:
    if y.get(i):
        y[i] += 1
    else:
        y[i] = 1
    
print(y)

