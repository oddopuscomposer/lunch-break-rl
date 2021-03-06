import registry

from ai.actions import throwaction
from entities.items import weapon


class Glove(weapon.Weapon):
    def __init__(self, char='g', position=(0, 0)):
        super().__init__(char, position)

        self.name = 'glove'
        self.verb = 'throws'
        self.throw_distance = 5

    def get_perform_action(self, requester, target):
        return throwaction.ThrowAction(requester, target)

    def get_special_action(self, requester, target):
        return throwaction.ThrowAction(requester, target)
