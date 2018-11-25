import sys
sys.path.append("../..")
import game
PRONF=2
Coin=[[0,0],[7,7],[0,7],[7,0]]
CoteCoin=[[1,1],[0,1],[1,0],[6,0],[6,1],[7,1],[1,6],[1,7],[0,7],[6,6],[6,7],[7,7]]


def evaluation(jeu,coup,joueur,ev):
    return ev[0]*score(jeu,joueur)+ev[1]*VCoin(jeu,joueur)+ev[2]*VCoteCoin(jeu,joueur)+ev[3]*Bord(jeu,joueur)+ev[4]*Mobilite(jeu,joueur)

def score(jeu,joueur):
    L=game.getScores(jeu)
    
    if joueur==1:
        return L[0]-L[1]
    else:
        return L[1]-L[0]



def VCoin(jeu,joueur):
    eval=0
    for i in Coin:
        if game.getCaseVal(jeu,i[0],i[1])==0:
            eval=eval+0
        elif game.getCaseVal(jeu,i[0],i[1])==joueur:
            eval=eval+1
        else:
            eval=eval-1
        
    return eval


def VCoteCoin(jeu,joueur):
    eval=0
    for i in CoteCoin:
    #while i <len(CoteCoin):
        #if (game.getCaseVal(jeu,CoteCoin[i/3][0],getCaseVal(jeu,CoteCoin[i//3][0])
        if game.getCaseVal(jeu,i[0],i[1])==0:
            eval=eval+0
        elif game.getCaseVal(jeu,i[0],i[1])==joueur:
            eval=eval+1
        else:
            eval=eval-1
    return eval

def Bord(jeu,joueur):
    eval=0
    for i in range(2,6):
        for j in [0,7]:
            p=game.getCaseVal(jeu,j,i)
            if(p==joueur):
                eval=eval+1
            elif(p==0):
                continue
            else:
                eval=eval-1
        for j in [0,7]:
            p=game.getCaseVal(jeu,i,j)
            if(p==joueur):
                eval=eval+1
            elif(p==0):
                continue
            else:
                eval=eval-1
        
    return eval

def Mobilite(jeu,joueur):
    return len(game.getCoupsValides(jeu))

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



