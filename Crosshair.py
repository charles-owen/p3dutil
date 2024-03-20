import p3dutil as pu
from panda3d.core import *


class Crosshair(pu.NodePathUser):
    """
    Simple class to display a crosshair
    """
    def __init__(self, p: LVector3f = None, size=10, thickness=3,
                 color: LVector4f = LVector4f(1, 0, 0, 1), parent: NodePath = None):
        """
        Constructor
        :param p: Position to display the crosshair
        :param size: Size of the crosshair (total width, height, depth, default=10)
        :param thickness: Line thickness (default=3)
        :param color: Color to draw the crosshair (default=red)
        :param parent: Optional parent to set for the node
        """
        lines = LineSegs()
        lines.setThickness(thickness)
        lines.setColor(color)
        lines.moveTo(-size / 2, 0, 0)
        lines.drawTo(+size / 2, 0, 0)
        lines.moveTo(0, -size / 2, 0)
        lines.drawTo(0, +size / 2, 0)
        lines.moveTo(0, 0, -size / 2)
        lines.drawTo(0, 0, +size / 2)

        node = lines.create()
        np = NodePath(node)
        super().__init__(np, parent=parent, p=p)


