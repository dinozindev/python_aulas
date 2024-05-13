def resto(a,b):
    return(a % b)

def inteira(a, b):
    return(a // b)

a = 5
b = 3

comando = "c = inteira(a, b) + resto(a, b)"
print(comando)
exec(comando)
print(c)

