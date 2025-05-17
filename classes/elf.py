from classes.player import Player

class Elf(Player):
    def __init__(self, username, level, health, mana, power, inventory, perception):
        super().__init__(username, level, health, mana, power, inventory)
        self.__perception = perception

    def get_perception(self):
        return self.__perception
    
    def __repr__(self):
        return f"""
Name        : {self.get_username()} 
Class       : Elf
Health      : {self.get_health()}
Mana        : {self.get_mana()}
Power       : {self.get_power()}
Perception  : {self.get_perception()}
"""