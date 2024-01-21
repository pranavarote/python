def find_smallest_index(matrix):
    n = len(matrix)

    for k in range(n):
        row_contains_zeros = all(element == '0' for element in matrix[k])
        column_contains_ones = all(matrix[i][k] == '1' for i in range(n))

        if row_contains_zeros and column_contains_ones:
            return k

    return -1

# Read input
n = int(input().strip())
matrix = [input().strip() for _ in range(n)]

# Find and print the smallest index
result = find_smallest_index(matrix)
print(result)
