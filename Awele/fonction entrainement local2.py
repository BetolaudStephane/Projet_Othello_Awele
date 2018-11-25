# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game
import awele
import time
import random
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

def Entrainement(ev,epsi):
    t1=time.time()
    j=0
    i=0
    evmoins=[]
    evplus=[]

    while i<len(ev):
        j=0
        while j< 20:
            print i
            evmoins=changeValVecteur(ev,i,-epsi)
            evplus=changeValVecteur(ev,i,epsi)
            ev=joueEntrainement(evmoins,evplus)
            print "gg="+str(ev)
            j=j+1
        i=i+1
    print ev
    print time.time()-t1

def changeValVecteur(ev,i,epsi):
    t=0
    evt=[]
    for j in range(0,len(ev)):
        evt.append(ev[j])

    evt[i]=evt[i]+epsi
    print evt
    return evt
    
def joue(ev1,ev2):
    it=0
    jeu=game.initialiseJeu()
    while((it<100)and (not(game.finJeu(jeu)))):
            if (it<4):
                coup=Random.saisieCoup(game.getCopieJeu(jeu))
                game.joueCoup(jeu,coup)
            else :
                if(game.getJoueur(jeu)==1):
                    coup=Alpha_Beta_Train.saisieCoup(jeu,ev1)
                else:
                    coup=Alpha_Beta_Train.saisieCoup(jeu,ev2)
                game.joueCoup(jeu,coup)
            it+=1
    return game.getGagnant(jeu)
    
def joueEntrainement(ev1,ev2):
    nbrepartie=0
    j1=0
    j2=0
    j0=0
    switch=False
    
    while(nbrepartie<NBPARTIE):
        if (nbrepartie==(NBPARTIE/2)):
            
            a=j1
            j1=j2
            j2=a
            switch=True
        
        if(switch):
            g=joue(ev1,ev2)
        if(not(switch)):
            g=joue(ev2,ev1)
        
        if (g==1):
            j1=j1+1
        if (g==2):
            j2=j2+1
        if (g==0):
            j0=j0+1
        nbrepartie+=1
        
            
    if (j1==j2):
        if random.random()<0.5:
            return ev1
        else:
            return ev2
    elif j2-j1<0:
        return ev1
    else:
        return ev2
#[19.0, 4.0, 2.0, 1.0]
Entrainement([19.80, 2.40, 2.80, 1.80],0.20)

