
def loopx(x, y):
    print("entrei", x, y)
    while x < 3:
        if x < 3:
            x += 1
            y += 1
            print("chamando", x, y)
            loopx(x, y)
            print("voltei dentro", x, y)
    print("voltei fora", x, y)
    return(x)

print("chamando", 0, 1)
loopx(0, 1)
print("voltei", 0, 1)