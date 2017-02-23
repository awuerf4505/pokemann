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

    def execute_move(self, move, target):
        pass

    def apply_damage(self, amount):
        pass

    def draw(self):
        pass


class Move:

    def __init__(self, name, kind, powerpoint, power, accuracy):

        self.name = name
        self.kind = kind
        self.powerpoint = powerpoint
        self.power = power
        self.accuracy = accuracy

    def get_effectiveness(self, target):
        if self.kind == 'teacher' and target.kind == 'student':
            effectiveness = 1.5
        elif self.kind == 'student' and target.kind == 'teacher':
            effectiveness = 0.5
        elif self.kind == 'student' and target.kind == 'administrator':
            effectiveness = 0.5
        elif self.kind == 'teacher' and target.kind == 'administrator':
            effectiveness = 1.5
        elif self.kind == 'administrator' and target.kind == 'student':
            effectiveness = 2.5
        elif self.kind == 'administrator' and target.kind == 'teacher':
            effectiveness = 2.5
        else:
            effectiveness = 1.0

    def get_damage(self, attacker, target):
        p = self.power
        a = attacker.attack
        d = target.defense
        e = get_effectiveness(target)
        return p * a / d * e 
    

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

    # Create some Pokemann(s)
    coopasaur = Pokemann("coopasaur", "teacher", 30, 20, 50, 30, [homework, pop_quiz, id_violation], "coopasaur.png")
    mayfieldarow = Pokemann("mayfieldarow", "administrator", 30, 20, 50, 30, [dress_code, id_violation, lecture], "mayfieldarow.png")
    andrewag = Pokemann("andrewag", "student", 30, 20, 50, 30, [excessive_talking, disruptive_behavior, homework], "andrewag.png")
