# https://py.checkio.org/en/mission/the-warriors/


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7

    @property
    def is_alive(self):
        return self.health > 0


def fight(unit_1, unit_2):
    result = 0
    while True:
        unit_2.health -= unit_1.attack
        if unit_2.health <= 0:
            result = True
            break
        unit_1.health -= unit_2.attack
        if unit_1.health <= 0:
            result = False
            break

    return result
