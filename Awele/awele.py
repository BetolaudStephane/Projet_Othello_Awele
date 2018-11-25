import sys
sys.path.append("../..")
import game


def initPlateau():
    """void->List[List[nat]]
        Retourne un nouveau plateau de jeu
    """
    return [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    #return [[1,0,0,0,1,1],[3,4,4,4,4,2]]

def initScores():
    """void->Pair(int int]
        Retourne les scores initiaux pour le jeu
    """
    return [0,0]

def coups(jeu):
    """jeu->List[coup]
        Return une liste de coups pour le jeu
    """
    j=game.getJoueur(jeu)
    return [[j-1,x] for x in range(0,6)]

def listeCoupsValides(jeu):
    """ jeu->List[coup]
        Retourne la liste des coups valides selon l'etat du jeu. Un coup est valide si:
             - La case correspondant au coup appartient bien au joueur courant
             - La case correspondant au coup contient au moins une graine
             - Le coup nourrit l'adversaire si il est affame. 
    """

    
    def estValide(jeu,coup,checkNourrit=True):
        """jeu*coup*bool->bool
        """
        l=coup[0]
        c=coup[1]
        g=game.getCaseVal(jeu,l,c)
        if(g==0):
            return False
        if(checkNourrit):
            if(l==0):
                return (g>c)
            else:
                return (g>(5-c))
        return True
                
        
    cp=coups(jeu)
    affame=adversaireAffame(jeu)
    return [x for x in cp if estValide(jeu,x,affame)]
    

def adversaireAffame(jeu):
    """jeu->bool
        Retourne vrai si l'adversaire n'a aucune graine dans son jeu
    """
    j=game.getJoueur(jeu)
    j=j%2+1
    for i in range(0,6):
        x=game.getCaseVal(jeu,j-1,i)
        if x!=0:
            return False
    return True


def finJeu(jeu):
    """jeu->bool
        Retourne vrai si il n'y a plus aucun coup valide ou si un joueur a manger plus de la moitie des graines
    """
    s=game.getScores(jeu)
    return len(game.getCoupsValides(jeu))==0 or s[0]>=25 or s[1]>=25 or len(game.getCoupsJoues(jeu))>=100
                                                                            

def finalisePartie(jeu):
    """jeu->void
        Met a jour les scores des joueurs en prenant en compte les graines restantes sur le plateau
    """
    p=game.getPlateau(jeu)
    g1=reduce(lambda a,b: a+b,p[0])
    g2=reduce(lambda a,b: a+b,p[1])
    game.addScore(jeu,1,g1)
    game.addScore(jeu,2,g2)
    
def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction distribue
        Hypothese:le coup est valide
    """
    v=game.getCaseVal(jeu,coup[0],coup[1])
    game.setCaseVal(jeu,coup[0],coup[1],0)
    distribue(jeu,coup,v)
    game.addCoupJoue(jeu,coup)
    game.changeJoueur(jeu)
    game.razCoupsValides(jeu)

def nextCase(jeu,case,inv=True):
    """jeu*Pair[nat nat]->Pair[nat nat]
        Retourne la prochaine case sur le plateau, dans le sens inverse des aiguilles d'une montre si inv est vrai, dans le sens des aiguilles d'une montre sinon
    """
    sens=1
    if inv:
        sens=-1
    c=case[1]-1*sens
    if(case[0]==0):
        c=case[1]+(1*sens)
    if(c<0):
        if(case[0]==0):
            return [1,0]
        return [0,0]
    if(c>5):
        if(case[0]==0):
            return [1,5]
        return [0,5]
    return [case[0],c]

            

        
def distribue(jeu,case,nb):
    """ jeu * Pair[nat nat] * nat -> void
    Egraine nb graines (dans le sens inverse des aiguilles d'une montre) en partant de la case suivant la case suivant celle pointee par cellule,
    puis mange ce qu'on a le droit de manger
    Pseudo-code :
        - Distribution des graines dans le sens inverse des aiguilles d'une montre en evitant la case de depart (si nb>=12, on nourrit plusieurs fois les memes cases)
        - Parcours du plateau dans le sens inverse tant qu'on peut manger des graines
    Note: on egraine pas dans la case de depart si on a fait un tour
    Note2: On ne peut pas manger le contenu de plus de 3 cases
    Note3: On ne mange rien si le coup affame l'adversaire
    """
    c=case
    while nb>0:
        c=nextCase(jeu,c)
        if c[0]==case[0] and c[1]==case[1]:
            continue
        game.addCaseVal(jeu,c[0],c[1],1)
        nb-=1

    n=0
    old=[]
    while peutManger(jeu,c):
        v=game.getCaseVal(jeu,c[0],c[1])
        old.append(v)
        game.setCaseVal(jeu,c[0],c[1],0)
        game.addScore(jeu,game.getJoueur(jeu),v)
        n+=1
        c=nextCase(jeu,c,False)

    if (len(old)>0) and adversaireAffame(jeu):
        #print('Adversaire affame, on ne peut pas manger')
        n=1
        while(n<=len(old)):
            c=nextCase(jeu,c,True)
            g=old[-n]
            game.setCaseVal(jeu,c[0],c[1],g)
            #print('on rend '+str(g)+' dans la case '+str(c))
            game.addScore(jeu,game.getJoueur(jeu),-g)  
            n+=1
        
        
    
def peutManger(jeu,c):
    """jeu * Pair[nat nat] -> bool
        Retourne vrai si on peut manger le contenu de la case:
            - c'est une case appartenant a l'adversaire du joueur courant
            - La case contient 2 ou 3 graines
    """
    if c[0]==(game.getJoueur(jeu)-1):
        return False
    v=game.getCaseVal(jeu,c[0],c[1])
    if(v!=2) and (v!=3):
        return False
    return True
