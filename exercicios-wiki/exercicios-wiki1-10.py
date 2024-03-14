# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello, World!")

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
a = int(input("Digite um número: "))
print(f"O número informado foi [{a}]")

# 3. Faça um Programa que peça dois números e imprima a soma.
a = int(input("Type a number: "))
b = int(input("Type another number: "))

soma = a + b

print(f"{a} + {b} = {soma}")

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"media = {media}")

# 5. Faça um Programa que converta metros para centímetros.

metros = float(input("Type a number in meters: "))
cm = metros * 100

print(f"{metros} meters in centimeters: {cm}cm")

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Type the radius of the circle: "))
area = 3.14 * (raio ** 2)

print(f"a área do círculo de raio {raio} é igual a {area} centimetros quadrados")

# 7. Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

lado = 4

areaQuadrado = lado ** 2
dobro = areaQuadrado * 2

print(f"o dobro da área do quadrado de lado {lado} é igual a {dobro}")

# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhoHora = float(input("Ganho por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas por mês: "))

ganhoTotal = ganhoHora * horasTrabalhadas

print(f"Ganho por mês: {ganhoTotal} reais")

# 9. Faça um programa que peça a temperatura em graus Fahrenheit, transforme a temperatura em graus Celsius.

tempFahrenheit = int(input("Temperatura em Fahrenheit: "))
tempCelsius = 5 * ((tempFahrenheit - 32) / 9)
round(tempCelsius, 1)

print(f"Temperatura em graus Celsius: {tempCelsius} graus Celsius")

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

tempCelsius = int(input("Temperatura em Celsius: "))
tempFahrenheit = (tempCelsius * 1.8) + 32
round(tempFahrenheit, 1)

print(f"Temperatura em Fahrenheit: {tempFahrenheit}F")