from Components.RotationMatrix import RotationMatrix
from math import cos, sin


class RotationZ(RotationMatrix):

    def __init__(self):
        # default theta 1
        self.rotation_matrix_z = [[cos(1), -sin(1), 0],
                                  [sin(1), cos(1), 0],
                                  [0, 0, 1]]

    def gen_z_matrix(self, theta: int | float):
        self.rotation_matrix_z[0][0] = cos(theta)
        self.rotation_matrix_z[0][1] = -sin(theta)
        self.rotation_matrix_z[1][0] = sin(theta)
        self.rotation_matrix_z[1][1] = cos(theta)
        return self.rotation_matrix_z
