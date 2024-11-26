def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

result_1 = get_matrix(3, 2, 'Yes')
result_2 = get_matrix(6, 4, False)
result_3 = get_matrix(7, 7, 4)
print(result_1)
print(result_2)
print(result_3)