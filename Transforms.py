from panda3d.core import *
class Transforms:

    @staticmethod
    def opencv_mat_to_lmatrix4f(m):
        if len(m) == 3:
            return LMatrix4f(m[0][0], m[1][0], m[2][0], 0,
                             m[0][1], m[1][1], m[2][1], 0,
                             m[0][2], m[1][2], m[2][2], 0,
                             0, 0, 0, 1)
        else:
            return LMatrix4f(m[0][0], m[1][0], m[2][0], m[3][0],
                             m[0][1], m[1][1], m[2][1], m[3][1],
                             m[0][2], m[1][2], m[2][2], m[3][2],
                             m[0][3], m[1][3], m[2][3], m[3][3])

