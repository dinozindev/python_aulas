numeroFinal = 0
par_impar = ""
int_dec = ""
pos_neg = ""

num1 = input("Numero 1: ")
num1 = float(num1)
num2 = input("Numero 2: ")
num2 = float(num2)

option = input("Qual operação deseja realizar? 1-Adição 2-Subtração 3-Multiplicação 4-Divisão: ")
option = int(option)

if option == 1:
    numeroFinal = num1 + num2
elif option == 2:
    numeroFinal = num1 - num2
elif option == 3:
    numeroFinal = num1 * num2
elif option == 4:
    numeroFinal = num1 / num2

if numeroFinal % 2:
    par_impar = "impar"
else:
    par_impar = "par"

if numeroFinal > 0:
    pos_neg = "positivo"
else:
    pos_neg = "negativo"

if numeroFinal != round(numeroFinal):
    int_dec = "decimal"
else:
    int_dec = "inteiro"

print(f"{numeroFinal} - {par_impar}, {int_dec}, {pos_neg}")