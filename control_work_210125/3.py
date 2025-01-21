def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()
def transposed(matrix):
    matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return matrix

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

import random
n = int(input())
matrix = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
print("Начальная матрица: ")
print_matrix(matrix)
matrix = transposed(matrix)
for row in range(len(matrix)):
    matrix[row] = merge_sort(matrix[row])
matrix = transposed(matrix)
print("Конечная матрица: ")
print_matrix(matrix)