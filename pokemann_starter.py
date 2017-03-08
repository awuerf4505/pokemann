import random
class Pokemann:

    def __init__(self, name, kind, attack, defense, speed, health, moves, image):

        self.name = name
        self.kind = kind
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.health = health
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
            print("Error: " + self.name + " is fainted!")
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
        self.current_health <= 0
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not more than the base health.
        """
        self.current_health += amount
        print(self.name + "'s has been healed.")
        if self.current_health > self.health:
            self.current_health = self.health
        self.fainted = False
        pass

    def restore(self):
        self.current_health = self.health
        print("Power Restored")
        

    def draw(self):
        pass
    
    def get_available_moves(self):
        result = []
                  
        for m in self.moves:
            if m.remaining_power > 0:
                  result.append(m)
                  
        return result
                  
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
        self.remaining_power = self.moves
        print("Power Restored")
        
        
class Character:
    
    def __init__(self, name, pokemann, image):
        self.name = name
        self.pokemann = pokemann
        self.image = image

    def get_available_pokemann(self):
        """
        Returns a list of all unfainted Pokemann belonging to a character.
        """
        pass
    
    def get_first_pokemann(self):
        """
        Returns the first [0] unfainted character in the pokemann list.
        """
        pass
    
    def set_first_pokemann(self, swap_pos):
        """
        Moves pokemann to first position [0] in the pokemann list by exchanging it with
        pokemann located at swap_pos.
        """
        pass
    
    def draw(self):
        pass

class Player(Character):

    def __init__(self, name, pokemann):
        Character.__init__(self, name, pokemann)
        
        self.collection = []
        self.pokeballs = 0

class Opponent(Character):

    def __init__(self, name, pokemann):
        Character.__init__(self, name, pokemann)

class Game:

    def __init__(self):
        pass

    def select_pokemann(self, character):
        """
        1) Generate a menu which shows a numbered list of all characters along with status (health).
        2) Have the player select a character.
        3) Move the selected character to position [0] in the characters list.
        """
        pass

    def select_random_pokemann(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        available_moves = pokemann.get_available_moves()
        return random.choice(available_moves)
    
    def select_move(self, pokemann):
        """
        1) Generate a menu which shows a numbered list all available moves for a pokemann.
        2) Have the player select a move.
        3) Return the selected move.
        """

        available = pokemann.get_available_moves()
        
        print("Select a move:")
        
        for i, move in enumerate(available):
            print(str(i) + ") " + move.name)

        n = input("Your choice: ")
        n = int(n)
        
        return available[n]

    def select_random_move(self, pokemann):
        """
        Returns a random available move from the pokemann. This will probably only be used
        by computer controlled pokemann.
        """
        pass

    def fight(self, player_pokemann, target_pokemann):
        """
        This controls the logic for a single round in a fight whether in context of a battle
        or with a wild pokemann.
        
        1. Select player_move (use select_move)
        2. Select target_move (use select_random_move)
        3. Compare speeds of player_pokemann and target_pokemann
            If player_pokemann.speed > target_pokemann.speed, set first = player_pokemann,
            second = target_pokemann. Otherwise, set first = target_pokemann, second = player_pokemann
            If speeds are equal, assign first and second randomly.
        4. Call
            first.execute_move(move, second)
        5. If second is still unfainted, call
            second.execute_move(move, first)
        (Once we have an actual game, we'll need to devise a way to remove fainted targets.)
        """
        pass
    
    def catch(self, target):
        """
        Can only be applied to wild pokemann. Determine a catch by generating a random
        value based on the target health. If a catch is successful, add the target to the
        player's collection. Decrease the player's pokeball count by 1 regardless of success.
        (Perhaps pokeballs kind could be incorporated into the probability at some point.)
        """
        pass

    def encounter(self, player, target):
        """
        This function controls all logic when encountering a wild pokemann. Options are to
        fight, catch, or ignore.
        Use a loop so that this continues until a pokemann is fainted, caught, or the
        target is ignored.
        """
        pass
    

    def battle(self, player, opponent):
        """
        This function controls all battle logic including decisions to reorder pokemann,
        fight, use potions, and whatever else happens in Pokebattles.
        Use a loop so that this continues until all characters for either the player or
        opponent are fainted.
        """
        pass
    
    def loop(self):
        pass
    
        # get input

        # do logic stuff

        # draw stuff

    '''def __init__(self, name, kind, powerpoint, power, accuracy):'''

    '''    def __init__(self, name, kind, attack, defense, speed, health, moves, image):'''

if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 2, 10, 100)
    pop_quiz = Move("Pop quiz", "teacher", 3, 30, 45)
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
    coopasaur = Pokemann("coopasaur", "teacher", 10, 20, 50, 30, [homework, pop_quiz, lecture], "coopasaur.png")
    mayfieldarow = Pokemann("mayfieldarow", "administrator", 30, 20, 50, 30, [ask_id, fired, call], "mayfieldarow.png")
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, [phone_out, no_hw, complaining], "andrewag.png")
