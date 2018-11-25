import sys
sys.path.append("../..")
import game
#joueur=game.getJoueur


def Min(L):
    min=L[0]
    for i in L:
        if min > i:
            min=i
    return min

def Max(L):
    max=L[0]
    for i in L:
        if max < i:
            max=i
    return max


def evaluation(jeu,coup,joueur):
    L=game.getScores(jeu)
    
    if joueur==1:
        return L[0]-L[1]
    else:
        return L[1]-L[0]

def decision(jeu):
    joueur = game.getJoueur(jeu)
    L= game.getCoupsValides(jeu)
    J=[]
    #jeu2=game.getCopieJeu(jeu)
    
    for i in range(0,len(L)):
        #game.joueCoup(jeu2,L[i])
        l=estimation(game.getCopieJeu(jeu),L[i],1,joueur)
        J.append(l)
        #jeu2=game.getCopieJeu(jeu)

    challenger=0
    i=1

    while i< len (J):
        if(J[challenger]<J[i]):
            challenger=i
        i=i+1

    return L[challenger]


def estimation(jeu,coup,prf,joueur):
    game.joueCoup(jeu,coup)
    #L= game.getCoupsValides(jeu)
    if game.finJeu(jeu):
        g=game.getGagnant(jeu)
        if g==joueur:
            return 100000
        elif g==0:
            return -100
        else:
            return -100000
    elif prf>=2:
        return evaluation(jeu,coup,joueur)
            
    else:
        L=game.getCoupsValides(jeu)
        m=[]
        for i in L:
            jeu2=game.getCopieJeu(jeu)
            #game.joueCoup(jeu2,i)
            m.append(estimation(jeu2,i,prf+1,joueur))

        if game.getJoueur(jeu)==joueur:
            return max(m)
        else:
            return min(m)

def saisieCoup(jeu):
    coup=decision(jeu)
    return coup
        
