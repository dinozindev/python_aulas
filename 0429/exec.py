x = input("Digite x: ")
y = input("Digite y: ")
o = input("Digite a operação: ")

c = "r = " + x + o + y
exec(c)
print(f"Resultado de {x} {o} {y} = {r}")

print("antes: ", r)
if r:
    print("dentro: ", r)