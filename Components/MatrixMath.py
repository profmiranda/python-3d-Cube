from Components.Point import Point
from Lib.StringHelper import StringHelper
from typing import Type


class MatrixMath:

    # https://docs.python.org/3/library/typing.html#typing.Type
    @classmethod
    def multiply_matrix(cls, matrix_a: Type[list | list[list]], matrix_b: Type[list | list[list]]):
        """ This function needs the matrices A and B parameters in
        proper order. It is not smart enough to try both ways"
        """
        matrix_a_rows = len(matrix_a)
        matrix_a_columns = len(matrix_a[0])
        matrix_b_rows = len(matrix_b)
        matrix_b_columns = len(matrix_b[0])

        # Dot product: matrix_a_cols == matrix_b_rows
        # initiates matrix with all 0s. Matrix multiplication results in a new
        # matrix with the rows of A and columns of B
        # In order for matrix multiplication to be defined, the number of columns in the first
        # matrix must be equal to the number of rows in the second matrix.
        if matrix_a_columns == matrix_b_rows:
            # Dot product matrix dimensions = matrix_a_rows x matrix_b_columns
            product = [[0 for col in range(matrix_b_columns)]
                       for row in range(matrix_a_rows)]
            # row by column
            for row_a in range(matrix_a_rows):
                for column_b in range(matrix_b_columns):
                    for row_b in range(matrix_b_rows):
                        # if row_b < matrix_b_rows - 1:
                        product[row_a][column_b] += matrix_a[row_a][row_b] * matrix_b[row_b][column_b]
            return product
        return None

    multiply_matrix.__doc__ = "This function needs the matrices A and B parameters in" \
                              " proper order. It is not smart enough to try both ways"
