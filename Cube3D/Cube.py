from Components.Point import Point
from Components.ProjectionMatrix import ProjectionMatrix
from Components.RotationX import RotationX
from Components.RotationY import RotationY
from Components.RotationZ import RotationZ
from Components.MatrixMath import MatrixMath


class Cube:
    TOTAL_CUBE_POINTS = 8
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCALE = 50

    def __init__(self, point: list[Point]):
        self.projection_matrix = None
        self.point_2d = None
        self.rotation_matrix_z = None
        self.rotation_matrix_y = None
        self.rotation_matrix_x = None
        self.point = point

    def calculate_rotation(self, angle_x: float, angle_y: float, angle_z: float):
        # gen rotation matrices based in theta
        self.rotation_matrix_x = RotationX().gen_x_matrix(angle_x)
        self.rotation_matrix_y = RotationY().gen_y_matrix(angle_y)
        self.rotation_matrix_z = RotationZ().gen_z_matrix(angle_z)
        self.projection_matrix = ProjectionMatrix()

        # gen 2d points for new cube position on 2d plane
        self.point_2d = [0 for elem in range(self.TOTAL_CUBE_POINTS)]

        # loop trough points and calculate rotation and new 2d points
        i = 0
        for point in self.point:
            rotate_x = MatrixMath.multiply_matrix(self.rotation_matrix_x, point.point_3d)
            rotate_y = MatrixMath.multiply_matrix(self.rotation_matrix_y, rotate_x)
            rotate_z = MatrixMath.multiply_matrix(self.rotation_matrix_z, rotate_y)
            point_2d = MatrixMath.multiply_matrix(self.projection_matrix.get_projection_matrix(), rotate_z)
            self.point_2d[i] = self._define_scale_and_position_point(point_2d)
            i += 1
        # print(self.point_2d)
        return self.point_2d

    def _define_scale_and_position_point(self, point_2d: list):
        x = (point_2d[0][0] * self.SCALE) + self.SCREEN_WIDTH / 2
        y = (point_2d[1][0] * self.SCALE) + self.SCREEN_WIDTH / 2   # self.SCREEN_HEIGHT / 2
        return x, y

    def calculate_rotation_single_point(self, x, y, angle_x, angle_y, angle_z):
        # gen rotation matrices based in theta
        self.rotation_matrix_x = RotationX().gen_x_matrix(angle_x)
        self.rotation_matrix_y = RotationY().gen_y_matrix(angle_y)
        self.rotation_matrix_z = RotationZ().gen_z_matrix(angle_z)
        self.projection_matrix = ProjectionMatrix()

        rotate_x = MatrixMath.multiply_matrix(self.rotation_matrix_x, [[x[0], x[1]], [y[0], y[1]], [0, 0]])
        rotate_y = MatrixMath.multiply_matrix(self.rotation_matrix_y, rotate_x)
        rotate_z = MatrixMath.multiply_matrix(self.rotation_matrix_y, rotate_y)
        point_2d = MatrixMath.multiply_matrix(self.projection_matrix.get_projection_matrix(), rotate_z)
        point_2d = self._define_scale_and_position_point(point_2d)
        return point_2d