from classes.player import Player

class Elf(Player):
    def __init__(self, username, level, health, mana, power, inventory, perception):
        super().__init__(username, level, health, mana, power, inventory)
        self.__perception = perception

    def get_perception(self):
        return self.__perception