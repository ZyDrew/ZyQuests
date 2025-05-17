class Player:
    def __init__(self, username, level, health, mana, power, inventory):
        self.__username = username
        self.__level = level
        self.__health = health
        self.__mana = mana
        self.__power = power
        self.__inventory = inventory

    def get_username(self):
        return self.__username
    def get_level(self):
         return self.__level
    def get_health(self):
        return self.__health
    def get_mana(self):
        return self.__mana
    def get_power(self):
        return self.__power
    def get_inventory(self):
        return self.__inventory
    
    def take_damage(self, damage):
        self.__health -= damage

    def __repr__(self):
        pass
    
