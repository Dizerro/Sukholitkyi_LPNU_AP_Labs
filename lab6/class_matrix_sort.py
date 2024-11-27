class Matrix:
    def __init__(self, data):
        self.data = data

    def sorting_decorator(sorting_enabled=True):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                if sorting_enabled:
                    self.sort_rows_descending()
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

    def sort_rows_descending(self):
        for i in range(len(self.data)):
            self.data[i] = self.bubble_sort_descending(self.data[i])

    @staticmethod
    def bubble_sort_descending(row):
        n = len(row)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if row[j] < row[j + 1]:
                    row[j], row[j + 1] = row[j + 1], row[j]
        return row

    def calculate_fi(self):
        n = len(self.data)
        fi = []
        for col in range(n):
            product = 1
            has_elements = False
            for row in range(n):
                if row + col >= n:
                    product *= self.data[row][col]
                    has_elements = True
            if has_elements:
                fi.append(product)
        return fi

    def calculate_F(self, fi):
        total = 0
        for value in fi:
            total += value
        if len(fi) == 0:
            return 0
        return total / len(fi)

    @sorting_decorator(sorting_enabled=True)
    def compute_results(self):
        fi = self.calculate_fi()
        F = self.calculate_F(fi)
        return fi, F

    def __add__(self, other):
        if isinstance(other, Matrix):
            result = [
                [self.data[i][j] + other.data[i][j] for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Matrix(result)
        raise ValueError("Додавати можна тільки два об'єкти Matrix.")

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

if __name__ == "__main__":
    initial_matrix = [
        [10, 32, 1, -8, -1],
        [2, 4, 91, -82, 96],
        [33, 62, -1, -8, 0],
        [5, -5, 6, -6, 7],
        [-19, 0, 3, -22, -3]
    ]

    matrix = Matrix(initial_matrix)

    print("Початкова матриця:")
    print(matrix)

    fi_values, F_value = matrix.compute_results()

    print("\nВідсортована матриця:")
    print(matrix)

    print("\nfi(aij) для кожного стовпця під допоміжною діагоналлю:")
    print(fi_values)
    print("\nF(fi(aij)) (середнє арифметичне):")
    print(F_value)

    print("\nСума двох матриць:")
    other_matrix = Matrix([[1, 1, 1, 1, 1]] * 5)
    print(matrix + other_matrix)
