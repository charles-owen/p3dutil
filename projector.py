from .transforms import Transforms
from panda3d.core import *
import screeninfo
import sys


class Projector:
    """
    Projector support for Panda3D. Supports loading the calibration and
    fullscreen for projection.
    """
    def open_fullscreen(self, p3app, screen_num):
        """
        Open a Panda3D main window fullscreen on a selected
        screen number.
        :param p3app: The Panda3D application class object
        :param screen_num: Screen number, starting at 1
        :return: None
        """
        # get the size of the screen
        monitors = screeninfo.get_monitors()
        if screen_num < 1 or screen_num > len(monitors):
            print(f'Fullscreen: screen {screen_num} is not available')
            return

        screen = screeninfo.get_monitors()[screen_num - 1]
        primary_monitor = self.get_primary_monitor()

        # For this, see https://github.com/rr-/screeninfo/issues/63
        screen_y = primary_monitor.height - (screen.y + screen.height) if sys.platform == "darwin" else screen.y
        screen_x = screen.x

        width, height = screen.width, screen.height

        # Create the Pands3D window fullscreen on the monitor
        props = WindowProperties()
        props.setSize(width, height)
        props.setOrigin(screen_x, screen_y)
        props.setUndecorated(True)
        # props.setMaximized(True)
        p3app.openMainWindow(props=props)

    @staticmethod
    def get_primary_monitor():
        """
        Get the primary monitor using screeninfo
        :return: Primary monitor object
        """
        monitors = screeninfo.get_monitors()
        for monitor in monitors:
            if monitor.is_primary:
                return monitor

        return monitors[0]

    @staticmethod
    def set_projection(p3window, calibration, near, far):
        #
        # Set the projection
        #
        h, w = calibration.imsize
        cam_mat = calibration.matrix
        alpha = cam_mat[0][0]
        beta = cam_mat[1][1]
        x0 = cam_mat[0][2]
        y0 = cam_mat[1][2]

        a = -(near + far)
        b = near * far

        # Create a projection matrix based on the OpenCV
        # camera matrix.
        kgl = LMatrix4f(-alpha, 0, 0, 0,
                        0, -beta, 0, 0,
                        w-x0, h-y0, a, 1,
                        0, 0, b, 0)

        # Create a matrix to convert the OpenCV matrix output
        # to the range -1 to 1 in each dimension, which works
        # like an OpenGL matrix
        ndc = LMatrix4f(-2/w, 0, 0, 0,
                        0, 2/h, 0, 0,
                        0, 0, -2 / (far-near), 0,
                        1, -1, -(far + near) / (far - near), 1)

        proj_mat = kgl * ndc
        ml = MatrixLens()
        ml.setUserMat(proj_mat)
        p3window.cam.node().setLens(ml)

        #
        # Set the view
        #
        t, r = calibration.lastPose()
        rp = Transforms.opencv_mat_to_lmatrix4f(r)
        tm = LMatrix4f.translateMat(t[0][0], t[1][0], t[2][0])

        view = rp * tm
        view.invertInPlace()
        p3window.cam.setMat(view)
