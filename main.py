def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def sum_of_negative_elements_in_column(matrix, column_index):
    return sum(row[column_index] for row in matrix if row[column_index] < 0)

def find_column_with_min_sum(matrix):
    min_sum = float('inf')
    min_column_index = -1
    for column_index in range(len(matrix[0])):
        column_sum = sum_of_negative_elements_in_column(matrix, column_index)
        if column_sum < min_sum:
            min_sum = column_sum
            min_column_index = column_index
    return min_column_index, min_sum

def get_column(matrix, column_index):
    return [row[column_index] for row in matrix]

# Основная логика программы
file_path = 'ekzo.txt'
matrix = read_matrix_from_file(file_path)

min_column_index, min_sum = find_column_with_min_sum(matrix)
min_column = get_column(matrix, min_column_index)

print(f"Минимальная сумма отрицательных элементов в столбце {min_column_index}: {min_sum}")
print(f"Элементы {min_column_index} столбца: {min_column}")