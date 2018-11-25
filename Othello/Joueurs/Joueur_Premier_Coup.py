import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
    i=game.getCoupsValides(jeu)

    return i[0]
