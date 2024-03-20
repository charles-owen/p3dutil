import p3dutil as pu
from panda3d.core import *

class Lines(pu.NodePathUser):
    """
    Simple class to display a coordinate axis
    """

    def __init__(self, p: LVector3f = None, mat: LMatrix4 = None, size=10, thickness=3,
                 parent: NodePath = None):
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
        lines.drawTo(0, 0, 0)
        self._lines = lines

        # lines.setColor(LVecBase4f(0, 1, 0, 1))
        # lines.moveTo(0, 0, 0)
        # lines.drawTo(0, size, 0)
        #
        # lines.setColor(LVecBase4f(0, 0, 1, 1))
        # lines.moveTo(0, 0, 0)
        # lines.drawTo(0, 0, size)
        #
        node = lines.create(False)
        np = NodePath(node)
        super().__init__(np, parent=parent, p=p, mat=mat)

    def line(self, fm: LVector3, to: LVector3, size=10, thickness=3, color=LVector4f(1, 1, 1, 1)):
        lines = LineSegs()
        lines.setThickness(thickness)
        lines.setColor(color)
        lines.moveTo(fm)
        lines.drawTo(to)

        node = lines.create(False)
        self.node.attachNewNode(node)

