import moves
class bulbasaur():

    def __init__(self):
        self.name = "Bulbasaur"
        self.level = 5
        self.type = "grass"
        self.max_health = 45
        self.current_health = 45
        self.attack = 49
        self.defence = 49
        self.speed = 45
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.vine_whip
        self.move3 = moves.growl
        self.move4 = moves.poison_powder

    def __repr__(self):
        return self.name

class charmander():

    def __init__(self):
        self.name = "Charmander"
        self.level = 5
        self.type = "fire"
        self.max_health = 39
        self.current_health = 39
        self.attack = 52
        self.defence = 43
        self.speed = 65
        self.knocked_out = False
        self.move1 = moves.scratch
        self.move2 = moves.ember
        self.move3 = moves.growl
        self.move4 = moves.dragon_breath

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
        self.move2 = moves.water_gun
        self.move3 = moves.tail_whip
        self.move4 = moves.bite

    def __repr__(self):
        return self.name

class rattata():

    def __init__(self):
        self.name = "Rattata"
        self.level = 5
        self.type = "normal"
        self.max_health = 30
        self.current_health = 30
        self.attack = 56
        self.defence = 35
        self.speed = 72
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.tail_whip
        self.move3 = moves.quick_attack
        self.move4 = moves.bite

    def __repr__(self):
        return self.name

class pikachu():

    def __init__(self):
        self.name = "Pikachu"
        self.level = 5
        self.type = "electric"
        self.max_health = 35
        self.current_health = 35
        self.attack = 55
        self.defence = 40
        self.speed = 90
        self.knocked_out = False
        self.move1 = moves.thunder_shock
        self.move2 = moves.thunder_wave
        self.move3 = moves.growl
        self.move4 = moves.double_team

    def __repr__(self):
        return self.name

class caterpie():

    def __init__(self):
        self.name = "Caterpie"
        self.level = 5
        self.type = "bug"
        self.max_health = 45
        self.current_health = 45
        self.attack = 30
        self.defence = 35
        self.speed = 45
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.bug_bite
        self.move3 = moves.string_shot
        self.move4 = moves.tackle

    def __repr__(self):
        return self.name

class ekans():

    def __init__(self):
        self.name = "Ekans"
        self.level = 5
        self.type = "poison"
        self.max_health = 35
        self.current_health = 35
        self.attack = 60
        self.defence = 44
        self.speed = 55
        self.knocked_out = False
        self.move1 = moves.poison_sting
        self.move2 = moves.acid
        self.move3 = moves.bite
        self.move4 = moves.leer

    def __repr__(self):
        return self.name

class jigglypuff():

    def __init__(self):
        self.name = "Jigglypuff"
        self.level = 5
        self.type = "fairy"
        self.max_health = 115
        self.current_health = 115
        self.attack = 45
        self.defence = 20
        self.speed = 20
        self.knocked_out = False
        self.move1 = moves.sing
        self.move2 = moves.pound
        self.move3 = moves.defense_curl
        self.move4 = moves.double_slap

    def __repr__(self):
        return self.name

class pidgey():

    def __init__(self):
        self.name = "Pidgey"
        self.level = 5
        self.type = "flying"
        self.max_health = 40
        self.current_health = 40
        self.attack = 45
        self.defence = 40
        self.speed = 56
        self.knocked_out = False
        self.move1 = moves.tackle
        self.move2 = moves.sand_attack
        self.move3 = moves.gust
        self.move4 = moves.quick_attack

    def __repr__(self):
        return self.name


