# Pokemon Code Academy Project
# Written by Jeff Dorfman 6/12/20
# This is a sample project from code academy, w00t!


class Pokemon():
    def __init__(self, name, type_element, current_health=None, level=0, max_health=None, awake=True):
        self.name = name
        self.level = level
        self.type_element = type_element
        self.awake = awake

        if max_health == None:
            self.max_health = 100
        else:
            self.max_health = max_health

        if current_health == None:
            self.current_health = self.max_health
        else:
            self.current_health = current_health

        return

    def attack(self, other, attack):
        other.lose_health(attack)
        print(f'{self.name} attacked {other.name} for {attack} points of damage!')
        return

    def lose_health(self, attack):
        self.current_health = self.current_health - attack
        if self.current_health <= 0:
            self.knock_out()

        print(f'{self.name} now has {self.current_health} health')
        return

    def gain_health(self, heal):
        if self.current_health == 0:
            self.revive()
        self.current_health = self.current_health + heal

        print(f'{self.name} now has {self.current_health} health')
        return

    def revive(self):
        if self.current_health == 0:
            self.current_health = 1

        self.awake = True
        print(f'{self.name} has been revived.')
        return

    def knock_out(self):
        self.current_health = 0
        self.awake = False
        print(f'{self.name} has been knocked out!!')
        return

    def __repr__(self):
        return f'''
    Name: {self.name}
    HP: {self.current_health}/{self.max_health}
    LVL: {self.level}
    Type: {self.type_element}
    Awake: {self.awake}
    '''


mewtwo = Pokemon('Mewtwo', 'Psychic')
bulbasaur = Pokemon('Bulbasaur', 'Seed')
