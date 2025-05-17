class Monster:
    def __init__(self, name, health, power):
        self.__name = name
        self.__health = health
        self.__power = power

    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_power(self):
        return self.__power
        