import sys
sys.path.append("../..")
import game
PRONF=2
max_val=-50
min_val=50
cpt = 0   

def evaluation(jeu,coup, joueur,ev):

    return ev[0]*Score(jeu,coup,joueur)+ev[1]*CaseConsecutif(jeu,coup,joueur)+ev[2]*Piege(jeu,joueur)+ev[3]*Krou(jeu,coup,joueur)
    
def Score(jeu,coup,joueur):
    L=game.getScores(jeu)
    
    if joueur==1:
        return L[0]-L[1]
    else:
        return L[1]-L[0]
    
def CaseConsecutif(jeu,coup,joueur):
    cj = game.getCoupsJoues(jeu)
    i=-6

    while i<0:
        if len(cj)<15 and (len(cj)+i)<0 : #si in est plus en debut et si il n'y a plus de coup precedent
            return 0
        elif abs(cj[i][1]-coup[1])==1: #si c'est un voisin des deux dernier
            return 0
        i=i+2
    return 1

def Piege(jeu,joueur):
    L=game.getScores(jeu)
    eval=0
    j1=0
    j2=0

   
    if(L[0]+L[1]>48-15):
        for i in range(0,6):
            j1=game.getCaseVal(jeu,0,i)
            j2=game.getCaseVal(jeu,1,i)
         
        if(joueur==1):
            """
            if game.getCaseVal(jeu,1,1)<=1 and game.getCaseVal(jeu,1,0)==1:
                    eval=eval+2
            """
            eval=eval+j1-j2
            
        else:
            """
            if game.getCaseVal(jeu,0,4)<=1 and game.getCaseVal(jeu,0,5)==1:
                    eval=eval+2
            """
            eval=eval+j2-j1
    return eval
"""
def Piege(jeu,coup,joueur):
    L=game.getScores(jeu)
    eval=0

    
    if(L[0]+L[1]>48-15):
        if(joueur==1):
            if game.getCaseVal(jeu,1,1)<=1 and game.getCaseVal(jeu,0,0)==1:
                if (coup[1]-game.getCaseVal(jeu,joueur-1,0)) >=0:
                    return 2
                
            
            if game.getCaseVal(jeu,0,0)>=1:
                if coup[1]-game.getCaseVal(jeu,0,coup[1])<0:
                    return 1
                else:
                    return -1
        else:
            if game.getCaseVal(jeu,0,5)<=1 and game.getCaseVal(jeu,0,0)==1:
                if (5-coup[1]-game.getCaseVal(jeu,joueur-1,0)) >=0:
                    return 5
                            
            if game.getCaseVal(jeu,0,0)>=1:
                if 5-coup[1]-game.getCaseVal(jeu,0,coup[1])<0:
                    return 1
                else:
                    return -1
    return 0
            
"""   
def Krou(jeu,coup,joueur):
    eval=0
    for i in range(0,6):
        if game.getCaseVal(jeu,joueur-1,i)>=12:
            eval=eval+1
    return eval
        
         
    return case
    


def decision(jeu,ev): 
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
        l=estimation(game.getCopieJeu(jeu),L[i],1,joueur,alpha,beta,ev)
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


def estimation(jeu,coup,prf,joueur,alpha,beta,ev):
    game.joueCoup(jeu,coup)
    if game.finJeu(jeu):
        g=game.getGagnant(jeu)
        if g==joueur:
            return 100000
        elif g==0:
            return -100
        else:
            return -100000
    elif prf>=PRONF:
        return evaluation(jeu,coup,joueur,ev)
            
    else:
        L=game.getCoupsValides(jeu)
        
        if(joueur==game.getJoueur(jeu)):
            val = -5000000
            for i in L:
                jeu2=game.getCopieJeu(jeu)
                val = max(val, estimation(jeu2,i,prf+1,joueur,alpha,beta,ev))
                if val >= beta:
                    return val+1
                alpha = max(val, alpha)
            return val
        else:
            val = 5000000
            for i in L:
                jeu2=game.getCopieJeu(jeu)
                val = min(val, estimation(jeu2,i,prf+1,joueur,alpha,beta,ev))
                if val <= alpha:
                    return val-1
                beta = min(val, beta)
            return val
            
            

def saisieCoup(jeu,ev):    
    coup=decision(jeu,ev)
    return coup



