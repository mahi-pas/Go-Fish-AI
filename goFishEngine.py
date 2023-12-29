import sys
import random
import numpy as np
from goFishPlayer import *

if __name__ == '__main__':
    n = len(sys.argv)
    if (n<2):
        print("Invalid number of arguments! Correct usage: file.py <num-players>")
        quit()

    card_options = []
    for i in ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]:
        for j in  ["♠", "♥", "♦", "♣"]:
            card_options.append(i+j)
    
    cards = card_options.copy()
    np.random.shuffle(cards)

    num_players = int(sys.argv[1])
    hands = [[] for _ in range(num_players)]
    i = 0
    while(len(cards)>0): # Distribute cards
        hands[i].append(cards.pop())
        i+=1
        if (i == num_players): i = 0

    players = []
    for i in range(num_players):
        players.append(Player(i, hands[i]))
        print(players[i])
