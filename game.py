

# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup: Pair[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:N-UPLET[plateau nat List[coup] List[coup] Pair[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]
  
def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
    """
    if(jeu[2]==None):
        majCoupsValides(jeu)
    return jeu[2]


def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]

def getCopieJeu(jeu,computeCoupsValides=True):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
    """
    p=getPlateau(jeu)
    plateau=[[x for x in l] for l in p]
    sc=[x for x in getScores(jeu)]
    lc=[x for x in getCoupsJoues(jeu)]
    if(computeCoupsValides):
        lv=[x for x in getCoupsValides(jeu)]
    else:
        if(jeu[2]==None):
            lv=None
        else:
            lv=[x for x in jeu[2]]
    return [plateau, getJoueur(jeu),lv,lc, sc]

#def getCopieCoup(coup):
#    """ coup -> coup
#        Retourne une copie du coup
#    """
#    return [x for x in coup]


def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    j=getJoueur(jeu)
    if(j==1):
             jeu[1]=2
    else:
             jeu[1]=1

def getNbLignes(jeu):
    """ jeu->nat
        Retourne le nombre de lignes du plateau
    """
    return len(getPlateau(jeu))
    
def getNbColonnes(jeu):
    """ jeu->nat
        Retourne le nombre de colonnes du plateau
        Hypothese: il existe au moins une ligne et toutes les lignes ont la meme dimension (on se base ici sur la premiere ligne)
    """
    return len(getPlateau(jeu)[0])

def setCaseVal(jeu, ligne, colonne, val):
    """ jeu*nat*nat*nat -> void
        Modifie la case ligne,colonne du jeu en modifiant son contenu avec la valeur val
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    p=getPlateau(jeu)
    p[ligne][colonne]=val
    
def addCaseVal(jeu, ligne, colonne, val):
    """ jeu*nat*nat*int -> void
        Ajoute val a la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    p=getPlateau(jeu)
    p[ligne][colonne]+=val

def addScore(jeu, joueur, val):
    """ jeu*nat*int -> void
        Ajoute val au score du joueur 
        Hypothese: le joueur est 1 ou 2
    """
    s=getScores(jeu)
    s[joueur-1]+=val

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return getScores(jeu)[joueur-1]

def addCoupJoue(jeu,coup):
    """jeu*coup->void
        Ajoute un coup a la liste des coups joues du jeu
    """
    jeu[3].append(coup)

def razCoupsValides(jeu):
    """jeu->void
        Supprime la liste de coups valides
    """
    jeu[2]=None

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    p=getPlateau(jeu)
    return p[ligne][colonne]


def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu     """
    return game.finJeu(jeu)

def majCoupsValides(jeu):
    """jeu->void
        Met a jour la liste des coups valides du jeu
    """
    lv=game.listeCoupsValides(jeu)
    jeu[2]=lv

def coupsEgaux(c1,c2):
    """coup^2->bool
        Retourne vrai si les deux coups sont egaux
    """
    return (c1[0]==c2[0] and c1[1]==c2[1]) 

def coupValide(jeu,coup):
    """jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
    """
    lv=getCoupsValides(jeu)
    for c in lv:
        if coupsEgaux(c,coup):
            return True
    return False

def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
    """
    game.joueCoup(jeu,coup)

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, listes des coups vide, scores a 0 et joueur = 1)
    """
    #print game
    return [game.initPlateau(),1,None,[],game.initScores()]

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    game.finalisePartie(jeu)
    s=getScores(jeu)
    if(s[0]>s[1]):
        return 1
    elif (s[1]>s[0]):
        return 2
    return 0



def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """

    l=getCoupsJoues(jeu)
    x='None'
    if(len(l)>0):
        x=l[len(l)-1]
    print('Coup joue = '+str(x))
    print('Scores = '+str(getScores(jeu)))
    print('Plateau :')
    nl=getNbLignes(jeu)
    nc=getNbColonnes(jeu)
    lig='------'
    lig2='======'
    st='  X  ||'
    for j in range(0,nc):
        st+=getCenteredValInStr(str(j),5)+'|'
        lig+='------'
        lig2+='======'
    print(st)
    print(lig2)
    for i in range(0,nl):
        st=getCenteredValInStr(str(i),5)+'||'
        l=getPlateau(jeu)[i]
        for j in range(0,nc):
            st+=getCenteredValInStr(str(l[j]),5)+'|'
        print(st)
        print(lig)
    #print('\n')
    print('Joueur '+str(getJoueur(jeu))+', a vous de jouer \n')
           

def getCenteredValInStr(val,nb):
    """ str * nat -> str
        Retourne une chaine dans laquelle val est centree, sachant que la chaine fait nb caracteres
        Hypothese: nb>=len(str)
    """
    v=''
    n=len(val)
    for i in range(0,int((nb-n)/2)+((nb-n)%2)):
        v+=' '
    v+=val
    for i in range(0,int((nb-n)/2)):
        v+=' '
    return v
