import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu-> coup
        retourne un coup a jouer
    """
    c=input("joueur"+str(game.getJoueur(jeu))+": quelle colonne?")
    d=input("joueur"+str(game.getJoueur(jeu))+": quelle ligne?")
    coup=[d,c]

    while(not(game.coupValide(jeu,coup))):
        
        c=input("  num colonne?")
        d=input("coup non valide recommencer num ligne?")
        coup=(d,c)

    return coup
    
