# TP1-tests

Voici un petit script qui vous permettra de tester vos fonctions de calculatrice!

## Description des fichiers

- `answers.json`: Fichier contenant les réponses attendues, obtenues en roulant le corrigé

- `testCalculatrice.py`: Script qui roule vos fonctions et qui compare les réponses avec celles du corrigé

- `qualiteDuCode/README.md`: Un [fichier](qualiteDuCode/README.md) qui résume les erreurs courantes de qualité du code! Super important, vous êtes notés là-dessus!

## Comment exécuter

Simplement copier-coller les fichiers answers.json et test_calculatrice.py dans votre dossier tp1/ (dans le même dossier que calculatrice.py et partie1-4.py) et exécuter le script avec la commande

```cmd
python test_calculatrice.py
```

Le fichier vous génère un rapport de tous les tests exécutés dans la console. Exemple de test échoué:

```cmd
Exécution des tests pour arrondir...
POUR LA FONCTION arrondir ===============
✔ 0 tests réussi
❌ 100 tests échoués
On s'attendait à 32, mais la fonction a retourné None avec {'nombre': 31, 'facteurArrondissement': 16}
On s'attendait à 66, mais la fonction a retourné None avec {'nombre': 66, 'facteurArrondissement': 1}
On s'attendait à 26, mais la fonction a retourné None avec {'nombre': 25, 'facteurArrondissement': 26}
On s'attendait à 63, mais la fonction a retourné None avec {'nombre': 60, 'facteurArrondissement': 7}
On s'attendait à 50, mais la fonction a retourné None avec {'nombre': 66, 'facteurArrondissement': 50}
On s'attendait à 34, mais la fonction a retourné None avec {'nombre': 35, 'facteurArrondissement': 34}
On s'attendait à 91, mais la fonction a retourné None avec {'nombre': 91, 'facteurArrondissement': 7}
On s'attendait à 76, mais la fonction a retourné None avec {'nombre': 80, 'facteurArrondissement': 38}
On s'attendait à 84, mais la fonction a retourné None avec {'nombre': 85, 'facteurArrondissement': 6}
On s'attendait à 98, mais la fonction a retourné None avec {'nombre': 84, 'facteurArrondissement': 49}
... et 90 erreurs supplémentaires
```

Pour la première réponse par exemple, la réponse attendue est `32`, mais le programme retourne `None`, ce qui n'est pas bon. On voit aussi les nombres passés en paramètres, soit le nombre qu'on voulait arrondir `31` et le facteur d'arrondissement `16`.

## ⚠ Note importante ⚠

Ce n'est pas parce que vos tests passent que vous allez avoir 100%. Comme mentionné en classe, la qualité du code est également un critère très important !! Il est important de bien vérifier vos fonctions et de vous assurer que tout fonctionne bien. Cependant, si tous les tests passent, c'est un bon indicateur que votre logique fonctionne!
