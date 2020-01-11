import os
import random
from pokemon_db.pokemon_db import *

#=============================================================================================================================================#
#                                                         WILD AREA CLASS                                                                     #
#=============================================================================================================================================#

class wild_area():
    def __init__(self):
        pass
                
    def wild_pokemon(self):
        
        self.opponent_pokemon = (random.randint(0,len(story.pokedex) - 1 ))
        self.opponent_pokemon = pokemon_database[self.opponent_pokemon]
        self.opponent_pokemon.level = random.randint(2,5)
        self.opponent_pokemon.current_health = self.opponent_pokemon.max_health

        input("""
        Something is moving in the grass... """)

        input("""
        You have encountered a level """ + str(self.opponent_pokemon.level) + " " + str(self.opponent_pokemon) + "!!")
        pokemon.next_action(self)
        

#=============================================================================================================================================#
#                                                         POKEMON CLASS                                                                       #
#=============================================================================================================================================#

class pokemon():
    def __init__(self, name, level, type, max_health, current_health, attack, defence, speed, knocked_out, xp, move1, move2, move3, move4):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        self.knocked_out = knocked_out
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        
    def __repr__(self):
        return self.name

#=============================================================================================================================================#
#                                                      SELECT YOUR NEXT ACTION                                                                #
#=============================================================================================================================================#

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
                pokemon.attack_pokemon(self)
                if self.your_pokemon.speed < self.opponent_pokemon.speed:
                    pokemon.next_action(self)
                else:
                    pokemon.lose_health(self)
                    pokemon.next_action(self)
           
        elif str(choice) == "2":
            trainer.access_bag(self)

        elif str(choice) == "3":
            if len(list(self.pokemon_team)) == 1:
                input("""
        You cannot switch pokemon as you only have 1 pokemon in your party""")
                pokemon.next_action(self)
            else:
                trainer.switch_pokemon(self)
  
        elif str(choice) == "4":
            input("""
        You have successfully ran away!""")
            wild_area.wild_pokemon(self)

        else:
            print("""
        Thanks for playing!""")
            exit(0)

#=============================================================================================================================================#
#                                                      ATTACK POKEMON                                                                         #
#=============================================================================================================================================#

    def attack_pokemon(self):

        choice = 0
        while choice not in ("1", "2", "3", "4"):
            os.system('clear')
            choice = input(""" 
        
        1 - """ + str(self.your_pokemon.move1["name"]) + """ 
        2 - """ + str(self.your_pokemon.move2["name"]) + """
        3 - """ + str(self.your_pokemon.move3["name"]) + """
        4 - """ + str(self.your_pokemon.move4["name"]) + """
  
        What do you want to do: """)

        if str(choice) == "1":
            if self.your_pokemon.move1["inflict damage"] is True:
                damage_dealt = (self.your_pokemon.level * 2 / 5) * self.your_pokemon.move1["damage"] * (self.your_pokemon.attack / self.opponent_pokemon.defence + 2) / 50 
                self.chosen_move = self.your_pokemon.move1

        elif str(choice) == "2":
            if self.your_pokemon.move2["inflict damage"] is True:
                damage_dealt = (self.your_pokemon.level * 2 / 5) * self.your_pokemon.move2["damage"] * (self.your_pokemon.attack / self.opponent_pokemon.defence + 2) / 50 
                self.chosen_move = self.your_pokemon.move2

        elif str(choice) == "3":
            if self.your_pokemon.move3["inflict damage"] is True:
                damage_dealt = (self.your_pokemon.level * 2 / 5) * self.your_pokemon.move3["damage"] * (self.your_pokemon.attack / self.opponent_pokemon.defence + 2) / 50 
                self.chosen_move = self.your_pokemon.move3
    
        elif str(choice) == "4":
            if self.your_pokemon.move3["inflict damage"] is True:
                damage_dealt = (self.your_pokemon.level * 2 / 5) * self.your_pokemon.move4["damage"] * (self.your_pokemon.attack / self.opponent_pokemon.defence + 2) / 50 
                self.chosen_move = self.your_pokemon.move4
       
        self.opponent_move = self.opponent_pokemon.move1
        pokemon.effectiveness(self)
        damage_dealt = damage_dealt * self.effectiveness_for
        self.opponent_pokemon.current_health = self.opponent_pokemon.current_health - int(damage_dealt)
        
        if self.your_pokemon.speed < self.opponent_pokemon.speed:
            pokemon.lose_health(self)

        if self.opponent_pokemon.current_health > 0 and self.effectiveness_for > 1:
        
            input("""
        Your {} used {} on {} and has inflicted {} HP, it's super effective! Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.current_health))
        
        elif self.opponent_pokemon.current_health > 0:

             input("""
        Your {} used {} on {} and has inflicted {} HP. Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.current_health))

        elif self.opponent_pokemon.current_health > 0 and self.effectiveness_for < 1:

             input("""
        Your {} used {} on {} and has inflicted {} HP, it's not very effective... Its current HP is now {}""".format(self.your_pokemon.name, self.chosen_move["name"], self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.current_health))

        elif self.opponent_pokemon.current_health <= 0 and self.effectiveness_for > 1:
            
            input("""
        Your {} has attacked {}, inflicting {} HP, it's super effective! {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))
            
            self.opponent_pokemon.knocked_out = True
            self.opponent_pokemon.current_health = 0
            pokemon.xp(self)

        elif self.opponent_pokemon.current_health <= 0:
            
            input("""
        Your {} has attacked {}, inflicting {} HP. {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))

            self.opponent_pokemon.knocked_out = True
            self.opponent_pokemon.current_health = 0
            pokemon.xp(self)
        
        elif self.opponent_pokemon.current_health <= 0 and self.effectiveness_for < 1:
            
            input("""
        Your {} has attacked {}, inflicting {} HP, it's not very effective... {} has fainted.""".format(self.your_pokemon.name, self.opponent_pokemon.name, int(damage_dealt), self.opponent_pokemon.name))

            self.opponent_pokemon.knocked_out = True
            self.opponent_pokemon.current_health = 0
            pokemon.xp(self)


#=============================================================================================================================================#
#                                                      GET ATTACKED                                                                           #
#=============================================================================================================================================#

    def lose_health(self):

        global pokemon
        damage_received = 0

        random_number = random.randint(1,2)

        if random_number == 1:
            if self.opponent_pokemon.move1["inflict damage"] is True:
                damage_received = (self.opponent_pokemon.level * 2 / 5) * self.opponent_pokemon.move1["damage"] * (self.opponent_pokemon.attack / self.your_pokemon.defence + 2) / 50 
                self.opponent_move = self.opponent_pokemon.move1

        elif random_number == 2:
            if self.opponent_pokemon.move2["inflict damage"] is True:
                damage_received = (self.opponent_pokemon.level * 2 / 5) * self.opponent_pokemon.move2["damage"] * (self.opponent_pokemon.attack / self.your_pokemon.defence + 2) / 50 
                self.opponent_move = self.opponent_pokemon.move2

        elif random_number == 3:
            if self.opponent_pokemon.move3["inflict damage"] is True:
                damage_received = (self.opponent_pokemon.level * 2 / 5) * self.opponent_pokemon.move3["damage"] * (self.opponent_pokemon.attack / self.your_pokemon.defence + 2) / 50 
                self.opponent_move = self.opponent_pokemon.move3

        elif random_number == 4:
            if self.opponent_pokemon.move4["inflict damage"] is True:
                damage_received = (self.opponent_pokemon.level * 2 / 5) * self.opponent_pokemon.move4["damage"] * (self.opponent_pokemon.attack / self.your_pokemon.defence + 2) / 50 
                self.opponent_move = self.opponent_pokemon.move4
        
        pokemon.effectiveness_against(self)
        damage_received = damage_received * self.effectiveness_against
        self.your_pokemon.current_health = self.your_pokemon.current_health - int(damage_received)
        

        if self.your_pokemon.current_health > 0 and self.effectiveness_against > 1:
            input("""
        {} used {} on {}, inflicting {} HP, it's super effective! Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), self.your_pokemon.current_health))

        elif self.your_pokemon.current_health > 0 and self.effectiveness_against < 1:
            input("""
        {} used {} on {}, inflicting {} HP, it's not very effective... Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), self.your_pokemon.current_health))

        elif self.your_pokemon.current_health > 0:
            input("""
        {} used {} on {}, inflicting {} HP. Its current HP is now {}""".format(self.opponent_pokemon.name, self.opponent_move["name"], self.your_pokemon.name, int(damage_received), self.your_pokemon.current_health))

        elif self.your_pokemon.current_health <= 0 and self.effectiveness_against > 1:
            self.your_pokemon.knocked_out = True
            self.your_pokemon.current_health = 0
            input("""
        {} has attacked your {}, inflicting {} HP, it's super effective! {} has fainted.""".format(self.opponent_pokemon.name, self.your_pokemon.name, int(damage_received), self.your_pokemon.name))
            
            for pokemon in self.pokemon_team:
                if pokemon.knocked_out == False:
                    trainer.switch_pokemon(self)
                
        elif self.your_pokemon.current_health <= 0 and self.effectiveness_against < 1:
            self.your_pokemon.knocked_out = True
            self.your_pokemon.current_health = 0
            input("""
        {} has attacked your {}, inflicting {} HP, it's not very effective... {} has fainted.""".format(self.opponent_pokemon.name, self.your_pokemon.name, int(damage_received), self.your_pokemon.name))

            for pokemon in self.pokemon_team:
                if pokemon.knocked_out == False:
                    trainer.switch_pokemon(self)

        elif self.your_pokemon.current_health <= 0:
            self.your_pokemon.knocked_out = True
            self.your_pokemon.current_health = 0
            input("""
        {} has attacked your {}, inflicting {} HP. {} has fainted.""".format(self.opponent_pokemon.name, self.your_pokemon.name, int(damage_received), self.your_pokemon.name))
     
            for pokemon in self.pokemon_team:
                if pokemon.knocked_out == False:
                    input("""
        Please switch out your next pokemon""")
                    trainer.switch_pokemon(self)
                
            input("""
        Game Over!""")
            exit(0)

#=============================================================================================================================================#
#                                                    EFFECTIVENESS CALCULATOR                                                                 #
#=============================================================================================================================================#

    def effectiveness(self):
        
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


#=============================================================================================================================================#
#                                                                XP GAIN                                                                      #
#=============================================================================================================================================#

    def xp(self):

        points = 0

        input("""
        """ + str(self.your_pokemon) + """ has gained """ + str(points) + " XP!")
        wild_area.wild_pokemon(self)

#=============================================================================================================================================#
#                                                              TRAINER CLASS                                                                  #
#=============================================================================================================================================#

class trainer():
    def __init__(self, name, rival_name, pokemon_team, items, money):
        self.name = name
        self.pokemon_team = pokemon_team
        self.items = items
        self.money = money
        self.rival_name = rival_name

    def __repr__(self):
        return self.name

    def new_trainer(self):
   
        print(""" 

        Hi there!
        Welcome to the world of Pokémon!
        You can call me Juniper.
        But you'll hear people calling me the Pokémon Professor.
 
        Right! This world is full of Pocket Monsters...
        Well, usually called "Pokémon" for short! And they're fantastic creatures!
        Pokémon possess miraculous power, come in all shapes and sizes, live in all kinds of locales...
        And we humans live together with them in peace!
        We're always there for each other, the both of us.
        But joining forces to help each other can often be a difficult task.
        And while it's their most popular role of all, making fellow Pokémon fight only binds them further.
        And that's why I study Pokémon.

        Now, that's quite enough about me...
        Won't you tell me some about yourself?""")

        self.name = input(""" 
        So... tell me your name!

        Name: """)

        choice = 0
        while choice not in ("y", "n"):

            choice = input("""
        """ + str(self.name) + """, is it? y/n:""")
        
        if choice == "n":
            trainer.new_trainer(pokemon_trainer)
        
        elif choice == "y":

            input("""
        Your name's """ + str(self.name) + """ ! That\'s just wonderful!""")
        
            input("""
        Now then, allow me to introduce the friends who'll be with you on the way.
        (A guy appears.)
        This guy here is """ + str(self.rival_name) + """.
        He's a bit moody at times, the fat cunt, but he's very frank about things.""")

            input("""
        And now, I've given the two of you a present containing your precious, long-awaited Pokémon.
        """+ str(self.name) + """!! From the moment you choose your Pokémon partner for the journey ahead...
        That is when the tale of your own adventure begins!""")

            input("""
        On this journey, you will meet countless Pokémon, and many people who think in different ways!
        Through all these meetings, I deeply hope you find something that you alone can treasure...
        Right! As you come into contact with people and Pokémon, you will mature as a person.
        And that is the greatest goal of your adventure!
        So, let us be off! Into the world of Pokémon!""")
        

            trainer.starter(self,"","")
            
#=============================================================================================================================================#
#                                                      CHOOSE STARTER POKEMON                                                                 #
#=============================================================================================================================================#

    def starter(self, your_pokemon, opponent_pokemon):
        self.your_pokemon = your_pokemon
        self.opponent_pokemon = opponent_pokemon
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
            self.your_pokemon = bulbasaur()
            self.opponent_pokemon = squirtle()

        elif str(choice) == "2":
            self.your_pokemon = squirtle()
            self.opponent_pokemon = charmander()

        elif str(choice) == "3":
            self.your_pokemon = charmander()
            self.opponent_pokemon = bulbasaur()

        while choice not in ("y", "n"):
                choice = input("""
        You have chosen """ + str(self.your_pokemon.name) + """, the """ + str(self.your_pokemon.type) + """ type pokemon! Are you sure you want to go ahead with """ + str(self.your_pokemon.name) + """? y/n: """)

        if str(choice) == "y":      
            input("""
        Congratulations, you have obtained your first pokemon! """ + str(self.your_pokemon.name) + """ seems to like you!""")
        
            input("""
        """+ str(self.rival_name) + """ has chosen """ + str(self.opponent_pokemon.name) + """, the """ +  str(self.opponent_pokemon.type) + """ type pokemon.""")

            pokemon_team.append(self.your_pokemon)
            
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
            pokemon.next_action(self)

        elif str(choice) == "n":
            trainer.starter(self)
  


#=============================================================================================================================================#
#                                                             ACCESS BAG                                                                      #
#=============================================================================================================================================#
    
    def access_bag(self):

        choice = 0
        while choice not in ("1", "2", "3", "4"):
            os.system('clear')

            choice = input(""" 

        1 - Use a potion: """ + str(items["potion"]) + """
        2 - Use a revive: """ + str(items["revive"]) + """
        3 - Use a poke ball: """ + str(items["poke ball"]) + """
        4 - Exit
  
        What do you want to do: """)

        if str(choice) == "1":
            if items["potion"] == 0:
                input("""
        You don't have any potions left.""")
                trainer.access_bag(self)
            else:
                trainer.use_potion(self)

        elif str(choice) == "2":
            if items["revive"] == 0:
                input("""
        You don't have any revives left.""")
                trainer.access_bag(self)
            else:
                trainer.use_revive(self)

        elif str(choice) == "3":
            if items["poke ball"] == 0:
                input("""
        You don't have any poke balls left.""")
                trainer.access_bag(self)
            else:
                trainer.use_poke_ball(self)

        elif str(choice) == "4":
            pokemon.next_action(self)

#=============================================================================================================================================#
#                                                             USE ITEM                                                                        #
#=============================================================================================================================================#
    
    def use_potion(self):
 
        items["potion"] = items["potion"] - 1
        self.your_pokemon.current_health = self.your_pokemon.current_health + 30
        if self.your_pokemon.current_health > self.your_pokemon.max_health:
            self.your_pokemon.current_health = self.your_pokemon.max_health
        input("""    
        You have used a potion on your {}, it's current HP has increased to {}""".format(self.your_pokemon.name, self.your_pokemon.current_health))

        pokemon.lose_health(self)
        pokemon.next_action(self)

    def use_revive(self):
        items["revive"] = items["revive"] - 1
        self.your_pokemon.current_health = self.your_pokemon.max_health / 2
        input("""
        You have used a revive on your {}, it's current HP has increased to {}""".format(self.your_pokemon.name, self.your_pokemon.current_health))

        pokemon.lose_health(self)
        pokemon.next_action(self)

    def use_poke_ball(self):
        items["poke ball"] = items["poke ball"] - 1
        input("""
        You threw a poke ball at """ + str(self.opponent_pokemon) + "!""")
        
        pokemon.lose_health(self)
        pokemon.next_action(self)


#=============================================================================================================================================#
#                                                         SWITCH POKEMON                                                                      #
#=============================================================================================================================================#

    def switch_pokemon(self):
                           
        for i in range(len(list(self.pokemon_team))):
            print("""
        """ + str(i+1) + " -  " + str(self.pokemon_team[i]) + " | " + str(self.pokemon_team[i].current_health) + "/" + str(self.pokemon_team[i].max_health) + "HP | Level " + str(self.pokemon_team[i].level))

        choice = 0
        while choice not in ("1", "2", "3", "4", "5", "6"):

            choice = input("""
            Select the pokemon you want: """)

            if str(choice) == "1":
                if self.pokemon_team[0].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)
                else:
                    pokemon.next_action(self)
                
            elif str(choice) == "2":
                if self.pokemon_team[1].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.pokemon_team[1]
                    self.pokemon_team.pop(1)
                    self.pokemon_team.insert(0, self.your_pokemon)
                    input("""
            GO """ + str(self.your_pokemon) + """!""")
                    pokemon.next_action(self)

            elif str(choice) == "3":
                if self.pokemon_team[2].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.pokemon_team[2]
                    self.pokemon_team.pop(2)
                    self.pokemon_team.insert(0, self.your_pokemon)
                    input("""
            GO """ + str(self.your_pokemon) + """!""")
                    pokemon.next_action(self)

            elif str(choice) == "4":
                if self.pokemon_team[3].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.pokemon_team[3]
                    self.pokemon_team.pop(3)
                    self.pokemon_team.insert(0, self.your_pokemon)
                    input("""
            GO """ + str(self.your_pokemon) + """!""")
                    pokemon.next_action(self)
                
            elif str(choice) == "5":
                if self.pokemon_team[4].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.pokemon_team[4]
                    self.pokemon_team.pop(4)
                    self.pokemon_team.insert(0, self.your_pokemon)
                    input("""
            GO """ + str(self.your_pokemon) + """!""")
                    pokemon.next_action(self)
            
            elif str(choice) == "6":
                if self.pokemon_team[5].knocked_out == True:
                    input("""
            You can not battle with a fainted pokemon.""")
                    trainer.switch_pokemon(self)

                else:
                    self.your_pokemon = self.pokemon_team[5]
                    self.pokemon_team.pop(5)
                    self.pokemon_team.insert(0, self.your_pokemon)
                    input("""
            GO """ + str(self.your_pokemon) + """!""")
                    pokemon.next_action(self)

#=============================================================================================================================================#
#                                                          STORY CLASS                                                                      #
#=============================================================================================================================================#

class story():

    def __init__(self,pokedex):
        self.pokedex = pokedex

tackle = {"name": "Tackle", "damage":40, "accuracy":100, "type":"normal", "inflict damage":True}
vine_whip = {"name": "Vine Whip", "damage":40, "accuracy":100, "type":"grass", "inflict damage":True}
ember = {"name": "Ember", "damage":40, "accuracy":100, "type":"fire", "inflict damage":True}
water_gun = {"name": "Water Gun", "damage":40, "accuracy":100, "type":"water", "inflict damage":True}
growl = {"name": "Growl", "damage":40, "accuracy":100, "type":"normal", "inflict damage":False}
none = {"name": ""}

#bulbasaur = pokemon("Bulbasaur", 5, "grass", 45, 45, 49, 49, 45,  False, 0, tackle, vine_whip, growl, tackle)
charmander = pokemon("Charmander", 5, "fire", 39, 39, 52, 43, 65, False, 0, tackle, ember, growl, tackle)
#squirtle = pokemon("Squirtle", 5, "water", 44, 44, 48, 65, 43, False, 0, tackle, water_gun, growl, tackle)
rattata = pokemon("Rattata", 5, "normal", 30, 30, 56, 35, 72, False, 0, tackle, tackle, tackle, tackle)
pikachu = pokemon("Pikachu", 5, "electric", 35, 35, 55, 40, 90, False, 0, tackle, tackle, tackle, tackle)
caterpie = pokemon("Caterpie", 5, "bug", 45, 45, 30, 35, 45, False, 0, tackle, tackle, tackle, tackle)
ekans = pokemon("Ekans", 5, "poison", 35, 35, 60, 44, 55, False, 0, tackle, tackle, tackle, tackle)
jigglypuff = pokemon("Jigglypuff", 5, "fairy", 115, 115, 45, 20, 20, False, 0, tackle, tackle, tackle, tackle)
pidgey = pokemon("Pidgey", 5, "flying", 40, 40, 45, 40, 56, False, 0, tackle, tackle, tackle, tackle)

pokemon_database = [rattata, pikachu, caterpie, ekans, jigglypuff, pidgey]

items = {"potion": 0, "revive": 0, "poke ball": 0}
pokemon_team = []

story = story(pokemon_database)
pokemon_trainer = trainer("Daniel", "Liam", pokemon_team, items, 1000)
new_trainer = trainer.starter(pokemon_trainer, "", "")

#trainer.new_trainer(pokemon_trainer)
