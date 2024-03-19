num = input("Numero: ")
num = float(num)

if num != round(num):
    print("Numero eh decimal")
else:
    print("Numero eh inteiro")