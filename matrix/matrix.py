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

    def _get_the_matrix(self, rows: int, columns: int) -> list:
        matrix = [
            [random.randint(-10, 10) for column in range(columns)]
            for row in range(rows)
        ]

        return matrix

    def get_determinants(self) -> list:
        result = []

        for matrix in self.all_matrices:
            result.append(self._get_determinant(matrix))

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

    def get_multiplication_result(self, rank=None) -> list:
        result = []

        if rank:
            # exponentiation of matrices
            for matrix in self.all_matrices:
                matrix2: list = matrix

                for i in range(rank):
                    matrix2: list = (
                        self._get_multiplication(matrix, matrix2)
                    )

                result.append(matrix2)

        else:
            # simple matrix multiplication
            for index in range(1, len(self.all_matrices)):

                if result:
                    parameters: tuple = (
                        result.pop(),
                        self.all_matrices[index]
                    )

                else:
                    parameters: tuple = (
                        self.all_matrices[index-1],
                        self.all_matrices[index]
                    )

                result.append(
                    self._get_multiplication(*parameters)
                )

        return result

    def _get_multiplication(self, matrix_a: list, matrix_b: list):
        rows_a: int = len(matrix_a)
        rows_b: int = len(matrix_b)
        columns_a: int = len(matrix_a[0])
        columns_b: int = len(matrix_b[0])

        if rows_a == columns_b and rows_b == columns_a:
            result = []

            for row_a_index, row_a_obj in enumerate(matrix_a):
                result.append([])

                for column_b_index in range(columns_b):
                    temporary_element = 0

                    for row_b_index, element_a in enumerate(row_a_obj):
                        element_b = matrix_b[row_b_index][column_b_index]
                        temporary_element += element_a * element_b

                    result[row_a_index].append(temporary_element)

        else:
            raise BaseException(
                'In order to be able to multiply two matrices, '
                'the number of columns of the first matrix must '
                'be equal to the number of rows of the second matrix.'
            )

        return result

    def get_the_transposed_matrix(self):
        result = []

        for matrix in self.all_matrices:
            result.append(self._get_transpose(matrix))

        return result

    def _get_transpose(self, matrix):
        result = [[] for i in range(len(matrix[0]))]

        for row in matrix:
            for index, element in enumerate(row):
                result[index].append(element)

        return result

    def get_inverse_matrix(self) -> list:
        result = []

        for matrix in self.all_matrices:
            result.append(self._get_inverse(matrix))

        return result

    def _get_inverse(self, matrix: list) -> list:
        """
        The inverse matrix is obtained by the Gaussian Jordan method.
        :param matrix:
        :return:
        """
        matrix_size = len(matrix)
        inverse_matrix = [
            [0 if column != row else 1 for column in range(matrix_size)]
            for row in range(matrix_size)
        ]

        for main_index in range(matrix_size):
            # Transposition matrix rows so
            # that the main element is not equal to zero.
            for i in range(main_index, matrix_size):
                main_element: int = matrix[main_index][main_index]

                if main_element == 0:
                    row: list = matrix.pop(main_index)
                    inverse_row: list = inverse_matrix.pop(main_index)
                    matrix.append(row)
                    inverse_matrix.append(inverse_row)

                else:
                    coefficient = 1 / main_element
                    break

            else:
                # inverse matrix doesn't exists. Because of zero column.
                inverse_matrix = [ [ None ] ]
                break
            # Turn main element of base matrix to 1.
            # It's affect another elements of row (both matrix).
            for element_index in range(matrix_size):
                matrix[main_index][element_index] *= coefficient
                inverse_matrix[main_index][element_index] *= coefficient

            for nullable_row_index in range(matrix_size):

                if nullable_row_index == main_index:
                    continue

                nullable_coefficient: int = matrix[nullable_row_index][main_index]
                for nullable_element_index in range(matrix_size):
                    matrix[nullable_row_index][nullable_element_index] -= (
                        matrix[main_index][nullable_element_index]
                        * nullable_coefficient
                    )
                    inverse_matrix[nullable_row_index][nullable_element_index] -= (
                        inverse_matrix[main_index][nullable_element_index]
                        * nullable_coefficient
                    )

        return inverse_matrix
