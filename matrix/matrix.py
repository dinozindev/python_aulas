matrix1 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

matrix2 = [[row[i] for row in matrix1] for i in range(4)]
# matriz 2 
# [[1, 5, 9], 
# [2, 6, 10], 
# [3, 7, 11], 
# [4, 8, 12]]

matrix_final = []
# a partir da primeira linha da primeira matriz, itera sobre os elementos de cada coluna da segunda matriz, multiplicando, e assim por diante. Ex: 1*1 + 2*2 + 3*3 + 4*4 = 30
# loop de cada linha da primeira matriz
for j in range(3):
    print(f'entra linha {j} da matriz 1')
    row_matrix = []
    # loop de cada elemento de cada row da segunda matriz
    for k in range(3):
        elemento = 0
        # loop de cada elemento de cada row da primeira matriz
        for i in range(4):
            elemento+=matrix1[j][i]*matrix2[i][k]
        row_matrix.append(elemento)
        print(row_matrix)
    matrix_final.append(row_matrix)

print(matrix_final)
