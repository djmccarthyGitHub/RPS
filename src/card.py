class Card:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.title}: {self.description}"

class Rock(Card):
    def __init__(self):
        self.title = "Rock"
        self.description = "A rock is a naturally occurring solid mass composed of one or more minerals"

class Paper(Card):
    def __init__(self):
        self.title = "Paper"
        self.description = "a thin sheet made usually from rags, wood, straw, or bark"

class Scissors(Card):
    def __init__(self):
        self.title = "Scissors"
        self.description = "a cutting device consisting of two blades, each with a ring-shaped handle, which are joined in the middle"