
from goFishPlayerModel import Model 

class Player():
    def __init__(self, number, cards, model = Model):
        self.cards = cards
        self.number = number
        self.model = model
        
    def __str__(self):
        return "Player {}: {} cards | {}".format(str(self.number),len(self.cards),str(self.cards))
    
    def play():
        