# Qualité de code - erreurs courantes

Voici un petit résumé des erreurs les plus courantes dans les labos :)

## LECTURE

Lisez bien l'énoncé avant de commencer le TP! Beaucoup des erreurs peuvent être facilement évitées, ce sont souvent des erreurs d'inattention ou des manquements qui étaient spécifiés dans l'énoncé ou dans le TODO.

## VARIABLES BOOLÉENNES

Il est facile de faire des erreurs avec les variables booléennes sans s'en rendre compte.

```Python
condition = a < 10

# Mauvais exemple #1
if condition == True:
    faireQqch()

# Mauvais exemple #2
if a < b:
    condition == False

# Mauvais exemple #3
if condition:
    pass
else:
    faireQqch()

# Mauvais exemple #4
if condition:
    faireQqch()
else:
    pass
```

Ce sont des erreurs de redondance : on peut directement le simplifier à:

```Python
condition = a < 10
# condition est déjà un booléen, c'est comme si on disait if False == True ou if True == True,
# on fait juste se répéter!
if condition:
    faireQqch()

# On peut directement assigner une valeur d'une équation booléenne à sa valeur, pas besoin de passer par un if :)
condition = a >= b

# Si on fait un if ou un else avec un pass, c'est qu’on n’en a pas besoin :) Il y a souvent une manière d'inverser
# la condition pour juste utiliser ce dont on a besoin
if not condition:
    faireQqch()

# Même chose pour le else! Si on utilise un pass dans notre else, c'est qu’on n’en a pas vraiment besoin :)
if condition:
    faireQqch()
```

## CHIFFRES MAGIQUES

Pour les chiffres magiques, voici une règle du pouce: Si en relisant votre code vous n'avez pas à penser deux fois à pourquoi vous directement hardcodé telle ou telle valeur, ce n'est pas un chiffre magique. Par exemple, si on veut faire une fonction pour diviser un chiffre en 2, on n'a pas nécessairement besoin d'une constante:

```Python
# Pas besoin
def diviserParDeux(nombre):
    DIVISEUR = 2
    return nombre / DIVISEUR

# OK :)
def diviserParDeux(nombre):
    return nombre / 2
```

En revanche, pour les trucs plus complexes (qui ont nécessités des calculs par exemple ou qui ont une signification
particulière), on veut une constante pour savoir ce que ça représente. Par exemple:

```Python
# Pas clair
def validerPassword(password):
    return password < 7

# OK :)
def validerPassword(password):
    TAILLE_PASSWORD_MAX = 7
    return password < TAILLE_PASSWORD_MAX
```

Comme ça, quand on lit mon code, on comprend tout de suite! Et si on veut changer la taille max de password, on n'a qu'à la changer à une seule place :)

## NOMS DE VARIABLES

Pour les noms de variables, je vois parfois des trucs comme: l, f, m, n, etc. Pour vous qui avez regardé votre code pendant quelques heures, c'est super clair! Pour moi qui corrige, c'est un peu mélangeant ;)

```Python
# Pas clair, êtes-vous capables de dire ce que ce code fait au premier coup d'œil?
def lireFichier():
    c = "./"
    n = "listeDeNombres.txt"

    with open(c + n, 'r') as f:
        t = f.readlines()

    x = []
    for l in t:
        l = l.split()
        y = []
        for v in l:
            y.append(int(v))
        x.append(y)

    return x


# Beaucoup plus facile à lire !!
def lireFichier():
    chemin = "./"
    nom = "listeDeNombres.txt"

    with open(chemin + nom, 'r') as f:
        tableauDeLignes = f.readlines()

    contenu = []
    for ligne in tableauDeLignes:
        ligne = ligne.split()
        nouvelleLigne = []
        for n in ligne:
            nouvelleLigne.append(int(n))
        contenu.append(nouvelleLigne)

    return contenu
```

Comme vous pouvez voir, il y a encore des variables nommées f (standard pour file) et n (en général c'est accepté d'utiliser des variables à une lettre dans un for), mais le code est beaucoup plus clair!

## LISIBILITÉ

La lisibilité du code est un facteur très important. En entreprise, la très grande majorité du code que vous écrirez sera éventuellement passé à un stagiaire ou à un autre employé pour qu'il continue de travailler dessus. Cela veut dire que la capacité d'écrire du code clair et bien documenté est très importante! Par conséquent, sauf dans des cas spécifiques, ce n'est pas une bonne idée de définir une fonction dans une fonction:

```python
# Difficile à suivre, pas très lisible
def areResultEqual(actual, expected):
    def areListsEqual(actual, expected):
        return type(actual) == type(expected) and len(actual) == len(expected) and all([actual[i] is not None and abs(expected[i]-actual[i]) < 0.0001 for i in range(len(actual))])

    def areNumbersEqual(actual, expected):
        return actual != None and abs(expected-actual) < 0.0001

    isList = type(expected) == list or type(expected) == None or type(actual) == list or type(actual) == None
    return areListsEqual(actual, expected) if isList else areNumbersEqual(actual, expected)
```

```python
# OK :)
def areListsEqual(actual, expected):
    return type(actual) == type(expected) and len(actual) == len(expected) and all([actual[i] is not None and abs(expected[i]-actual[i]) < 0.0001 for i in range(len(actual))])

def areNumbersEqual(actual, expected):
    return actual != None and abs(expected-actual) < 0.0001

def areResultEqual(actual, expected):
    isList = type(expected) == list or type(expected) == None or type(actual) == list or type(actual) == None
    return areListsEqual(actual, expected) if isList else areNumbersEqual(actual, expected)
```

Comme vous pouvez voir, l'exemple sans fonctions imbriquées est beaucoup moins dense, et il est plus facile à lire pour une personne qui n'a jamais vu le code. Un bon test est de montrer votre code à un collègue qui ne l'a jamais vu, et de voir s'il comprend en gros ce que le code fait. Les chiffres magiques et les noms de fonctions ou de variables pas clairs nuisent aussi à la lisibilité.

## DUPLICATION DE CODE

Voici la règle du pouce pour la duplication : si à un moment quand vous codez, vous faites ctrl+c, ctrl+v, posez-vous la question "est-ce qu'il y a moyen de généraliser cette ligne?"
Parfois, la duplication est inévitable, mais en général on essaie de la réduire le plus possible. Par exemple, si c'est le même code dans deux ifs différents, c'est habituellement évitable. Pour la lecture d'input ou les conditions qui dépendent de ce qu'on a généré avant, c'est ok d'avoir quelques lignes qui se répètent. Ce n'est pas vraiment applicable au TP1, mais il est important de le garder en tête pour les prochains TPs.

```Python
# Dupliqué
def aTrouveNombreCible(nombreCible, nombreDevine):
    MIN_POSSIBLE = 0
    MAX_POSSIBLE = 100

    if nombreDevine != nombreCible: 
        if nombreDevine > MAX_POSSIBLE:
            print("Le nombre recherché est toujours entre 0 et 100") # !! LIGNE DUPLIQUÉE
        elif nombreDevine < MIN_POSSIBLE:
            print("Le nombre recherché est toujours entre 0 et 100") # !! LIGNE DUPLIQUÉE
        elif nombreCible > nombreDevine:
            print("Le nombre recherché est plus grand!")
        else nombreCible < nombreDevine:
            print("Le nombre recherché est plus petit!")
        return False
    else
        print("Vous avez trouvé le nombre recherché!")
        return True


# OK :)
def aTrouveNombreCible(nombreCible, nombreDevine):
    MIN_POSSIBLE = 0
    MAX_POSSIBLE = 100

    if nombreDevine != nombreCible: 
        if MIN_POSSIBLE > nombreDevine or nombreDevine > MAX_POSSIBLE:
            print("Le nombre recherché est toujours entre 0 et 100") # Plus de ligne dupliquée :)
        elif nombreCible > nombreDevine:
            print("Le nombre recherché est plus grand!")
        else:
            print("Le nombre recherché est plus petit!")
        return False
    else
        print("Vous avez trouvé le nombre recherché!")
        return True
```

Ça sert entre autres à éviter les erreurs! Si on se rend compte qu'il y a une erreur dans une ligne dupliquée et qu'on doit la changer dans 3 fichiers à travers le code, on est plus à risque d'introduire de nouvelles erreurs ou d'oublier de la changer à un endroit!

## POUR RÉSUMER

Les erreurs qu'on fait ressortir ne sont vraiment pas graves, mais c'est vraiment important de prioriser la qualité du code, parce qu'en bout de ligne (surtout en entreprise), il y a souvent quelqu'un qui va réviser votre code, qui va travailler dessus avec vous ou même qui va hériter de votre projet. En insistant sur la qualité autant que sur la performance, on s'assure que vous écrivez du code qui est facilement lisible par n'importe qui :)
