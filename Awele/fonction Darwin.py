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
NBREFONCTIONDEVAL=4
NPERSONNE=4
PROBMUT=0.1

def Monde():
    monde=initialiseMonde()
    monde2=NouvelleGeneration(monde)
    
    print "nouvelle generation"
    print monde2
    
def Tournoi(monde):
    i=0
    tournoi=[]
    tournoi2=[]
    while i+1<NPERSONNE:
        tournoi.append( joue(monde[i],monde[i+1]) )
        i+=1

    
    while len(tournoi)>1:
        tournoi2=[]
        i=0
        while i+1<len(tournoi):
            tournoi2.append( joue(tournoi[i],tournoi[i+1]) )
            i+=1
        tournoi=tournoi2
            
    return tournoi[0]


def NouvelleGeneration(monde):
    NewMonde=[]
    Best=Tournoi(monde)
    print Best
    NewMonde.append(Best)
    for i in range(1,NPERSONNE):
        ev=[]
        #selection parent p1 et p2
        p=monde[int(random.random()*NPERSONNE)]

        for i in range(0,NBREFONCTIONDEVAL):
            if(random.random()<PROBMUT):
                ev.append(random.random() )
            elif(random.random()<0.5):
                ev.append(p[i])
            else:
                ev.append( Best[i] )
                
        NewMonde.append(Normaliser(ev))
        
    return NewMonde


        
def jouepartie(ev1,ev2):
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
    
def joue(ev1,ev2):
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

def Normaliser(ev):
    s=0
    for i in ev:
        s=s+i
    for i in range(0,len(ev)):
        ev[i]=ev[i]/s
    return ev

def initialiseMonde():
    monde=[]
    for i in range(0,NPERSONNE):
        ev=[]
        for i in range (0,NBREFONCTIONDEVAL):
            ev.append(random.random())
        ev=Normaliser(ev)
        monde.append(ev)
    return monde


Monde()


            
        


