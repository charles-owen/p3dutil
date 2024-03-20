from .NodePathUser import NodePathUser
from direct.actor.Actor import Actor
from panda3d.core import *

class ActorUser(NodePathUser):
    def __init__(self, actor: Actor, p: LVector3 = None, mat: LMatrix4 = None, parent:NodePath=None):
        super().__init__(actor, p=p, mat=mat, parent=parent)
        self._actor = actor


    @property
    def actor(self) -> Actor:
        """
        Actor property - gets the actor we are using
        :return:
        """
        return self._actor
