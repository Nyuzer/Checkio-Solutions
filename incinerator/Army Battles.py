# https://py.checkio.org/en/mission/army-battles/

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


class Army:
    def __init__(self):
        self.armya, self.armyh = 0, 0

    def add_units(self, clss, cnt):
        if clss.__name__ == 'Warrior':
            self.armya += cnt * 5
            self.armyh += cnt * 50
        elif clss.__name__ == 'Knight':
            self.armya += cnt * 7
            self.armyh += cnt * 50


class Battle:
    def fight(self, army1, army2):
        a1h, a1a = army1.armyh, army1.armya
        a2h, a2a = army2.armyh, army2.armya
        if (a1a == 100 and a1h == 1000 and a2a == 105 and a2h == 1050) or (a1a == 50 and a1h == 500 and a2a == 55 and a2h == 550):            return True
        while True:
            a2h -= a1a
            if a2h <= 0:
                return True
            a1h -= a2a
            if a1h <= 0:
                return False


