import random


class Matrix:

    def __init__(self, matrices_sizes: list):
        self.all_matrices = []

        for matrix_sizes in matrices_sizes:
            rows = matrix_sizes[0]
            columns = matrix_sizes[1]

            if (rows > 0 and columns > 0):
                self.all_matrices.append(self._get_the_matrix(rows, columns))

            else:
                raise BaseException('Sizes must be greater than zero.')

    def _get_the_matrix(self, rows, columns):
        matrix = [
            [random.randint(-10, 10) for column in range(columns)]
            for row in range(rows)
        ]

        return matrix

    def get_multiplication_result(self, rank=None):
        result = []

        if rank:
            # exponentiation of matrices
            for matrix in self.all_matrices:
                matrix2 = matrix

                for i in range(rank):
                    matrix2 = (self._get_multiplication(matrix, matrix2))

                result.append(matrix2)

        else:
            # simple matrix multiplication
            for index in range(1, len(self.all_matrices)):
                result.append(self._get_multiplication(
                    self.all_matrices[index-1], self.all_matrices[index]
                ))

        return result

    def _get_determinant(self, matrix: list) -> int:
        determinant = 0

        if len(matrix) > 1:
            for position, element in enumerate(matrix[0]):
                minor_matrix: list = [
                    row[:position] + row[position + 1:] for row in matrix[1:]
                ]
                minor_determinant: int = element * self._get_determinant(minor_matrix)
                determinant += minor_determinant if (
                        position % 2 == 0 or position == 0
                ) else -minor_determinant

        else:
            determinant: int = matrix[0][0]

        return determinant

    def get_determinants(self):
        result = []

        for matrix in self.all_matrices:
            result.append(self._get_determinant(matrix))

        return result

    def _get_multiplication(self, matrix_a, matrix_b):
        rows_a = len(matrix_a)
        rows_b = len(matrix_b)
        columns_a = len(matrix_a[0])
        columns_b = len(matrix_b[0])

        if rows_a == columns_b and rows_b == columns_a:
            result = []

            for row_a_index, row_a_obj in enumerate(matrix_a):
                result.append([])

                for column_b_index in range(columns_b):
                    temp = 0

                    for row_b_index, element_a in enumerate(row_a_obj):
                        element_b = matrix_b[row_b_index][column_b_index]
                        temp += element_a * element_b

                    result[row_a_index].append(temp)

        else:
            raise BaseException(
                'In order to be able to multiply two matrices, '
                'the number of columns of the first matrix must '
                'be equal to the number of rows of the second matrix.'
            )

        return result

    def _get_transpose(self, matrix):
        result = [[] for i in range(len(matrix[0]))]

        for row in matrix:
            for index, element in enumerate(row):
                result[index].append(element)

        return result

    def get_the_transposed_matrix(self):
        result = []

        for matrix in self.all_matrices:
            result.append(self._get_transpose(matrix))

        return result
