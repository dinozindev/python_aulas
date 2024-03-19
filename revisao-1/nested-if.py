x = input("Numero1: ")
x = float(x)
y = input("Numero2: ")
y = float(y)

if x > y:
    print("x maior que y")
    if x > 5:
        print("x maior que 5")
    else: 
        print("x menor que 5")
elif y > x:
    print("y maior que x")
    if y > 10:
        print("y maior que 10")
        if y > 20:
            print("y maior que 20")
        else:
            print("y menor que 20")
    else:
        print("y menor que 10")
else:
    print("x igual a y")