import p3dutil as pu
from panda3d.core import *


class Axis(pu.NodePathUser):
    """
    Simple class to display a coordinate axis
    """

    def __init__(self, p: LVector3f = None, mat: LMatrix4 = None, size=10, thickness=3,
                 parent: NodePath = None, axis=LVector3f(1, 1, 1)):
        """
        Constructor
        :param p: Position to display the coordinate axis
        :param mat: Matrix to place the coordinate axis (optional)
        :param size: Size of the axis (total width, height, depth, default=10)
        :param thickness: Line thickness (default=3)
        :param parent: Optional parent to set for the node
        """
        lines = LineSegs()
        lines.setThickness(thickness)
        lines.setColor(LVecBase4f(1, 0, 0, 1))
        lines.moveTo(0, 0, 0)
        lines.drawTo(axis[0] * size, 0, 0)

        lines.setColor(LVecBase4f(0, 1, 0, 1))
        lines.moveTo(0, 0, 0)
        lines.drawTo(0, axis[1] * size, 0)

        lines.setColor(LVecBase4f(0, 0, 1, 1))
        lines.moveTo(0, 0, 0)
        lines.drawTo(0, 0, axis[2] * size)

        node = lines.create(False)
        np = NodePath(node)
        super().__init__(np, parent=parent, p=p, mat=mat)
