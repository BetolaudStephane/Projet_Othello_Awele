import sys
sys.path.append("../..")
import game


def evaluation(jeu,coup):
    j=game.getJoueur(jeu)
    game.joueCoup(jeu,coup)
    L=game.getScores(jeu)
    
    if j==1:
        a=L[0]
    else:
        a=L[1]
    return a

def decision(jeu):
    L= game.getCoupsValides(jeu)
    J=[]
    jeu2=game.getCopieJeu(jeu)

    for i in range(0,len(L)):
        game.joueCoup(jeu2,L[i])
        l=evaluation(game.getCopieJeu(jeu),L[i])
        J.append(l)
        jeu2=game.getCopieJeu(jeu)

    challenger=0
    i=1

    while i< len (J):
        if(J[challenger]<J[i]):
            challenger=i
        i=i+1

    return L[challenger]

def saisieCoup(jeu):
    coup=decision(jeu)
    return coup
