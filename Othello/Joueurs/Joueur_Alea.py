import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):

    i=random.choice(game.getCoupsValides(jeu))

    return i
