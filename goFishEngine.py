import sys
import random
import numpy as np
from goFishPlayer import *


def print_game(players, deck):
    for player in players:
        print(player)
    print("Deck:",deck)

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
    cards_per_hand = 7 if (num_players <= 3) else 5
    # Distribute cards
    for _ in range(cards_per_hand):
        for i in range(num_players):
            if (len(cards) == 0): break
            hands[i].append(cards.pop())

    players = []
    for i in range(num_players):
        players.append(Player(i, hands[i]))
    print_game(players, cards)


    #Play!
    winner = None
    while (not winner):
        for i in range(num_players):
            players[i].play()
