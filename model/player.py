class Player:
    def __init__(self, id, name):
        self.points = None
        self.id = id
        self.name = name

    def add_points(self, amount):
        self.points += amount

    def reset_points(self):
        self.points = 0
