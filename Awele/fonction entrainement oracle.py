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
eleve   = Alpha_Beta_Train
maitre  = Alpha_Beta_Strategique
sparing = Alpha_Beta


def Normaliser(ev):
    for i in ev:
        s=s+i

    for i in range(0,len(ev)):
        ev[i]=ev[i]/s
                                                                           
def Entrainement(ev,alpha):
    nbrepartie=0
    j1=0
    j2=0
    it=0
    j=1
    while(nbrepartie<NBPARTIE):
        if (nbrepartie==NBPARTIE/2):
            j=2
        jeu=game.initialiseJeu()
        
        while ( it<100 or game.finJeu(jeu) ):
            if(game.getJoueur==j):
                coupElv=eleve.saisieCoup(game.getCopieJeu(jeu),ev)
                coupM=maitre.saisieCoup(game.getCopieJeu(jeu))
                if(coupElv==coupM):
                    game.saisieCoup(coupElv)
                else:
                     print "mauvais"
                     
                game.saisiecoup( eleve.saisieCoup(game.getCopieJeu(jeu),ev) )
            else:
                game.saisieCoup( sparing.saisieCoup(jeu) );             
            it+=1

        j=1
        nbrepartie+=1
        if (g==1):
            j1+=1
        if (g==2):
            j2+=1
        if (g==0):
            eg+=1    
        nbrepartie+=1
    print("score final :\nj1: "+str(j2) +"\nj2: " +str(j1)+"\nnb d'equalite : " +str(eg))
    print ev
        

Entrainement([13.0, 1.0, -2.0, 6.0],0.5)
