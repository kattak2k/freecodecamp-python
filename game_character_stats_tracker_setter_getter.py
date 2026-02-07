class GameCharacter:

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("'name' should be of type string")
        if not isinstance(health, int) or not isinstance(mana, int) or not isinstance(level, int):
            raise TypeError("'health', 'mana' and 'level' should be of type integer")

        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    def __str__(self):
        return f'Name: {self.name}\n Level: {self.health}\n Health: {self.mana}\n Mana: {self.level}'

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if not (new_health < 0 or new_health > 100):
            raise ValueError(f"Invalid input 'health' {new_health} should be between 0 and 100")
        self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if not (new_mana < 0 or new_mana > 50):
            raise ValueError(f"Invalid input 'mana' {new_mana} should be between 0 and 50")
        self._mana = new_mana    

    @property
    def level(self):
        return self._level

kratos = GameCharacter('Kratos')
print(kratos)
