

class Player():
    def __init__(self, number, cards):
        self.cards = cards
        self.number = number
        
    def __str__(self):
        return "Player {}: {} cards | {}".format(str(self.number),len(self.cards),str(self.cards))