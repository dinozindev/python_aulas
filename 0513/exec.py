z = 34
x = 0

comando = "x = " + str(z)
print(comando, " O valor de x agora eh ", x)
exec(comando)
print(f"agora o valor de x eh {x}")

comando2 = 'print(f"agora o valor de x eh {x}")'

print(comando2)
exec(comando2)