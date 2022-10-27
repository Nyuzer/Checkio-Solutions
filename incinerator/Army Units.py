# https://py.checkio.org/en/mission/army-units/

class Soldier:
    def __init__(self, units, name, army):
        self.units = units
        self.name = name
        self.army = army

    def introduce(self):
        info = self.units[self._type], self.name, self.army, self._type
        return "%s %s, %s %s" % info


class Swordsman(Soldier):
    _type = 'swordsman'


class Lancer(Soldier):
    _type = 'lancer'


class Archer(Soldier):
    _type = 'archer'


class Army:
    def train_swordsman(self, name):
        return Swordsman(self.units, name, self.army)

    def train_lancer(self, name):
        return Lancer(self.units, name, self.army)

    def train_archer(self, name):
        return Archer(self.units, name, self.army)


class EuropeanArmy(Army):
    army = 'European'
    units = {'swordsman': 'Knight', 'lancer': 'Raubritter', 'archer': 'Ranger'}


class AsianArmy(Army):
    army = 'Asian'
    units = {'swordsman': 'Samurai', 'lancer': 'Ronin', 'archer': 'Shinobi'}
