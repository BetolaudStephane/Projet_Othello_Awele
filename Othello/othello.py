import sys
sys.path.append("..")
sys.path.append("../..")
import game


def initPlateau():
    """void->List[List[nat]]
        Retourne un nouveau plateau de jeu
    """
    return [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def finJeu(jeu):
    """jeu->bool
        Retourne vrai si il n'y a plus aucun coup valide 
    """
    return len(game.getCoupsValides(jeu))==0

def initScores():
    """void->Pair(int int]
        Retourne les scores initiaux pour le jeu
    """
    return [2,2]

def entourageVide(jeu,case):
    """Pair[nat nat] -> Set[str]
        Retourne l'ensemble des chaines de caracteres reppresentant des cases vides contigues a la case passee en parametre
    """
    ret=set()
    l=case[0]
    c=case[1]
    if(l>0):
        if(game.getCaseVal(jeu,l-1,c)==0):
            ret.add(str([l-1,c]))
        if(c>0):
            if(game.getCaseVal(jeu,l-1,c-1)==0):
                ret.add(str([l-1,c-1]))
        if(c<7):
            if(game.getCaseVal(jeu,l-1,c+1)==0):
                ret.add(str([l-1,c+1]))
    if(l<7):
        if(game.getCaseVal(jeu,l+1,c)==0):
            ret.add(str([l+1,c]))
        if(c>0):
            if(game.getCaseVal(jeu,l+1,c-1)==0):
                ret.add(str([l+1,c-1]))
        if(c<7):
            if(game.getCaseVal(jeu,l+1,c+1)==0):
                ret.add(str([l+1,c+1]))
    if(c>0):
        if(game.getCaseVal(jeu,l,c-1)==0):
            ret.add(str([l,c-1]))
    if(c<7):
        if(game.getCaseVal(jeu,l,c+1)==0):
            ret.add(str([l,c+1]))
    return ret

def coups(jeu):
    """jeu->List[coup]
        Return une liste de coups pour le jeu tels qu'ils concernent chacun une case vide qui touche une case ou un pion de l'adversaire est place
    """
    j=game.getJoueur(jeu)
    if(j==2):
        j=1
    else:
        j=2
    s={x for l in range(0,8) for c in range(0,8) for x in entourageVide(jeu,[l,c])  if game.getCaseVal(jeu,l,c)==j}
    return [eval(x) for x in s]

def checkEncadrementDirection(jeu,l,c,sud,est):
    """jeu*nat*nat*nat*nat*nat->bool
        Verifie si a partir d'une case l+sud,c+est de l'adversaire on peut trouver des pions au joueur courant dans la direction donnee avant de tomber sur une case vide
        Retourne False si l,c n'appartient pas a l'adversaire
        si sud est 1, on se deplace vers le bas
        si sud est -1, on se deplace vers le haut
        si est est 1, on se deplace vers la droite
        si est est -1, on se deplace vers la gauche
    """
    l+=sud
    c+=est
    if(l>7)or(l<0)or(c>7)or(c<0):
            return False
    j=game.getJoueur(jeu)
    v=game.getCaseVal(jeu,l,c)
    if(v==j) or (v==0):
        return False
    while True:
        l+=sud
        c+=est
        #print str(l)+','+str(c)
        if(l>7)or(l<0)or(c>7)or(c<0):
            return False
        v=game.getCaseVal(jeu,l,c)
        if(v==0):
            return False
        if(v==j):
            return True
    return False

def trouveEncadrements(jeu,coup,tous=True):
    """jeu*coup*bool->List[Pair[nat nat]]
        Retourne la liste de directions dans lesquelles on trouve un encadrement pour le coup
        si tous est False, on s'arrete au premier trouve
    """
    ret=[]
    if checkEncadrementDirection(jeu,coup[0],coup[1],1,1):
        ret.append([1,1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],0,1):
        ret.append([0,1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],-1,1):
        ret.append([-1,1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],-1,0):
        ret.append([-1,0])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],-1,-1):
        ret.append([-1,-1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],0,-1):
        ret.append([0,-1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],1,-1):
        ret.append([1,-1])
        if not tous:
            return ret
    if checkEncadrementDirection(jeu,coup[0],coup[1],1,0):
        ret.append([1,0])
    return ret
    

def listeCoupsValides(jeu):
    """ jeu->List[coup]
        Retourne la liste des coups valides selon l'etat du jeu. Un coup est valide si:
             - La case est vide et touche une case ou un pion de l'adversaire est place (assure par la fonction coups)
             - La case permet d'encadrer au moins une liste de pions de l'adversaire
    """
    cp=coups(jeu)
    return [x for x in cp if len(trouveEncadrements(jeu,x,False))>0]


def finalisePartie(jeu):
    """jeu->void
        Ne fait rien dans le cas de l'othello 
    """

def retournePieces(jeu,coup,direction):
    """jeu * coup* Pair[int int] -> Pair[nat nat]
        Attribue au joueur courant les pieces encadres selon la direction donnee a partir du coup
        Retourne le nombre de pieces perdues ou gagnees par chacun des deux joueurs
        La direction est definie de la meme maniere que dans la fonction checkEncadrement
    """
    ret=[0,0]
    sud=direction[0]
    est=direction[1]
    l=coup[0]
    c=coup[1]
    l+=sud
    c+=est
    if(l>7)or(l<0)or(c>7)or(c<0):
            raise Exception('Pas d encadrement ici!')
    j=game.getJoueur(jeu)
    v=game.getCaseVal(jeu,l,c)
    if(v==j) or (v==0):
        raise Exception('Pas d encadrement ici !')
    game.setCaseVal(jeu,l,c,j)
    if(j==1):
        ret[0]+=1
        ret[1]-=1
    else:
        ret[0]-=1
        ret[1]+=1
    while True:
        l+=sud
        c+=est
        #print str(l)+','+str(c)
        if(l>7)or(l<0)or(c>7)or(c<0):
            raise Exception('Pas d encadrement ici !')
        v=game.getCaseVal(jeu,l,c)
        if(v==0):
            raise Exception('Pas d encadrement ici !')
        #print str(v)+','+str(j)
        if(v==j):
            return ret
        else:
            game.setCaseVal(jeu,l,c,j)
            if(j==1):
                ret[0]+=1
                ret[1]-=1
            else:
                ret[0]-=1
                ret[1]+=1
    return ret
    
    
def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup:
            - Cherche toutes les directions d'encadrement
            - Pour toutes les directions trouvees, lance la fonction retournePieces pour retourner les pieces encadrees
            - Met a jour les scores selon le nombre de pieces retournees
        Hypothese:le coup est valide
    """
    l=trouveEncadrements(jeu,coup)
    a=[retournePieces(jeu,coup,x) for x in l]
    j=game.getJoueur(jeu)
    sc=[0,0]
    if(j==1):
        sc[0]=1
    else:
        sc[1]+=1
    game.setCaseVal(jeu,coup[0],coup[1],j)
    s=reduce(lambda x,y:[x[0]+y[0],x[1]+y[1]],a,sc)
    game.addScore(jeu,1,s[0])
    game.addScore(jeu,2,s[1])
    game.addCoupJoue(jeu,coup)
    game.changeJoueur(jeu)
    game.razCoupsValides(jeu)


