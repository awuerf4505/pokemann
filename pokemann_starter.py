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
                damage = move.get_damage(self, target)
                target.apply_damage(damage)
                print(move.name + " hits " + target.name + " for " + str(damage) + ".")
            else:
                print(move.name + "missed!")

            move.remaining_power -= 1
                      
    def take_damage(self, amount):
        self.current_health -= amount

        if self.current_health <= 0:
            self.faint()
    def faint(self):
        self.current_health = 0
        print(self.name + " fainted!")
                  
    def heal(self, amount):
        """
        Raises current_health by amount but not more than the base health.
        """
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

    def draw(self):
        pass
                      
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

        self.remaining_power = remaining_power


    def get_damage(self, attacker, target):
        p = self.power
        a = attacker.attack
        d = target.defense
        e = self.effectiveness[(self.kind, target.kind)]
        
        return round(p * a / d * e) 
    

if __name__ == '__main__':

    # Make some moves
    homework = Move("Homework", "teacher", 80, 10, 100)
    pop_quiz = Move("Pop quiz", "teacher", 20, 60, 45)
    lecture = Move("Lecture", "teacher", 50, 30, 60)
    teacher_strike = Move("Teacher Strike", "teacher", 20, 60, 45)
    complaining = Move("Complaining", "teacher", 80, 10, 100)

    phone_out = Move("Phone put during lesson", "student", 80, 10, 100)
    no_hw = Move("No HW", "student", 50, 30, 60)
    talking_back = Move("Talking Back", "student", 20, 60, 45)
    complaining = Move("Complaining about social life", "student", 50, 30, 60)

    ask_id = Move("Ask for ID", "administrator", 50, 10, 100)
    call = Move("Call Parents", "administrator", 40, 40, 70)
    expulsion = Move("Expulsion", "administrator", 10, 80, 35)
    fired = Move("Fire Staff Member", "administrator", 10, 80, 35)
    restrict_lunch = Move("Restrict Lunchtime", "administrator", 40, 40, 70)

    # Create some Pokemann(s)
    coopasaur = Pokemann("coopasaur", "teacher", 30, 20, 50, 30, [homework, pop_quiz, lecture], "coopasaur.png")
    mayfieldarow = Pokemann("mayfieldarow", "administrator", 30, 20, 50, 30, [ask_id, fired, call], "mayfieldarow.png")
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, [phone_out, no_hw, complaining], "andrewag.png")
