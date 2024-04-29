a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [6, 7, 8, 9, 10]

for i in b:
    if i not in a:
        a.append(i)

#a.extend(b)

for i in a:
    if i % 2 != 0:
        a.remove(i)

print(a)

a = [1,2,3]
b = [5,6,7]
c = a
c.extend(b)

print(a)
print(b)
print(c)

print("==================")

a = [1,2,3]
b = [5,6,7]
# se nao usamos o ":", o a fica linkado com o c, ou seja, tudo que eh modificado em c, eh modificado tambem em a
# a[start:stop:step]
c = a[:]
c.extend(b)

print(a)
print(b)
print(c)

print("==================")

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# começa na posição 3, vai até a posição 7 (não inclui ela) e pula de 2 em 2
b = a[3:7:2]

print(a)
print(b)

print("=================")

a = [[1,2,3], [4,5,6], [7,8,9]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(f"a[{i}][{j}] = {a[i][j]}")

print("=================")

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sai = ["", "", ""]

print("      0     1     2")
print("   --------------------")
for i in range(len(a)):
    sai[i] = 'print(f"' + str(i) + '  |  '
    for j in range(len(a[i])):
        sai[i] = sai[i] + '{str(a['+ str(i) + '][' + str(j) + '])}  |  '
    sai[i] = sai[i] + '")'
    exec(sai[i])

print("   --------------------")

print("======================================")

a = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 8]]

sai = ["", "", "", "", ""]

print("      0     1     2     3")

for i in range(len(a)):
    sai[i] = 'print(f"' + str(i) + '  |  '
    for j in range(len(a[i])):
        sai[i] = sai[i] + '{str(a['+ str(i) + '][' + str(j) + '])}  |  '
    sai[i] = sai[i] + '")'
    exec(sai[i])

a = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 1], [1, 2, 3, 8]]

sai2 = ["", "", "", "", ""]
sai2[0] = "      0     1     2     3"

for i in range(len(a)):
    sai2[i+1] = str(i) + '  |  '
    for j in range(len(a[i])):
        sai2[i+1] = sai2[i+1] + str(a[i][j]) + '  |  '

for i in range(len(sai2)):
    print(sai2[i])

