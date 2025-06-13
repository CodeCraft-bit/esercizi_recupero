def sum_primary_diagonal(matrix) -> int:
    somma = 0
    somma2 = 0
    if len(matrix)==len(matrix[0]):
        for i in range(len(matrix)):
            somma += matrix[i][i]
        return somma
    elif len(matrix)!=len(matrix[0]):
        righe = len(matrix)
        colonne = len(matrix[0])
        for i in range(min(righe, colonne)):
            somma2 += matrix[i][i]
        return somma2

mat1: list[list] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
somma1 = sum_primary_diagonal(mat1)
print(somma1)

mat2: list[list] = [
    [1, 2, 3],
    [4, 5, 6]
]
somma2 = sum_primary_diagonal(mat2)
print(somma2)

def sum_secondary_diagonal(matrix) -> int:
    somma = 0
    somma2 = 0
    if len(matrix)==len(matrix[0]):
        for i in range(len(matrix)):
            somma += matrix[i][len(matrix[0]) - 1 - i]
        return somma
    elif len(matrix)!=len(matrix[0]):
        righe = len(matrix)
        colonne = len(matrix[0])
        for i in range(min(righe, colonne)):
            somma2 += matrix[i][colonne -1 -i]
        return somma2
    
mat3: list[list] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
somma3 = sum_secondary_diagonal(mat3)
print(somma3)

mat4: list[list] = [
    [1, 2, 3],
    [4, 5, 6]
]
somma4 = sum_secondary_diagonal(mat4)
print(somma4)

