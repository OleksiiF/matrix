from matrix.matrix import Matrix


def personal_print(obj_for_print):
    for matrix in obj_for_print:
        for row in matrix:
            for element in row:
                print("{0: ^4}".format(element), end=' ')
            print('\n', end='')
        print('=' * 40)


def main():
    matrices_sizes = [[4,4], [4,4]]
    matrix_obj = Matrix(matrices_sizes)
    personal_print(matrix_obj.all_matrices)
    personal_print(matrix_obj.get_the_transposed_matrix())
    personal_print(matrix_obj.get_multiplication_result(10))


if __name__ == '__main__':
    main()
