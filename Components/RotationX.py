from Components.RotationMatrix import RotationMatrix
from math import cos, sin


class RotationX(RotationMatrix):

    def __init__(self):
        # default theta 1
        self.rotation_matrix_x = [[1, 0, 0],
                                [0, cos(1), -sin(1)],
                                [0, sin(1), cos(1)]]

    def gen_x_matrix(self, theta: int | float):
        self.rotation_matrix_x[1][1] = cos(theta)
        self.rotation_matrix_x[1][2] = -sin(theta)
        self.rotation_matrix_x[2][1] = sin(theta)
        self.rotation_matrix_x[2][1] = cos(theta)
        return self.rotation_matrix_x
