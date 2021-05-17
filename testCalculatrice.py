from partie1 import *
from partie2 import *
from partie3 import *
from partie4 import *

import json

operations = {
    "add": additionner,
    "sub": soustraire,
    "mul": multiplier,
    "div": diviserAvecReste,
    "min": calculerMinutes,
    "arr": arrondir,
    "nba": calculerNombreA,
    "op": operationListe,
    "doub": enleverDoublons,
    "car":calculerPosVitesseAChaqueCapture,
    "rot": rotationListe
}

def areListsEqual(actual, expected):
    if actual is None and expected is None:
        return True

    is2d = actual is not None and len(actual) > 0 and (type(actual[0]) == tuple or type(actual[0]) == list)
    if is2d:
        # flatten: https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
        actual = [x for sublist in actual for x in sublist]
        expected = [x for sublist in expected for x in sublist]

    return type(actual) == type(expected) and len(actual) == len(expected) and all([actual[i] is not None and abs(expected[i]-actual[i]) < 0.0001 for i in range(len(actual))])

def printReport(funcName, nPassed, report):
    print(f"POUR LA FONCTION {funcName} ===============")
    print(f'\u2714 {nPassed} tests réussi')
    char = "\u274c "
    print(f'{char if len(report) > 0  else ""}{len(report)} tests échoués')

    if len(report) > 0:
        for fail in report[:10]:
            print(f"On s'attendait à {fail['expected']}, mais la fonction a retourné {fail['actual']} avec {fail['operands']}")
        if len(report) > 10:
            print(f"... et {len(report) - 10} erreurs supplémentaires")

def testFunction(key, answersDict):
    report = []
    nPassed = 0

    print(f"\nExécution des tests pour {operations[key].__name__}...")
    for test in answersDict:
        expected = test["res"]
        actual = operations[key](**test["operands"])

        if type(expected) is tuple:
            expected = list(expected)
        if type(actual) is tuple:
            actual = list(actual)

        isList = type(expected) == list or type(expected) == None or type(actual) == list or type(actual) == None

        if areListsEqual(actual, expected) if isList else (actual != None and abs(expected-actual) < 0.0001):
            nPassed += 1
        else:
            report.append({
                "expected": expected,
                "actual": actual,
                "operands": test["operands"]
            })

    printReport(operations[key].__name__, nPassed, report)


def main():
    with open('answers.json', 'r') as file:
        answers = json.load(file)

    for key in answers:
        testFunction(key, answers[key])


if __name__ == "__main__":
    main()
