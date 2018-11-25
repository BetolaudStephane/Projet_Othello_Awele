import sys
sys.path.append("..")
import game
import awele
import time
game.game=awele
sys.path.append("Joueurs")
import Humain
import Premier_Coup
import Random
import Horizon1
import Min_Max
import Alpha_Beta
import Alpha_Beta_Strategique
import Alpha_Beta_Train

NBPARTIE=100
joueur1 = Alpha_Beta_Train
joueur2 = Alpha_Beta

def saisieCoup(jeu):
    j=game.getJoueur(jeu)
    if(j==1):
        j=joueur1
    else:
        j=joueur2

    coup=j.saisieCoup(game.getCopieJeu(jeu))
    return coup

def saisieCoupTr(jeu,ev):
    j=game.getJoueur(jeu)
    if(j==1):
        j=joueur1
    else:
        j=joueur2

    coup=j.saisieCoup(game.getCopieJeu(jeu),ev)
    return coup

def Entrainement(ev,epsi):
    t1=time.time()
    for i in range(0,len(ev)):
        ratio=0
        challenger = jouentrainement(ev)
        j=0
        
        while j< 10:
            ratio=jouentrainement(ev)    
            if challenger<ratio:
                ev[i]=ev[i]-epsi
            if challenger >= ratio:
                ev[i]=ev[i]+epsi
                    
            j=j+1
    print ev
    print time.time()-t1

def jouentrainement(ev):
    global joueur2
    global joueur1
    nbrepartie=0
    j1=0
    j2=0
    eg=0
    switch=1
    
    while(nbrepartie<NBPARTIE):
        if (nbrepartie==(NBPARTIE/2)):    
            s=joueur1
            joueur1=joueur2
            joueur2=s
            a=j1
            j1=j2
            j2=a
            switch=2
            
        jeu=game.initialiseJeu()
        it=0
        
        while((it<100)and (not(game.finJeu(jeu)))):
            if (it<4):
                coup=Random.saisieCoup(game.getCopieJeu(jeu))
                game.joueCoup(jeu,coup)
            else :
                if(game.getJoueur(jeu)==switch):
                    coup=saisieCoupTr(jeu,ev)
                else:
                    coup=saisieCoup(jeu)
                game.joueCoup(jeu,coup)
            it+=1
        g=game.getGagnant(jeu)
        
        if (g==1):
            j1+=1
        if(g==2):
            j2+=1
        if(g==0):
            eg+=1    
        nbrepartie+=1

        if (nbrepartie==NBPARTIE):
            s=joueur2   
            joueur2=joueur1
            joueur1=s
            

    return j2-j1

Entrainement([1.0, 1.0, 1.0, 1.0],0.5)
