import sys
sys.path.append("../..")
import game
PRONF=4
n=0


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
    alpha=-5000000
    beta=5000000
    challenger=0
    
    i=0
    if(joueur==1):
        i=len(L)-1
    ok=0
    while(ok==0):
        l=estimation(game.getCopieJeu(jeu),L[i],1,joueur,alpha,beta)
        if(l>alpha):
            alpha=l
            challenger=i
        if(joueur==1):
            i-=1
            if(i<0):
                ok=1
        else:
            i+=1
            if(i>=len(L)):
                ok=1
        #J.append(l)
        #jeu2=game.getCopieJeu(jeu)



    #while i< len (J):
    #    if(J[challenger]<J[i]):
    #        challenger=i
    #    i=i+1
        
    return L[challenger]


def estimation(jeu,coup,prf,joueur,alpha,beta):
    global n
    game.joueCoup(jeu,coup)
    if game.finJeu(jeu):
        n=n+1
        g=game.getGagnant(jeu)
        if g==joueur:
            return 100000
        elif g==0:
            return -100
        else:
            return -100000
    elif prf>=PRONF:
        n=n+1
        return evaluation(jeu,coup,joueur)
            
    else:
        L=game.getCoupsValides(jeu)
        
        if(joueur==game.getJoueur(jeu)):
            val = -5000000
            for i in L:
                n=n+1
                jeu2=game.getCopieJeu(jeu)
                val = max(val, estimation(jeu2,i,prf+1,joueur,alpha,beta))
                if val >= beta:
                    return val+1
                alpha = max(val, alpha)
            return val
        else:
            val = 5000000
            for i in L:
                n=n+1
                jeu2=game.getCopieJeu(jeu)
                val = min(val, estimation(jeu2,i,prf+1,joueur,alpha,beta))
                if val <= alpha:
                    return val-1
                beta = min(val, beta)
            return val
            
            

def saisieCoup(jeu):    
    coup=decision(jeu)
    #print n
    return coup



