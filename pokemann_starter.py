import random
class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, catch_rate, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
        self.catch_rate = catch_rate
        self.moves = moves # this is a list of Move objects
        self.image = image # path to image file

        self.fainted = False
        self.current_health = health
        


    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                    
        return result
        
    def execute_move(self, move, target):
        available = self.get_available_moves()

        if self.fainted:
            print("Error: Your Pokemann, " + self.name + " is fainted!")

        elif move not in available:
            print("Error: " + move.name + " is not available.")
        else:
            r = random.randint(1, 100)

            if r <= move.accuracy:
                damage = move.calculate_damage(self, target)
                target.take_damage(damage)
                print(move.name + " hits " + target.name + " for " + str(damage) + ".")
            else:
                print(move.name + " missed!")

            move.remaining_power -= 1
                      
    def take_damage(self, amount):
        self.current_health -= amount

        if self.current_health <= 0:
            self.faint()
            
    def faint(self):
        self.current_health = 0
        self.fainted = True
        print(self.name + " is fainted.")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not more than the base health. 
        """
        self.current_health += amount

        if self.current_health > self.health:
            self.current_health = self.health
        print(self.name + "'s health is now {}/{}.".format(self.current_health, self.health))
        

    def restore(self):
        """
        Restores all health and resets powerpoint for all moves.
        """
        self.heal(self.health)
        for m in self.moves:
            m.restore()
        

    def draw(self):
        pass
    
                  
    def get_move(self):
        """
        This might only be used by computer controlled Pokemann. Perhaps
        'better' Pokemann could be smarter about the random move they choose.
        """
        available = self.get_available_moves()
        return random.choice(available)

                      
class Move:

    STRONG = 2.0
    NORMAL = 1.0
    WEAK = 0.5
        
    effectiveness = {
            ('student' ,'administrator'): STRONG,
            ('student' ,'student'): NORMAL,
            ('student', 'teacher'): WEAK,
            ('teacher', 'student'): STRONG,
            ('teacher' ,'teacher'): NORMAL,
            ('teacher' ,'administrator'): WEAK,
            ('administrator' ,'teacher'): STRONG,
            ('administrator', 'administrator'): NORMAL,
            ('administrator', 'student'): WEAK
            }

    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

        self.remaining_power = powerpoint


    def calculate_damage(self, attacker, target):
        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]
        
        return round(p * a / d * e) 
    
    def restore(self):
        """
        Resets remaing_power to starting powerpoint.
        """
        self.remaining_power = self.powerpoint
        
        
class Character:
    
    def __init__(self, name, party, image):
        self.name = name
        self.party = party
        self.image = image

    def get_available_pokemann(self):
        """
        Returns a list of all unfainted Pokemann belonging to a character.
        """
        result = []
        for p in self.party:
            if p.current_health == 0:
                p.fainted = True
            if not p.fainted:
                result.append(p.name)

        return result

    def restore(self):
        for p in self.party:
            p.restore()
            
    
    def get_active_pokemann(self):
        available = self.get_available_pokemann()

        if len(available) > 0:
            return available[0]
        else:
            return None
        
    
    def set_active_pokemann(self, swap_pos):
        """
        Moves pokemann to first position [0] in the pokemann list by exchanging it with
        pokemann located at swap_pos.
        """
        pass
    
    def draw(self):
        pass

class Player(Character):

    def __init__(self, name, party, image):
        Character.__init__(self, name, party, image)
        
        self.computer = []
        self.pokeballs = 0
        self.image = image
        self.party = self.party


    def catch(self, target):
        """
        Can only be applied to wild pokemann. Determine a catch by generating a random
        value and comparing it to the catch_rate. If a catch is successful, append the
        target to the player's pokemann list. However, if the pokemann list already
        contains 6 pokemann, add the caught target to the players computer instead.
        Pokemann sent to the computer will be fully restored, but other caught pokemann
        will remain at the strenght they were caught. Decrease the player's pokeball
        count by 1 regardless of success.
        """
        r = random.randint(1, 100)
        if self.pokeballs != 0:
            self.pokeballs -= 1
            if r <= target.catch_rate:
                    if len(self.party) >= 6:
                        self.computer.append(target)
                        for n in self.computer:
                            n.restore()
                        print("You caught " + target.name + ".")
                    else:
                        self.party.append(target)
                        print("You caught " + target.name + ".")
            else:
                print("It got away")
        else:
            print("No Pokeballs Remaining")
             

    def run(self, target):
        """
        Can only be applied in the presence of a wild pokemann. Success is determined by
        comparing speeds of the player's active pokemann and the wild pokemann. Incoroporate
        randomness so that speed is not the only factor determining success.
        Return True if the escape is successful and False otherwise.
        """

        corn = self.get_active_pokemann()
        
        r = random.randint(1,100)
        if r <= 50:
            return corn.speed >= target.speed
            print("You ran away!")
        else:
            return False
            print("You failed to do the one thing that is innate to all living/active organisms on this globular rock, water, plasma, matteristic sphere that humans call their place of origin...run ya idiot")
            
        

class NPC(Character):

    def __init__(self, name, party, image):
        Character.__init__(self, name, party, image)

class Game:

    def __init__(self):
        pass

        
if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 10, 10, 100)
    pop_quiz = Move("Pop quiz", "teacher", 3, 30, 2)
    lecture = Move("Lecture", "teacher", 1, 15, 60)
    teacher_strike = Move("Teacher Strike", "teacher", 20, 60, 45)
    complaining = Move("Complaining", "teacher", 80, 10, 100)

    phone_out = Move("Phone put during lesson", "student", 8, 10, 100)
    no_hw = Move("No HW", "student", 5, 30, 60)
    talking_back = Move("Talking Back", "student", 2, 60, 45)
    complaining = Move("Complaining about social life", "student", 5, 30, 60)

    ask_id = Move("Ask for ID", "administrator", 5, 10, 100)
    call = Move("Call Parents", "administrator", 4, 40, 70)
    expulsion = Move("Expulsion", "administrator", 1, 80, 35)
    fired = Move("Fire Staff Member", "administrator", 1, 80, 35)
    restrict_lunch = Move("Restrict Lunchtime", "administrator", 4, 40, 70)

    # Create some Pokemann(s)
    coopasaur = Pokemann("Coopasaur", "teacher", 30, 20, 50, 100, 100, [homework, pop_quiz, teacher_strike], "coopasaur.png")
    cookmander = Pokemann("Cookmander", "teacher", 30, 20, 43, 100, 5, [lecture, teacher_strike, homework], "cookmander.png")
    vincolairy = Pokemann("Vincolairy", "teacher", 30, 20, 78, 120, 100, [lecture, teacher_strike, homework], "vincolairy.png")
    mayfieldarow = Pokemann("Mayfieldarow", "administrator", 34, 20, 50, 90, 100, [call, teacher_strike, lecture], "mayfieldarow.png")
    andrewag = Pokemann("Andrewag", "student", 30, 20, 34, 150, 100, [talking_back, complaining, homework], "andrewag.png")
    caseypuff = Pokemann("Caseypuff", "student", 30, 20, 75, 170, 100, [talking_back, complaining, homework], "caseypuff.png")
    colboreon = Pokemann("Colboreon", "student", 30, 20, 64, 80, 100, [talking_back, complaining, homework], "colboreon.png")
    blakachu = Pokemann("Blakachu", "student", 30, 20, 37, 130, 100, [talking_back, complaining, homework], "blakachu.png")
    zoeotto = Pokemann("Zoeotto", "student", 30, 20, 82, 100, 100, [talking_back, complaining, homework], "zoeotto.png")
    morganyta = Pokemann("Morganyta", "student", 30, 20, 86, 160, 100, [talking_back, complaining, homework], "morganyta.png")
    katlevee = Pokemann("Katlevee", "student", 30, 20, 78, 140, 50, [talking_back, complaining, homework], "katlevee.png")
    marcelax = Pokemann("Marcelax", "student", 30, 20, 25, 30, 100, [talking_back, complaining, homework], "marcelax.png")
    
    pat = Player("Pat Riotum", [coopasaur, andrewag, caseypuff, blakachu], "pat.png")

    rocket = NPC("Team Rocket", [colboreon, zoeotto, morganyta, cookmander], "rocket.png")
    jessie = NPC("Jessie", [vincolairy, mayfieldarow, katlevee, marcelax], "jessie.png")

    # Create a game
    g = Game()
 
