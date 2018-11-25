import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu-> coup
        retourne un coup a jouer
    """

    c=input("joueur"+str(game.getJoueur(jeu))+": quelle colonne?")
    coup=[game.getJoueur(jeu)-1,c]

    while(not(game.coupValide(jeu,coup))):
          c=input("coup non valide recommencer")
          coup=(game.getJoueur(jeu)-1,c)
    return coup

