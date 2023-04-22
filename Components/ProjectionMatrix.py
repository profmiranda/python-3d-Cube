class ProjectionMatrix:
    # projection matrix rows
    n = 3
    # projection matrix columns
    m = 3

    def __init__(self):
        # 3d to 2d
        self.projection_matrix = self._gen()

    @classmethod
    def _gen(cls):
        val: list = [0] * cls.n
        # print(val)
        for x in range(cls.n):
            val[x] = [0] * cls.m
            if x == 0:
                val[x][0] = 1
            elif x == 1:
                val[x][1] = 1
        # print(val)
        return val

    def get_projection_matrix(self):
        return self.projection_matrix
