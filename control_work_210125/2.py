import random
def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()

n = int(input())
matrix = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
print("Начальная матрица: ")
print_matrix(matrix)
enter = int(input("Выберите сдвиг: "))

for lst in range(len(matrix)):
    matrix[lst] = matrix[lst][-enter:] + matrix[lst][:-enter]

print("Конечная матрица: ")
print_matrix(matrix)