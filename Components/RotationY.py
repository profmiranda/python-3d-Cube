from Components.RotationMatrix import RotationMatrix
from math import cos, sin


class RotationY(RotationMatrix):

    def __init__(self):
        # default theta 1
        self.rotation_matrix_y = [[cos(1), 0, sin(1)],
                                  [0, 1, 0],
                                  [-sin(1), 0, cos(1)]]

    def gen_y_matrix(self, theta: int | float):
        self.rotation_matrix_y[0][0] = cos(theta)
        self.rotation_matrix_y[0][2] = sin(theta)
        self.rotation_matrix_y[2][0] = -sin(theta)
        self.rotation_matrix_y[2][2] = cos(theta)
        return self.rotation_matrix_y
