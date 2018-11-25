import sys
import time
sys.path.append("..")
import game
import othello
game.game=othello
sys.path.append("Joueurs")
import joueur_humain
import joueur_premier_coup
import Horizon1
import Alpha_Beta
import Min_Max
import joueur_alea
import Alpha_Beta_Strategique
import AI_weapon_train


NBPARTIE=100
joueur1 = Min_Max
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


def joue():
    jeu=game.initialiseJeu()
    it=0
    while((it<100)and (not game.finJeu(jeu))):
        game.affiche(jeu)
        coup=saisieCoup(jeu)
        game.joueCoup(jeu,coup)
        it+=1

    game.affiche(jeu)
    print("gagnant="+str(game.getGagnant(jeu)+":"+ str(game.getScore(jeu))))

    return jeu
        
def joueplsr():
    tf=time.time()
    nbrepartie=0
    j1=0
    j2=0
    eg=0
    tj1=0
    tj2=0
    
    while(nbrepartie<NBPARTIE):
        if (nbrepartie==(NBPARTIE/2)):
            global joueur2
            global joueur1

            print("score mi-temps("+ str(nbrepartie) +" partie):\nj1: "+str(j1)+" score j2: " +str(j2) +" nb d'equalite : " +str(eg)+"\n")
            s=joueur1
            joueur1=joueur2
            joueur2=s
            a=j1
            j1=j2
            j2=a

            tj1=a
            tj1=tj2
            tj2=a
            
        jeu=game.initialiseJeu()
        it=0
        switch=0
        while((it<100)and (not(game.finJeu(jeu)))):
            if (it<4):
                coup=joueur_alea.saisieCoup(game.getCopieJeu(jeu))
                game.joueCoup(jeu,coup)
            else :
                t=time.time()
                coup=saisieCoup(jeu)
                if game.getJoueur(jeu)==1:
                    tj1=tj1+time.time()-t
                else:
                    tj2=tj2+time.time()-t
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
    print("score final :\nj1: "+str(j2)+" temp/coup="+str(tj2/NBPARTIE)+"\nj2: " +str(j1)+"temp/coup="+str(tj1/NBPARTIE) +" nb d'equalite : " +str(eg))
    print time.time()-tf
    
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
                coup=joueur_alea.saisieCoup(game.getCopieJeu(jeu))
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
            

    return j2

def stat(ev):
    tab=[]
    i=0
    while i<6:
        tab.append(jouentrainement(ev))
        ev[4]=ev[4]+1
        i=i+1
    print tab
print str(joueur1)
joueplsr()


#Entrainement([1,35,-15,1,3],0.1)
#[1.0, 35.60000000000001, -14.8, 0.40000000000000013, 2.8]
#-14508.2720001
