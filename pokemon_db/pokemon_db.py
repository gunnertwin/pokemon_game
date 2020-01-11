from . import moves
class bulbasaur():

    def __init__(self):
        self.name = "Bulbasaur"
        self.level = 5
        self.type = "fire"
        self.max_health = 45
        self.current_health = 45
        self.attack = 49
        self.defence = 49
        self.speed = 45
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.vine_whip
        self.move3 = moves.growl
        self.move4 = moves.tackle

    def __repr__(self):
        return self.name

class squirtle():

    def __init__(self):
        self.name = "Squirtle"
        self.level = 5
        self.type = "water"
        self.max_health = 44
        self.current_health = 44
        self.attack = 48
        self.defence = 65
        self.speed = 43
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.vine_whip
        self.move3 = moves.growl
        self.move4 = moves.tackle

    def __repr__(self):
        return self.name
