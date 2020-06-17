# Pokemon Code Academy Project
# Written by Jeff Dorfman 6/12/20
# This is a sample project from code academy, w00t!

# DATABASE

advantage_table = {
    'Fire': ['Grass', 'Seed'],
    'Water': ['Fire'],
    'Grass': ['Water', 'Seed'],
    'Seed': ['Water'],
    'Psychic': ['Water', 'Fire', 'Grass', 'Seed']
}


# CLASSES

class Trainer():
    def __init__(self, name, potions=[], pokemon=[], current_pokemon=None):
        self.name = name
        self.potions = potions
        self.pokemon = pokemon
        if self.pokemon != []:
            self.current_pokemon = self.pokemon[0]
        else:
            self.current_pokemon = current_pokemon

    def attack(self, trainer):
        pass

    def use_potion(self, pokemon):
        pass

    def switch_pokemon(self, new_pokemon):
        pass

    def catch_pokemone(self, ):
        #         if self.pokemon != []:
        # self.current_pokemon = self.pokemon[0]


def __repr__(self):
    return f'''
    Name: {self.name}
    Current Pokemon: {self.current_pokemon}
    Potions: {self.potions}
    Pokemon: {self.pokemon}
    '''


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

    def type_advantage_check(self, enemy_type):
        advantage = None
        if enemy_type == self.type_element:
            pass
        elif self.type_element in advantage_table:
            if enemy_type in advantage_table[self.type_element]:
                advantage = True
            else:
                advantage = False

        return advantage

    def attack(self, other, attack):
        try:
            advantage = self.type_advantage_check(other.type_element)
        except TypeError:
            advantage = None

        # print(f'advantage returned {advantage}')
        if advantage == True:
            other.lose_health(attack * 2)
            print(f'{self.name} has advantage.')
            print(
                f'{self.name} attacked {other.name} for {attack * 2} points of damage!')
        elif advantage == False:
            other.lose_health(attack * .5)
            print(f'{self.name} has disadvantage.')
            print(
                f'{self.name} attacked {other.name} for {int(attack / 2)} points of damage!')
        else:
            other.lose_health(attack)
            print(f'{self.name} attacked {other.name} for {attack} points of damage!')

        return

    def lose_health(self, attack):
        self.current_health = int(self.current_health - attack)
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
mewtwo2 = Pokemon('Mewtwo', 'Psychic')
bulbasaur = Pokemon('Bulbasaur', 'Seed')

bob = Trainer('Bob')

print(bob)

mewtwo.attack(bulbasaur, 10)
bulbasaur.attack(mewtwo, 10)
mewtwo2.attack(mewtwo, 10)
# print(mewtwo.type_element in advantage_table)
