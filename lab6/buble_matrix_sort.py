matrix = [
    [10, 32, 1, -8, -1],
    [2, 4, 91, -82, 96],
    [33, 62, -1, -8, 0],
    [5, -5, 6, -6, 7],
    [-19, 0, 3, -22, -3]
]

def bubble_sort_descending(row):
    n = len(row)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if row[j] < row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]
    return row

sorted_matrix = [bubble_sort_descending(row) for row in matrix]

print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

def calculate_fi(matrix):
    n = len(matrix)
    fi = []
    for col in range(n):  
        product = 1
        has_elements = False
        for row in range(n):
            if row + col >= n:  
                product *= matrix[row][col]
                has_elements = True
        if has_elements:
            fi.append(product)
    return fi

def calculate_F(fi):
    if len(fi) == 0:
        return 0 
    total = 0
    for value in fi:
        total += value
    return total / len(fi)

fi_values = calculate_fi(sorted_matrix)
F_value = calculate_F(fi_values)

print("\nfi(aij) для кожного стовпця під допоміжною діагоналлю:")
print(fi_values)

print("\nF(fi(aij)) (середнє арифметичне):")
print(F_value)
