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
import Alpha_Beta_Strategique1

NBPARTIE=100
joueur1 = Alpha_Beta_Strategique 
joueur2 = Alpha_Beta_Strategique1

def saisieCoup(jeu):
    j=game.getJoueur(jeu)
    if(j==1):
        j=joueur1
    else:
        j=joueur2

    coup=j.saisieCoup(game.getCopieJeu(jeu))
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
    nbrepartie=0
    j1=0
    j2=0
    eg=0
    tj1=0
    tj2=0
    tt=time.time()
    
    while(nbrepartie<NBPARTIE):
        if (nbrepartie==(NBPARTIE/2)):
            global joueur2
            global joueur1

            print("score mi-temps("+ str(nbrepartie) +" partie):\nj1: "+str(j1)+" \nscore j2: " +str(j2) +"\nnb d'equalite : " +str(eg)+"\n")
            s=joueur1
            joueur1=joueur2
            joueur2=s
            a=j1
            j1=j2
            j2=a

            a=tj1
            tj1=tj2
            tj2=a
            
        jeu=game.initialiseJeu()
        it=0
        
        while((it<100)and (not(game.finJeu(jeu)))):
            if (it<4):
                coup=Random.saisieCoup(game.getCopieJeu(jeu))
                game.joueCoup(jeu,coup)
            else :
                t1=time.time()
                coup=saisieCoup(jeu)
                if game.getJoueur(jeu)==1:
                    tj1+=time.time()-t1
                else:
                    tj2+=time.time()-t1
                game.joueCoup(jeu,coup)
            it+=1
        g=game.getGagnant(jeu)
        tj1=tj1/it
        tj2=tj2/it
        
        if (g==1):
            j1+=1
        if(g==2):
            j2+=1
        if(g==0):
            eg+=1    
        nbrepartie+=1
    
    tt=time.time()-tt
    print("score final :\nj1: "+str(j2) +"temps/coup="+str(tj2)+"\nj2: " +str(j1)+"temps/coup="+str(tj2)+"\nnb d'equalite : " +str(eg))

joueplsr()
