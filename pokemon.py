import os
import random
from pokemon_db import *
from moves import *

#=================================================================================================#
#                                       WILD AREA CLASS                                           #
#=================================================================================================#

class Wild_Area():
    def __init__(self):
        pass

    def wild_pokemon(self):

        number = (random.randint(0, len(STORY.pokedex) - 1))
        wild_pokemon = POKEMON_DATABASE[number]
        self.opponent_pokemon = Pokemon(**wild_pokemon)
        self.opponent_pokemon.level = random.randint(5, 10)

        self.opponent_pokemon.attack = self.opponent_pokemon.attack + (self.opponent_pokemon.level - 5) * 2
        self.opponent_pokemon.defence = self.opponent_pokemon.defence + (self.opponent_pokemon.level - 5) * 2
        self.opponent_pokemon.speed = self.opponent_pokemon.speed + (self.opponent_pokemon.level - 5) * 2
        self.opponent_pokemon.max_health = self.opponent_pokemon.max_health + (self.opponent_pokemon.level - 5) * 2
        self.opponent_pokemon.current_health = self.opponent_pokemon.max_health

        input("""
        Something is moving in the grass... """)

        input("""
        You have encountered a level """ + str(self.opponent_pokemon.level) + " " + str(self.opponent_pokemon) + "!!")
        Pokemon.next_action(self)


#=================================================================================================#
#                                       POKEMON CLASS                                             #
#=================================================================================================#

class Pokemon():
    def __init__(self, name, level, type, max_health, current_health, attack, defence, speed, knocked_out, xp, move1, move2, move3, move4, poisoned, sleeping, paralyzed, burned, counter):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.knocked_out = knocked_out
        self.xp = xp
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.poisoned = poisoned
        self.sleeping = sleeping
        self.paralyzed = paralyzed
        self.burned = burned
        self.counter = counter

    def __repr__(self):
        return self.name

#=================================================================================================#
#                                 SELECT YOUR NEXT ACTION                                         #
#=================================================================================================#

    def next_action(self):

        choice = 0
        while choice not in ("1", "2", "3", "4"):
            os.system('clear')
            choice = input("""

        1 - Battle
        2 - Bag
        3 - Switch Pokemon
        4 - Run

        What do you want to do: """)

        if str(choice) == "1":
            Pokemon.attack_pokemon(self)
            if self.your_pokemon.speed < self.opponent_pokemon.speed:
                Pokemon.poisoned(self)
                Pokemon.burned(self)
                Pokemon.next_action(self)
                
            else:
                Pokemon.lose_health(self)
                Pokemon.poisoned(self)
                Pokemon.burned(self)
                Pokemon.next_action(self)

        elif str(choice) == "2":
            Trainer.access_bag(self)

        elif str(choice) == "3":
            if len(list(self.Pokemon_team)) == 1:
                input("""
        You cannot switch pokemon as you only have 1 pokemon in your party""")
                Pokemon.next_action(self)
            else:
                Trainer.switch_pokemon(self)

        elif str(choice) == "4":
            input("""
        You have successfully ran away!""")
            Wild_Area.wild_pokemon(self)

        else:
            print("""
        Thanks for playing!""")
            exit(0)

#=================================================================================================#
#                                        ATTACK POKEMON                                           #
#=================================================================================================#

    def attack_pokemon(self):
        damage_dealt = 0
        choice = 0

        while choice not in ("1", "2", "3", "4", "5"):
            os.system('clear')
            choice = input("""

        1 - """ + str(self.your_pokemon.move1["name"]) + """
        2 - """ + str(self.your_pokemon.move2["name"]) + """
        3 - """ + str(self.your_pokemon.move3["name"]) + """
        4 - """ + str(self.your_pokemon.move4["name"]) + """

        5 - Exit

        What do you want to do: """)

        if str(choice) == "1":
            self.chosen_move = self.your_pokemon.move1

        elif str(choice) == "2":
            self.chosen_move = self.your_pokemon.move2

        elif str(choice) == "3":
            self.chosen_move = self.your_pokemon.move3

        elif str(choice) == "4":
            self.chosen_move = self.your_pokemon.move4

        elif str(choice) == "5":
            Pokemon.next_action(self)
          
        if self.chosen_move["inflict damage"] is True:
            damage_dealt = (self.your_pokemon.level * 2 / 5) * self.chosen_move["damage"] * (self.your_pokemon.attack / self.opponent_pokemon.defence + 2) / 50

        Pokemon.effectiveness_for(self)
        damage_dealt = damage_dealt * self.effectiveness_for
        self.opponent_pokemon.current_health = self.opponent_pokemon.current_health - int(damage_dealt)
        
        if self.chosen_move["effect"] == "lower accuracy":
            self.opponent_pokemon.move1["accuracy"] = self.opponent_move["accuracy"] - 10
            self.opponent_pokemon.move2["accuracy"] = self.opponent_move["accuracy"] - 10
            self.opponent_pokemon.move3["accuracy"] = self.opponent_move["accuracy"] - 10
            self.opponent_pokemon.move4["accuracy"] = self.opponent_move["accuracy"] - 10
            message = "accuracy"
        
        elif self.chosen_move["effect"] == "lower attack":
            self.opponent_pokemon.attack = self.opponent_pokemon.attack * 0.70
            message = "attack"

        elif self.chosen_move["effect"] == "lower defence":
            self.opponent_pokemon.defence = self.opponent_pokemon.defence * 0.70
            message = "defence"

        elif self.chosen_move["effect"] == "increase defence":
            self.your_pokemon.defence = self.your_pokemon.defence * 1.30
            message = "defence"

        elif self.chosen_move["effect"] == "lower speed":
            self.opponent_pokemon.speed = self.opponent_pokemon.speed * 0.70
            message = "speed"

        elif self.chosen_move["effect"] == "inflict sleep":
            message = "sleep" 

        elif self.chosen_move["effect"] == "inflict poison":
            message = "poison" 

        elif self.chosen_move["effect"] == "inflict paralysis":
            message = "paralysis"

        elif self.chosen_move["effect"] == "inflict burn":
            message = "burn" 

        if self.your_pokemon.speed < self.opponent_pokemon.speed:
            Pokemon.lose_health(self)

        if self.your_pokemon.paralyzed is True and random.randint(1, 100) <= 50:

            input("""
        Your {} is paralyzed and unable to move.""".format(self.your_pokemon.name))

        sleep_counter = random.randint(2,3)
        if self.your_pokemon.sleeping is True and self.your_pokemon.counter >= sleep_counter:
            
            input("""
        Your {} woke up!""".format(self.your_pokemon.name))
            self.your_pokemon.counter = 0
            self.your_pokemon.sleeping = False
            
        if self.your_pokemon.sleeping is True and self.your_pokemon.counter < sleep_counter:

            input("""
        Your {} is still sleeping.""".format(self.your_pokemon.name))
            self.your_pokemon.counter += 1

        elif random.randint(1, 99) >= self.chosen_move["accuracy"]:

            input("""
        Your {} used {} but failed to land a hit.""".format(self.your_pokemon.name, self.chosen_move["name"]))

        elif self.chosen_move["inflict damage"] is True:

            if int(self.opponent_pokemon.current_health) > 0 and self.effectiveness_for > 1:

                input("""
        Your {} used {} on {} and has inflicted {} HP, it's super effective! Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), int(self.opponent_pokemon.current_health)))

            elif int(self.opponent_pokemon.current_health) > 0:

                input("""
        Your {} used {} on {} and has inflicted {} HP. Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), int(self.opponent_pokemon.current_health)))

            elif int(self.opponent_pokemon.current_health) > 0 and self.effectiveness_for < 1:

                input("""
        Your {} used {} on {} and has inflicted {} HP, it's not very effective... Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), int(self.opponent_pokemon.current_health)))

            elif int(self.opponent_pokemon.current_health) <= 0 and self.effectiveness_for > 1:

                input("""
        Your {} has attacked {}, inflicting {} HP, it's super effective! {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))

                self.opponent_pokemon.knocked_out = True
                self.opponent_pokemon.current_health = 0
                Pokemon.xp(self)

            elif int(self.opponent_pokemon.current_health) <= 0:

                input("""
        Your {} has attacked {}, inflicting {} HP. {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))

                self.opponent_pokemon.knocked_out = True
                self.opponent_pokemon.current_health = 0
                Pokemon.xp(self)

            elif int(self.opponent_pokemon.current_health) <= 0 and self.effectiveness_for < 1:

                input("""
        Your {} has attacked {}, inflicting {} HP, it's not very effective... {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))

                self.opponent_pokemon.knocked_out = True
                self.opponent_pokemon.current_health = 0
                Pokemon.xp(self)

            if "burn" in self.chosen_move["effect"] and random.randint(1,100) >= 85 and self.opponent_pokemon.burned is False:
                self.opponent_pokemon.burned = True
                
                input("""
        {} has been inflicted with a burn.""".format(self.opponent_pokemon.name))

            if "paralysis" in self.chosen_move["effect"] and random.randint(1,100) >=85 and self.opponent_pokemon.paralyzed is False:
                self.opponent_pokemon.paralyzed = True
            
                input("""
        {} has been paralyzed.""".format(self.opponent_pokemon.name))

        elif "lower" in self.chosen_move["effect"]:

            input("""
        Your {} used {} and has lowered {}'s {}.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, message ))

        elif "increase" in self.chosen_move["effect"]:

            input("""
        Your {} used {} and has increased its {}.""".format(self.your_pokemon.name, self.chosen_move["name"], message))

        elif "poison" in self.chosen_move["effect"]:

            if self.opponent_pokemon.poisoned is True:

                input("""
        Your {} used {} but the move failed as {} is already poisoned.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

            else: 
                self.opponent_pokemon.poisoned = True

                input("""
        Your {} used {} and has poisoned {}.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

        elif "paralysis" in self.chosen_move["effect"]:

            if self.opponent_pokemon.paralyzed is True:

                input("""
        Your {} used {} but the move failed as {} is already paralyzed.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

            else: 
                self.opponent_pokemon.paralyzed = True 

                input("""
        Your {} used {} and has paralyzed {}.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

        elif "sleep" in self.chosen_move["effect"]:

            if self.opponent_pokemon.sleeping is True:

                input("""
        Your {} used {} but the move failed as {} is already sleeping.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

            else: 
                self.opponent_pokemon.sleeping = True 

                input("""
        Your {} used {} and has made {} doze off to sleep.""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name))

#=================================================================================================#
#                                         GET ATTACKED                                            #
#=================================================================================================#

    def lose_health(self):

        global Pokemon
        damage_received = 0

        random_number = random.randint(1, 4)

        if random_number == 1:
            self.opponent_move = self.opponent_pokemon.move1

        elif random_number == 2:
            self.opponent_move = self.opponent_pokemon.move2

        elif random_number == 3:
            self.opponent_move = self.opponent_pokemon.move3

        elif random_number == 4:
            self.opponent_move = self.opponent_pokemon.move4

        if self.opponent_move["inflict damage"] is True:
            damage_received = (self.opponent_pokemon.level * 2 / 5) * self.opponent_move["damage"] * (self.opponent_pokemon.attack / self.your_pokemon.defence + 2) / 50

        Pokemon.effectiveness_against(self)
        damage_received = damage_received * self.effectiveness_against
        self.your_pokemon.current_health = self.your_pokemon.current_health - int(damage_received)

        if self.opponent_move["effect"] == "lower accuracy":
            self.your_pokemon.move1["accuracy"] = self.your_pokemon.move1["accuracy"] - 10
            self.your_pokemon.move2["accuracy"] = self.your_pokemon.move2["accuracy"] - 10
            self.your_pokemon.move3["accuracy"] = self.your_pokemon.move3["accuracy"] - 10
            self.your_pokemon.move4["accuracy"] = self.your_pokemon.move4["accuracy"] - 10
            message = "accuracy"
        
        elif self.opponent_move["effect"] == "lower attack":
            self.your_pokemon.attack = self.your_pokemon.attack * 0.70
            message = "attack"

        elif self.opponent_move["effect"] == "lower defence":
            self.your_pokemon.defence = self.your_pokemon.defence * 0.70
            message = "defence"

        elif self.opponent_move["effect"] == "increase defence":
            self.opponent_pokemon.defence = self.opponent_pokemon.defence * 1.30
            message = "defence"

        elif self.opponent_move["effect"] == "lower speed":
            self.your_pokemon.speed = self.your_pokemon.speed * 0.70
            message = "speed"

        elif self.opponent_move["effect"] == "inflict sleep":
            pass 

        elif self.opponent_move["effect"] == "inflict poison":
            message = "poison" 

        elif self.opponent_move["effect"] == "inflict paralysis":
            pass 

        if self.opponent_pokemon.paralyzed is True and random.randint(1, 100) <= 50:
    
            input("""
        {} is paralyzed and unable to move.""".format(self.opponent_pokemon.name))

        sleep_counter2 = random.randint(2,3)
        if self.opponent_pokemon.sleeping is True and self.opponent_pokemon.counter >= sleep_counter2:
            
            input("""
        Your {} woke up!""".format(self.opponent_pokemon.name))
            self.opponent_pokemon.counter = 0
            self.opponent_pokemon.sleeping = False
            
        if self.opponent_pokemon.sleeping is True and self.opponent_pokemon.counter < sleep_counter2:

            input("""
        Your {} is still sleeping.""".format(self.opponent_pokemon.name))
            self.opponent_pokemon.counter += 1

        elif random.randint(1, 99) >= self.opponent_move["accuracy"]: 
            
            input("""
        {} used {} but failed to land a hit.""".format(self.opponent_pokemon.name, self.opponent_move["name"]))

        elif self.opponent_move["inflict damage"] is True:
            if int(self.your_pokemon.current_health) > 0 and self.effectiveness_against > 1:

                input("""
        {} used {} on {}, inflicting {} HP, it's super effective! Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), int(self.your_pokemon.current_health)))

            elif int(self.your_pokemon.current_health) > 0 and self.effectiveness_against < 1:

                input("""
        {} used {} on {}, inflicting {} HP, it's not very effective... Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), int(self.your_pokemon.current_health)))

            elif int(self.your_pokemon.current_health) > 0:

                input("""
        {} used {} on {}, inflicting {} HP. Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), int(self.your_pokemon.current_health)))

            elif int(self.your_pokemon.current_health) <= 0 and self.effectiveness_against > 1:
                self.your_pokemon.knocked_out = True
                self.your_pokemon.current_health = 0

                input("""
        {} used {} on {}, inflicting {} HP, it's super effective! {} has fainted.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), self.your_pokemon.name))

                Pokemon.fainted(self)

            elif int(self.your_pokemon.current_health) <= 0 and self.effectiveness_against < 1:
                self.your_pokemon.knocked_out = True
                self.your_pokemon.current_health = 0

                input("""
        {} has attacked your {}, inflicting {} HP, it's not very effective... {} has fainted.""".format(self.opponent_pokemon.name, self.your_pokemon.name, int(damage_received), self.your_pokemon.name))

                Pokemon.fainted(self)

            elif int(self.your_pokemon.current_health) <= 0:
                self.your_pokemon.knocked_out = True
                self.your_pokemon.current_health = 0

                input("""
        {} has attacked your {}, inflicting {} HP. {} has fainted.""".format(self.opponent_pokemon.name, self.your_pokemon.name, int(damage_received), self.your_pokemon.name))

                Pokemon.fainted(self)

            if "burn" in self.opponent_move["effect"] and random.randint(1,100) >=85 and self.your_pokemon.burned is False:
                self.your_pokemon.burned = True
            
                input("""
        {} has been inflicted with a burn.""".format(self.your_pokemon.name))

            if "paralysis" in self.opponent_move["effect"] and random.randint(1,100) >=85 and self.your_pokemon.paralyzed is False:
                self.your_pokemon.paralyzed = True
            
                input("""
        {} has been paralyzed.""".format(self.your_pokemon.name))

        elif "increase" in self.opponent_move["effect"]:
            input("""
        {} used {} and has increased its {}.""".format(self.opponent_pokemon.name, self.opponent_move["name"], message))

        elif "lower" in self.opponent_move["effect"]:
            input("""
        {} used {} and has decreased {}'s {}.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, message))

        elif "poison" in self.opponent_move["effect"]:

            if self.your_pokemon.poisoned is True:

                input("""
        {} used {} but the move failed as {} is already Poisoned.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))

            else: 
                self.your_pokemon.poisoned = True 

                input("""
        {} used {} and has poisoned {}.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))

        elif "paralysis" in self.opponent_move["effect"]:

            if self.your_pokemon.paralyzed is True:

                input("""
        {} used {} but the move failed as {} is already paralyzed.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))

            else: 
                self.your_pokemon.paralyzed = True 

                input("""
        {} used {} and has paralyzed {}.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))

        elif "sleep" in self.opponent_move["effect"]:

            if self.your_pokemon.sleeping is True:

                input("""
        {} used {} but the move failed as {} is already sleeping.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))

            else: 
                self.your_pokemon.sleeping = True 

                input("""
        {} used {} and has made {} doze off to sleep.""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name))


#=================================================================================================#
#                                      EFFECTIVENESS CALCULATOR                                   #
#=================================================================================================#

    def effectiveness_for(self):

        self.effectiveness_for = 1
        self.effectiveness_against = 1

        if self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "water":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "water" and self.opponent_pokemon.type == "fire":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "electric" and self.opponent_pokemon.type == "water":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "electric" and self.opponent_pokemon.type == "flying":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "fire" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "fire" and self.opponent_pokemon.type == "bug":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "poison" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "poison" and self.opponent_pokemon.type == "fairy":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "flying" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "flying" and self.opponent_pokemon.type == "bug":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "bug" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 2

        elif self.chosen_move["type"] == "water" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "water" and self.opponent_pokemon.type == "water":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "fire" and self.opponent_pokemon.type == "water":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "fire" and self.opponent_pokemon.type == "fire":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "fire":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "flying":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "poison":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "grass" and self.opponent_pokemon.type == "bug":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "electric" and self.opponent_pokemon.type == "electric":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "electric" and self.opponent_pokemon.type == "grass":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "flying" and self.opponent_pokemon.type == "electric":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "poison" and self.opponent_pokemon.type == "poison":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "bug" and self.opponent_pokemon.type == "flying":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "bug" and self.opponent_pokemon.type == "poison":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "bug" and self.opponent_pokemon.type == "fire":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "fairy" and self.opponent_pokemon.type == "poison":
            self.effectiveness_for = 0.5

        elif self.chosen_move["type"] == "fairy" and self.opponent_pokemon.type == "fire":
            self.effectiveness_for = 0.5

        else:
            self.effectiveness_for = 1
            self.effectiveness_against = 1

    def effectiveness_against(self):

        self.effectiveness_for = 1
        self.effectiveness_against = 1

        if self.opponent_move["type"] == "grass" and self.your_pokemon.type == "water":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "water" and self.your_pokemon.type == "fire":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "electric" and self.your_pokemon.type == "water":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "electric" and self.your_pokemon.type == "flying":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "fire" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "fire" and self.your_pokemon.type == "bug":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "poison" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "poison" and self.your_pokemon.type == "fairy":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "flying" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "flying" and self.your_pokemon.type == "bug":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "bug" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 2

        elif self.opponent_move["type"] == "water" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "water" and self.your_pokemon.type == "water":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "fire" and self.your_pokemon.type == "water":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "fire" and self.your_pokemon.type == "fire":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "grass" and self.your_pokemon.type == "fire":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "grass" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "grass" and self.your_pokemon.type == "flying":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "grass" and self.your_pokemon.type == "poison":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "grass" and self.your_pokemon.type == "bug":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "electric" and self.your_pokemon.type == "electric":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "electric" and self.your_pokemon.type == "grass":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "flying" and self.your_pokemon.type == "electric":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "poison" and self.your_pokemon.type == "poison":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "bug" and self.your_pokemon.type == "flying":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "bug" and self.your_pokemon.type == "poison":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "bug" and self.your_pokemon.type == "fire":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "fairy" and self.your_pokemon.type == "poison":
            self.effectiveness_against = 0.5

        elif self.opponent_move["type"] == "fairy" and self.your_pokemon.type == "fire":
            self.effectiveness_against = 0.5

        else:
            self.effectiveness_for = 1
            self.effectiveness_against = 1


#=================================================================================================#
#                                            XP GAIN                                              #
#=================================================================================================#

    def xp(self):

        points = self.opponent_pokemon.level ** 2
        self.your_pokemon.xp += points 

        input("""
        """ + str(self.your_pokemon) + """ has gained """ + str(points) + " XP!")

        if self.your_pokemon.level ** 3 <= self.your_pokemon.xp:
            while self.your_pokemon.level ** 3 <= self.your_pokemon.xp:
                self.your_pokemon.level += 1
                self.your_pokemon.attack = self.your_pokemon.attack * 1.045
                self.your_pokemon.defence = self.your_pokemon.defence * 1.045
                self.your_pokemon.speed = self.your_pokemon.speed * 1.045
                self.your_pokemon.max_health = self.your_pokemon.max_health * 1.05
                self.your_pokemon.current_health = self.your_pokemon.max_health
                hp_up = self.your_pokemon.max_health * 1.05 - self.your_pokemon.max_health
                attack_up = self.your_pokemon.attack * 1.05 - self.your_pokemon.attack
                defence_up = self.your_pokemon.defence * 1.05 - self.your_pokemon.defence
                speed_up = self.your_pokemon.speed * 1.05 - self.your_pokemon.speed
                
                input("""
        """ + str(self.your_pokemon) + """ has grown to level """ + str(self.your_pokemon.level) + "!")

                os.system('clear')

                input("""
        {}'s stats grew!

        Level:   {} +1
        HP:      {} +{}
        Attack:  {} +{}
        Defence: {} +{}
        Speed:   {} +{}
        """.format(self.your_pokemon, self.your_pokemon.level, int(self.your_pokemon.max_health), int(hp_up), int(self.your_pokemon.attack), int(attack_up), int(self.your_pokemon.defence), int(defence_up), int(self.your_pokemon.speed), int(speed_up)))

        Wild_Area.wild_pokemon(self)


#=================================================================================================#
#                                         STATUS AILMENTS!                                        #
#=================================================================================================#

    def poisoned(self):

        if self.opponent_pokemon.poisoned is True:
                damage = self.opponent_pokemon.max_health / 100 * 10
                self.opponent_pokemon.current_health = self.opponent_pokemon.current_health - damage

                if int(self.opponent_pokemon.current_health) <= 0:
                    self.opponent_pokemon.knocked_out = True
                    self.opponent_pokemon.current_health = 0

                    input("""
        {} has been hurt by poison. It has fainted.""".format(self.opponent_pokemon.name))

                    Pokemon.xp(self)

                input("""
        {} has been hurt by poison. Its HP has decreased to {}""".format(self.opponent_pokemon.name, int(self.opponent_pokemon.current_health)))

        if self.your_pokemon.poisoned is True:
            damage = self.your_pokemon.max_health / 100 * 10
            self.your_pokemon.current_health = self.your_pokemon.current_health - damage

            if int(self.your_pokemon.current_health) <= 0:
                self.your_pokemon.current_health = 0

                input("""
        {} has been hurt by poison. It has fainted.""".format(self.your_pokemon.name))

                self.your_pokemon.knocked_out = True
                Pokemon.fainted(self)
                
            input("""
        {} has been hurt by poison. Its HP has decreased to {}""".format(self.your_pokemon.name, int(self.your_pokemon.current_health)))

    def burned(self):

        if self.opponent_pokemon.burned is True:
            damage = self.opponent_pokemon.max_health / 100 * 10
            self.opponent_pokemon.current_health = self.opponent_pokemon.current_health - damage

            if int(self.opponent_pokemon.current_health) <= 0:
                self.opponent_pokemon.knocked_out = True
                self.opponent_pokemon.current_health = 0

                input("""
        {} has been hurt by its burn. It has fainted.""".format(self.opponent_pokemon.name))

                Pokemon.xp(self)

            input("""
        {} has been hurt by its burn. Its HP has decreased to {}""".format(self.opponent_pokemon.name, int(self.opponent_pokemon.current_health)))

        if self.your_pokemon.burned is True:
            damage = self.your_pokemon.max_health / 100 * 10
            self.your_pokemon.current_health = self.your_pokemon.current_health - damage

            if int(self.your_pokemon.current_health) <= 0:
                self.your_pokemon.current_health = 0

                input("""
        {} has been hurt by its burn. It has fainted.""".format(self.your_pokemon.name))

                self.your_pokemon.knocked_out = True
                Pokemon.fainted(self)

            input("""
        {} has been hurt by its burn. Its HP has decreased to {}""".format(self.your_pokemon.name, int(self.your_pokemon.current_health)))


#=================================================================================================#
#                                           FAINTED                                               #
#=================================================================================================#

    def fainted(self):

        for i in range(len(list(self.Pokemon_team))):
            if Pokemon_team[i].knocked_out is False:
                
                input("""
        Please switch out your next pokemon""")
                
                Trainer.switch_pokemon(self)
                    
        return input("""
        Game over, all your Pokemon have fainted""")
        exit(0)


#=================================================================================================#
#                                         TRAINER CLASS                                           #
#=================================================================================================#

class Trainer():
    def __init__(self, name, rival_name, Pokemon_team, items, money, your_pokemon, opponent_pokemon):
        self.name = name
        self.Pokemon_team = Pokemon_team
        self.items = items
        self.money = money
        self.rival_name = rival_name
        self.your_pokemon = your_pokemon
        self.opponent_pokemon = opponent_pokemon

    def __repr__(self):
        return self.name

    def NEW_TRAINER(self):

        os.system('clear')
        input("""

        Hi there!
        Welcome to the world of Pokémon!
        You can call me Juniper.
        But you'll hear people calling me the Pokémon Professor.""")

        os.system('clear')
        input("""
        Right! This world is full of Pocket Monsters...
        Well, usually called "Pokémon" for short! And they're fantastic creatures!
        Pokémon possess miraculous power, come in all shapes and sizes, live in all kinds of locales...
        And we humans live together with them in peace!
        We're always there for each other, the both of us.
        But joining forces to help each other can often be a difficult task.
        And while it's their most popular role of all, making fellow Pokémon fight only binds them further.
        And that's why I study Pokémon.""")

        os.system('clear')
        self.name = input("""
        Now, that's quite enough about me...
        Won't you tell me some about yourself?

        So... tell me your name!

        Name: """)

        choice = 0
        while choice not in ("y", "n"):

            choice = input("""
        """ + str(self.name) + """, is it? y/n:""")

        if choice == "n":
            Trainer.NEW_TRAINER(POKEMON_TRAINER)

        elif choice == "y":

            os.system('clear')
            input("""
        Your name's """ + str(self.name) + """! That\'s just wonderful!""")

            os.system('clear')
            input("""
        Now then, allow me to introduce the friends who'll be with you on the way.
        (A guy appears.)""")

            os.system('clear')
            input("""
        This guy here is """ + str(self.rival_name) + """.
        He's a bit moody at times, and his face doesn't look bothered, but he's very frank about things.""")

            os.system('clear')
            input("""
        And now, I've given the two of you a present containing your precious, long-awaited Pokémon.
        """+ str(self.name) + """!! From the moment you choose your Pokémon partner for the journey ahead...
        That is when the tale of your own adventure begins!""")

            os.system('clear')
            input("""
        On this journey, you will meet countless Pokémon, and many people who think in different ways!
        Through all these meetings, I deeply hope you find something that you alone can treasure...
        Right! As you come into contact with people and Pokémon, you will mature as a person.
        And that is the greatest goal of your adventure!
        So, let us be off! Into the world of Pokémon!""")


            Trainer.starter(self)

#=================================================================================================#
#                                     CHOOSE STARTER POKEMON                                      #
#=================================================================================================#

    def starter(self):

        os.system('clear')
        choice = 0            

        while choice not in ("1", "2", "3"):
            os.system('clear')
            choice = input("""

        1 - Bulbasaur
        2 - Squirtle
        3 - Charmander

        Please select your starter Pokemon: """)
        
        if str(choice) == "1":
            self.your_pokemon = Pokemon(**bulbasaur)
            self.opponent_pokemon = Pokemon(**squirtle)

        elif str(choice) == "2":
            self.your_pokemon = Pokemon(**squirtle)
            self.opponent_pokemon = Pokemon(**charmander)

        elif str(choice) == "3":
            self.your_pokemon = Pokemon(**charmander)
            self.opponent_pokemon = Pokemon(**bulbasaur)

        while choice not in ("y", "n"):
            choice = input("""
        You have chosen """ + str(self.your_pokemon.name) + """, the """ + str(self.your_pokemon.type) + """ type pokemon! Are you sure you want to go ahead with """ + str(self.your_pokemon.name) + """? y/n: """)

        if str(choice) == "y":
            input("""
        Congratulations, you have obtained your first pokemon! """ + str(self.your_pokemon.name) + """ seems to like you!""")

            input("""
        """+ str(self.rival_name) + """ has chosen """ + str(self.opponent_pokemon.name) + """, the """ +  str(self.opponent_pokemon.type) + """ type Pokemon.""")

            self.Pokemon_team.append(self.your_pokemon)
            self.Pokemon_team.append(Pokemon(**jigglypuff))

            input("""
        Please accept these little gifts to help you embark on your adventure...

        You have received 10 Poke balls!
        You have received 10 potions!
        You have received 5 revives!""")

            self.items["potion"] += 10
            self.items["revive"] += 5
            self.items["poke ball"] += 1

            input("""
        A whole new adventure awaits you and your """ + str(self.your_pokemon.name) + """! Go out there and catch them all!""")
            Pokemon.next_action(self)

        elif str(choice) == "n":
            Trainer.starter(self)



#=================================================================================================#
#                                            ACCESS BAG                                           #
#=================================================================================================#

    def access_bag(self):

        choice = 0
        while choice not in ("1", "2", "3", "4", "5"):
            os.system('clear')

            choice = input("""

        1 - Use a potion: """ + str(self.items["potion"]) + """
        2 - Use a revive: """ + str(self.items["revive"]) + """
        3 - Use a poke ball: """ + str(self.items["poke ball"]) + """
        4 - Use an antidote: """ + str(self.items["antidote"]) + """
        5 - Exit

        What do you want to do: """)

        if str(choice) == "1":
            if self.items["potion"] == 0:
                input("""
        You don't have any potions left.""")
                Trainer.access_bag(self)
            else:
                Trainer.use_potion(self)

        elif str(choice) == "2":
            if self.items["revive"] == 0:
                input("""
        You don't have any revives left.""")
                Trainer.access_bag(self)
            else:
                Trainer.use_revive(self)

        elif str(choice) == "3":
            if self.items["poke ball"] == 0:
                input("""
        You don't have any poke balls left.""")
                Trainer.access_bag(self)
            else:
                Trainer.use_poke_ball(self)

        elif str(choice) == "4":
            if self.items["antidote"] == 0:
                input("""
        You don't have any antidotes left.""")
                Trainer.access_bag(self)
            else:
                Trainer.use_antidote(self)

        elif str(choice) == "5":
            Pokemon.next_action(self)

#=================================================================================================#
#                                            USE ITEM                                             #
#=================================================================================================#

    def use_potion(self):

        self.items["potion"] = self.items["potion"] - 1
        self.your_pokemon.current_health = self.your_pokemon.current_health + 30
        if int(self.your_pokemon.current_health) > self.your_pokemon.max_health:
            self.your_pokemon.current_health = self.your_pokemon.max_health
        input("""
        You have used a potion on your {}, it's current HP has increased to {}""".format(self.your_pokemon.name, int(self.your_pokemon.current_health)))

        Pokemon.lose_health(self)
        Pokemon.poisoned(self)
        Pokemon.burned(self)
        Pokemon.next_action(self)

    def use_revive(self):
        self.items["revive"] = self.items["revive"] - 1
        self.your_pokemon.current_health = self.your_pokemon.max_health / 2
        input("""
        You have used a revive on your {}, it's current HP has increased to {}""".format(self.your_pokemon.name, int(self.your_pokemon.current_health)))

        Pokemon.lose_health(self)
        Pokemon.poisoned(self)
        Pokemon.burned(self)
        Pokemon.next_action(self)

    def use_poke_ball(self):
        self.items["poke ball"] = self.items["poke ball"] - 1
        input("""
        You threw a poke ball at """ + str(self.opponent_pokemon) + "!""")

        Pokemon.lose_health(self)
        Pokemon.poisoned(self)
        Pokemon.burned(self)
        Pokemon.next_action(self)

    def use_antidote(self):
        #if self.your_pokemon.poisoned is True:
        self.items["antidote"] = self.items["antidote"] - 1
        self.your_pokemon.poisoned = False
        input("""
        You have used an antidote on """ + str(self.your_pokemon) + "!, it is no longer poisoned.""")
        
        Pokemon.lose_health(self)
        Pokemon.poisoned(self)
        Pokemon.burned(self)
        Pokemon.next_action(self)


#=================================================================================================#
#                                            SWITCH POKEMON                                       #
#=================================================================================================#

    def switch_pokemon(self):
        
        os.system('clear')
        for i in range(len(list(self.Pokemon_team))):
            print("""
        {} - {} | {}/{}HP | Level {}""".format(i+1, self.Pokemon_team[i].name, int(self.Pokemon_team[i].current_health), int(self.Pokemon_team[i].max_health), self.Pokemon_team[i].level))
        
        choice = 0
        while choice not in ("1", "2", "3", "4", "5", "6"):

            choice = input("""
        Select the pokemon you want to switch to: """)

            if str(choice) == "1":
                if self.Pokemon_team[0].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)
                else:
                    Pokemon.next_action(self)

            elif str(choice) == "2":
                if self.Pokemon_team[1].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.Pokemon_team[1]
                    self.Pokemon_team.pop(1)
                    self.Pokemon_team.insert(0, self.your_pokemon)
                    input("""
        GO """ + str(self.your_pokemon) + """!""")
                    Pokemon.lose_health(self)
                    Pokemon.next_action(self)

            elif str(choice) == "3":
                if self.Pokemon_team[2].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.Pokemon_team[2]
                    self.Pokemon_team.pop(2)
                    self.Pokemon_team.insert(0, self.your_pokemon)
                    input("""
        GO """ + str(self.your_pokemon) + """!""")
                    Pokemon.lose_health(self)
                    Pokemon.next_action(self)

            elif str(choice) == "4":
                if self.Pokemon_team[3].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.Pokemon_team[3]
                    self.Pokemon_team.pop(3)
                    self.Pokemon_team.insert(0, self.your_pokemon)
                    input("""
        GO """ + str(self.your_pokemon) + """!""")
                    Pokemon.lose_health(self)
                    Pokemon.next_action(self)

            elif str(choice) == "5":
                if self.Pokemon_team[4].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.Pokemon_team[4]
                    self.Pokemon_team.pop(4)
                    self.Pokemon_team.insert(0, self.your_pokemon)
                    input("""
        GO """ + str(self.your_pokemon) + """!""")
                    Pokemon.lose_health(self)
                    Pokemon.next_action(self)

            elif str(choice) == "6":
                if self.Pokemon_team[5].knocked_out is True:
                    input("""
        You can not battle with a fainted Pokemon.""")
                    Trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.Pokemon_team[5]
                    self.Pokemon_team.pop(5)
                    self.Pokemon_team.insert(0, self.your_pokemon)
                    input("""
        GO """ + str(self.your_pokemon) + """!""")
                    Pokemon.lose_health(self)
                    Pokemon.next_action(self)

#=================================================================================================#
#                                            STORY CLASS                                          #
#=================================================================================================#

class STORY():

    def __init__(self, pokedex):
        self.pokedex = pokedex


POKEMON_DATABASE = [bulbasaur, charmander, squirtle, rattata, pikachu, caterpie, ekans, jigglypuff, pidgey]

ITEMS = {"potion": 0, "revive": 0, "poke ball": 0, "antidote": 5}
Pokemon_team = []

STORY = STORY(POKEMON_DATABASE)
POKEMON_TRAINER = Trainer("Daniel", "Daniel", Pokemon_team, ITEMS, 1000, "", "")
NEW_TRAINER = Trainer.starter(POKEMON_TRAINER)

#Trainer.NEW_TRAINER(POKEMON_TRAINER)
